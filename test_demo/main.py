# -*- coding: utf-8 -*-
# @Time     :2018/9/4
# @Author   :qpf

from test_demo import input_record, recognition_speech, tuling_robot

from test_demo import compound_speech, output_redio

# 存放的文件名称
file_path = "record-audio.wav"
# 百度需要的参数
APP_ID = '换成自己的'
API_KEY = '换成自己的'
SECRET_KEY = '换成自己的'
# 图灵需要的参数
TULING_KEY = '换成自己的'

# 先调用录音函数
input_record.record(file_path)

# 语音转成文字的内容
input_message = recognition_speech.voice2text(APP_ID, API_KEY, SECRET_KEY, file_path)
print(input_message)
print(type(input_message))

# 获取回答信息
answer = tuling_robot.answer(input_message[0], TULING_KEY)
print(answer)


tuling_answer_path = 'tuling-answer.mp3'  # 语音存放的位置

# 将文字转化为语音
text = answer['text']
print("text===", text)
compound_speech.text2voice(APP_ID, API_KEY, SECRET_KEY, answer['text'], tuling_answer_path)

# 播放图灵回答的内容
output_redio.speak(tuling_answer_path)
