# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 18:42
# @Author  : Chris
# @Email   : 10512@qq.com
# @File    : utils.py
# @Software: PyCharm
import json
from types import SimpleNamespace


def json_str_to_object(json_str):
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
