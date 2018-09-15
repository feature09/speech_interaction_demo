# -*- coding: utf-8 -*-
# @Time     :2018/9/4
# @Author   :qpf


"""
保存说话音频
"""

import pyaudio
import wave


def record(file_path):


    # 各路参数
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = file_path

    pau = pyaudio.PyAudio()

    stream = pau.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK, )

    frames = []

    print("开始录音")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("结束录音")

    stream.stop_stream()
    stream.close()
    pau.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pau.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
