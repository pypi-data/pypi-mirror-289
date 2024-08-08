# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 18:42
# @Author  : Chris
# @Email   : 10512@qq.com
# @File    : utils.py
# @Software: PyCharm
import json
import random
import string
from types import SimpleNamespace


def json_str_to_object(json_str):
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))


def text_mid(origin_text: str, front_string: str, back_string: str, start_position: int = 0) -> str:
    try:
        front_pos = origin_text.index(front_string, start_position) + len(front_string)
        back_pos = origin_text.index(back_string, front_pos)
        return origin_text[front_pos: back_pos]
    except ValueError:
        return ""


def text_random_str(count: int = 1) -> str:
    result = random.choice(string.ascii_letters)
    letters = string.ascii_letters + string.digits
    for i in range(count - 1):
        result += random.choice(letters)
    return result
