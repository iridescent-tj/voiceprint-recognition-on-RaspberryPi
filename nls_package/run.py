import time
import threading
import sys

import nls


URL="wss://nls-gateway.cn-shanghai.aliyuncs.com/ws/v1"
AKID="LTAI5tBrSdLnacds5up6Be3K"
AKKEY="C5aGXMP9hZZ9M8RrQJ0vWqnvW0cdZJ"
APPKEY="CWrqwVL74fGAUbtt"
my_message = ""

#以下代码会根据音频文件内容反复进行一句话识别
class TestSr:
    def __init__(self, tid, test_file):
        self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid
        self.__test_file = test_file
   
    def loadfile(self, filename):
        with open(filename, "rb") as f:
            self.__data = f.read()
    
    def start(self):
        self.loadfile(self.__test_file)
        self.__th.start()

    def test_on_start(self, message, *args):
        pass
        #print("test_on_start:{}".format(message))

    def test_on_error(self, message, *args):
        pass
        #print("on_error args=>{}".format(args))

    def test_on_close(self, *args):
        pass
        #print("on_close: args=>{}".format(args))

    def test_on_result_chg(self, message, *args):
        pass
        #print("test_on_chg:{}".format(message))

    def test_on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))
        global my_message
        my_message = message[message.find("result") + 9:message.find("duration") - 3]

    def __test_run(self):
        #print("thread:{} start..".format(self.__id))
        
        sr = nls.NlsSpeechRecognizer(
                    url=URL,
                    akid=AKID,
                    aksecret=AKKEY,
                    appkey=APPKEY,
                    on_start=self.test_on_start,
                    on_result_changed=self.test_on_result_chg,
                    on_completed=self.test_on_completed,
                    on_error=self.test_on_error,
                    on_close=self.test_on_close,
                    callback_args=[self.__id]
                )
        if True:
            print("{}: session start".format(self.__id))
            r = sr.start(aformat="pcm", ex={"hello":123})
           
            self.__slices = zip(*(iter(self.__data),) * 640)
            for i in self.__slices:
                sr.send_audio(bytes(i))
                time.sleep(0.01)

            r = sr.stop()
            print("{}: sr stopped:{}".format(self.__id, r))
            time.sleep(1)

def getreply(file,num = 1):
    #设置打开日志输出
    nls.enableTrace(True)
    global my_message
    my_message = ""
    t = TestSr("thread0", file)
    t.start()
    # import time
    # time.sleep(4)
    return my_message

