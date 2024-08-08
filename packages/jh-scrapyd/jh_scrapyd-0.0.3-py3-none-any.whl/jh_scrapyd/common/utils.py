import json


def hash_data_encode(input_dict: dict):
    """编码成哈希格式的数据"""
    return {str(key): json.dumps(value) for key, value in input_dict.items()}


def hash_data_decode(input_dict: dict):
    """解码哈希格式的数据"""
    return {k.decode('utf-8'): json.loads(v.decode('utf-8')) for k, v in input_dict.items()}
