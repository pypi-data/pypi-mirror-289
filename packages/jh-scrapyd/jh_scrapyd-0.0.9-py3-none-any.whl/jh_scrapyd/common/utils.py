import json


def str_decode(b: str):
    """字符串解码"""
    if isinstance(b, bytes):
        return b.decode('utf-8', errors='ignore')
    else:
        return str(b)


def data_encode(input_dict: dict):
    """编码成json格式的数据"""
    return json.dumps(input_dict)


def data_decode(input_dict: str):
    """解码json格式的数据"""
    return json.loads(input_dict)
