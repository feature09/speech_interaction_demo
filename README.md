# speech_interaction_demo
```
在windows10上运行的内容。
Python版本：Python3.6.2。
修改test_demo/main.py中的百度key/图灵key，就可以用。
```

#### 整体的实现流程

1. 语音输入。
2. 语音翻译成文字。
3. 聊天回应文字。
4. 将文字合成语音。
5. 输出语音。

#### 实现方式

1. pyaudio模块识别麦克风
2. 在线百度语音识别，把录音文件转换成文字
3. 在线图灵机器人，对文字进行回答
4. 使用百度的语音合成技术，把文字转为音频文件(要合成MP3格式)
5. 通过pygame识别音频（上一步合成wav文件的话，会识别不出来），输出语音

#### 外部包
```
pip install pyaudio==0.2.11
pip install baidu-aip==2.2.5.2
pip install pygame==1.9.4
```
