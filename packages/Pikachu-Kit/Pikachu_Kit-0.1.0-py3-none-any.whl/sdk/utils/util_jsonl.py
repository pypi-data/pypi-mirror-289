# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_jsonl.py
@time: 2024/7/31 14:53 
@desc: 

"""
from sdk.utils.util_json import JsonProcess


class JSONL(object):
    """

    """

    def __init__(self):
        self.json = JsonProcess()

    def read_yield_jsonl(self, file, encoding="utf-8"):
        """

        :param file:
        :param encoding:
        :return:
        """
        with open(file, "r", encoding=encoding) as fp:
            for i in fp:
                yield self.json.loads(i.strip())

    def write_to_jsonl(self, file, data):
        """

        :param file:
        :param data: [{}]
        :return:
        """
        with open(file, "w", encoding="utf-8") as fp:
            for i in data:
                fp.write(self.json.dumps(i, indent=None))
