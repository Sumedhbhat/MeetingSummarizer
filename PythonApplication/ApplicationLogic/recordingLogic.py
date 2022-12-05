from mss import mss
import random
import string
import time
import speech as s
import directoryCheckAndDelete as dd

record = False


    
def start_recording():
    global record
    record = True
    i = 0
    while record == True:
        with mss() as sct:
            name = 'Output/Screenshots/screenshot'
            name += str(i)
            i += 1
            name += '.png'
            sc_file_name = sct.shot(output = name)
        try:
            time.sleep(5)
        except:
            continue


def pause_recording():
    pass

def resume_recording():
    pass

def stop_recording():
    global record
    record  = False
    

def record_speech():
    while record == True:
        s.rec()
        #time.sleep(11)


def delete_dir():
    dd.delete_dir()
