# -*- coding: utf-8 -*-
# @Time     :2018/9/4
# @Author   :qpf

"""
对本地语音文件解析成文字
"""

from aip import AipSpeech


def voice2text(APP_ID, API_KEY, SECRET_KEY, file_path):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    ret = client.asr(get_data(file_path), 'pcm', 16000, {'dev_pid': 1536}, )
    return ret['result']


def get_data(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()
