# -*- coding: utf-8 -*-
# @Time     :2018/9/11
# @Author   :qpf

"""
将文字合成语音
"""

from aip import AipSpeech


def text2voice(APP_ID, API_KEY, SECRET_KEY, text, file_path):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'per': 4,
    })

    if not isinstance(result, dict):
        with open(file_path, 'wb') as f:
            f.write(result)
