import logging
import uuid
from enum import Enum
from io import BytesIO

import math
from pydub import AudioSegment

from zyjj_client_sdk.base import Base, ApiService, MqttServer, MqttEventType
from zyjj_client_sdk.base.entity import TaskInfo
from zyjj_client_sdk.lib import FFMpegService, OSSService
from dataclasses import dataclass
from typing import Callable, Optional, Any


class NodeType(Enum):
    BasicStart = 'basic_start'
    BasicEnd = 'basic_end'
    BasicCode = 'basic_code'
    BasicObjectImport = 'basic_object_import'
    BasicObjectExport = 'basic_object_export'
    ToolGetConfig = 'tool_get_config'
    ToolCostPoint = 'tool_cost_point'
    ToolCheckPoint = 'tool_check_point'
    ToolUploadFile = 'tool_upload_file'
    ToolDownloadFile = 'tool_download_file'
    ToolFileParse = 'tool_file_parse'
    ToolFileExport = 'tool_file_export'
    ToolGetTencentToken = 'tool_get_tencent_token'
    ToolGenerateLocalPath = 'tool_generate_local_path'
    ToolFfmpegPoint = 'tool_ffmpeg_point'
    ToolFfmpeg = 'tool_ffmpeg'


# 节点
@dataclass
class FlowNode:
    node_id: str
    node_type: NodeType
    data: str


@dataclass
class FlowRelation:
    from_id: str
    from_output: str
    to_id: str
    to_input: str


@dataclass
class NodeInfo:
    node_id: str = ''
    node_type: str = ''  # 节点类型
    data: str = ''  # 节点的额外参数
    cost: int = 0  # 执行耗时
    status: int = 0  # 执行状态
    msg: str = ''  # 错误信息


def format_ms(ms: int):
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    # 格式化字符串
    return "{:02d}:{:02d}:{:02d},{:03d}".format(int(hours), int(minutes), int(seconds), int(milliseconds))


# 给flow节点提供的基本方法
class FlowBase:
    def __init__(
            self,
            base: Base,  # 基本信息
            api: ApiService,  # api服务
            mqtt: MqttServer,  # mqtt服务
            global_data: dict,  # 全局数据
            task_info: TaskInfo,  # 任务数据
    ):
        # 一些私有变量，不暴露
        self.__base = base
        self.__ffmpeg = FFMpegService()
        self.__mqtt = mqtt
        self.__global_data = global_data
        self.__task_info = task_info
        self.__node_current: FlowNode | None = None
        self.__node_pre: list[FlowRelation] = []
        self.__node_next: list[FlowRelation] = []
        # 节点的描述信息
        self.__node_desc = {}
        self.__node_log = {}
        # 可以被外部模块使用的变量
        self.api = api
        self.uid = task_info.uid
        self.task_id = task_info.task_id
        self.source = task_info.source

    # 添加节点描述
    def add_desc(self, desc: str):
        if self.__node_current is not None:
            self.__node_desc[self.__node_current.node_id] = desc

    # 获取节点描述
    def get_desc(self) -> dict:
        return self.__node_desc

    # 添加节点日志
    def add_log(self, key: str, value: Any):
        if self.__node_current is None:
            return
        node_id = self.__node_current.node_id
        if node_id not in self.__node_log:
            self.__node_log[node_id] = {}
        self.__node_log[self.__node_current.node_id][key] = value

    def get_log(self) -> dict:
        return self.__node_log

    # 设置当前节点的关联关系
    def set_flow_relation(self, node: FlowNode, prev: list[FlowRelation], after: list[FlowRelation]):
        self.__node_current = node
        self.__node_pre = prev
        self.__node_next = after

    # 获取输入
    def input_get(self) -> dict:
        return self.__task_info.input

    # 获取当前节点需要哪些输出字段
    def node_output_need(self) -> list[str]:
        return [relation.from_output for relation in self.__node_next]

    # 获取存储服务
    def new_oss(self) -> OSSService:
        return OSSService(self.__base, self.api)

    # 生成一个本地路径
    def tool_generate_local_path(self, ext: str) -> str:
        return self.__base.generate_local_file(ext)

    # 音频分割
    @staticmethod
    def audio_split(audio_file: str, chunk_length_s: int = 60, return_bytes: bool = True) -> list:
        audio = AudioSegment.from_mp3(audio_file)
        segments_list = []
        # 计算要切割多少段
        segment_duration = chunk_length_s * 1000
        num_segments = math.ceil(len(audio) / segment_duration)
        for i in range(num_segments):
            start_time = i * segment_duration
            end_time = start_time + segment_duration
            segment = audio[start_time:end_time]
            info = {"start": start_time, "end": end_time}
            # 保存切割后的音频
            if return_bytes:
                byte_io = BytesIO()
                segment.export(byte_io, format="mp3")
                byte_io.seek(0)  # 重置指针到开头
                info["data"] = byte_io.read()
            else:
                name = f"tmp/{uuid.uuid4().hex}.mp3"
                segment.export(name, format="mp3")
                info["data"] = name
            segments_list.append(info)
        return segments_list

    # 字幕格式转srt
    @staticmethod
    def subtitles2srt(subtitles: list) -> bytes:
        srt = ""
        for i, subtitle in enumerate(subtitles):
            srt += f"{i + 1}\n"
            srt += f"{format_ms(subtitle['start'])} --> {format_ms(subtitle['end'])}\n"
            srt += f"{subtitle['text']}\n\n"
        return srt.encode()

    # 获取文件时长
    def ffmpeg_get_duration(self, path: str) -> float:
        return self.__ffmpeg.get_duration(path)

    # 执行ffmpeg任务
    def ffmpeg_execute(self, cmd: str) -> str:
        return self.__ffmpeg.ffmpeg_run(cmd)

    # ffmpeg压缩图片
    def ffmpeg_compress_image(self, img_file: str, quality: int = 5, max_width: int = 1920) -> bytes:
        out = self.tool_generate_local_path('jpg')
        cmd = f"-i {img_file} -q {quality} -vf \"scale='if(gt(iw,{max_width}),{max_width},iw)':'if(gt(ih*{max_width}/iw,ih),ih,ih*{max_width}/iw)'\" {out}"
        self.add_log("cmd", cmd)
        self.ffmpeg_execute(cmd)
        with open(out, "rb") as f:
            return f.read()

    # 触发代码节点
    def tiger_code(self, func_id: str, _input: dict, base=None) -> dict:
        # 获取代码信息
        code_info = self.api.get_func_code(func_id)
        logging.info(f"execute code {code_info}")
        self.add_desc(code_info['name'])
        tmp = {
            "inputs": [_input[unique] if unique in _input else None for unique in code_info["inputs"]],
            "base": base
        }
        exec(f"{code_info['code']}\noutput = handle(*inputs)", tmp)
        out = tmp['output']
        if not isinstance(out, tuple):
            out = (out,)
        output = {}
        for idx, unique in enumerate(code_info["outputs"]):
            output[unique] = out[idx]
        return output

    # mqtt 更新进度
    def mqtt_update_progress(self, progress: float):
        self.__mqtt.send_task_event(self.uid, self.task_id, MqttEventType.Progress, progress)

    # mqtt详情新增
    def mqtt_detail_append(self, data: dict):
        self.__mqtt.send_task_event(self.uid, self.task_id, MqttEventType.DetailAppend, data)


# 处理节点定义
node_define = Callable[[FlowBase, dict, Optional[dict]], dict]
