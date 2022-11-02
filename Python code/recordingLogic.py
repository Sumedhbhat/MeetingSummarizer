from mss import mss
import random
import string
import time
import speech as s

record = False


    
def startRecording():
    global record
    record = True
    i = 0
    while record == True:
        #print(id(record), record, "start")
        with mss() as sct:
            name = 'Screenshots/screenshot'
            name += str(i)
            i += 1
            name += '.png'
            scFileName = sct.shot(output = name)
        try:
            time.sleep(10)
        except:
            continue


def pauseRecording():
    pass

def resumeRecording():
    pass

def stopRecording():
    global record
    record  = False
    #print(id(record), record, "Stop")


def recordSpeech():
    while record == True:
        s.rec()
        time.sleep(11)
    

#startRecording()
