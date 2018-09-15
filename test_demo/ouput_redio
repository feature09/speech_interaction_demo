# -*- coding: utf-8 -*-
# @Time     :2018/9/11
# @Author   :qpf


"""
播放音频文件
"""

import pygame


def speak(name):
    # frequency用来控制语速，去掉试一下就明白了。。。
    pygame.mixer.init(frequency=16000, size=0)

    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()


if __name__ == '__main__':
    speak("tuling-answer.mp3")
