from mss import mss
import random
import string
import time
import speech as s
import directoryCheckAndDelete as dd
import os
from threading import *
from tkinter import *

record = True
r_a = 0
r_v = 0
audio_num = 0
video_num = 0
    
def init_recording(record_audio, record_video):

    global r_a, r_v, audio_num, video_num, record
    record = True
    r_a = record_audio
    r_v = record_video
    audio_num = 0
    video_num = 0

    if record_video == 1:
        record_video_thread = Thread(target=start_recording)
        record_video_thread.start()

    if record_audio == 1:
        record_audio_thread = Thread(target=record_speech)
        record_audio_thread.start()

def start_recording():
    global record, video_num

    while record == True:
        with mss() as sct:
            filename='screenshot'
            filename += str(video_num)
            video_num += 1
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            filename += '.png'
            name = os.path.join('Output','Screenshots',filename)
            print(name)
            sc_file_name = sct.shot(output = name)
        try:
            time.sleep(10)
        except:
            continue

def pause_recording(stop, resume, pause):
    pause["state"] = DISABLED
    resume["state"] = "normal"
    stop["state"] = DISABLED

    global record
    record = False

def resume_recording(stop, resume, pause):
    resume["state"] = DISABLED
    stop["state"] = "normal"
    pause["state"] = "normal"

    global record, r_a, r_v
    record = True

    if r_v == 1:
        record_video_thread = Thread(target=start_recording)
        record_video_thread.start()

    if r_a == 1:
        record_audio_thread = Thread(target=record_speech)
        record_audio_thread.start()
    

def stop_recording():
    global record
    record  = False
    

def record_speech():

    global record, audio_num
    while record == True:
        s.rec(audio_num)
        audio_num += 1


def delete_dir():
    dd.delete_dir()
