from mss import mss
import random
import string
import time
import speech as s
import directoryCheckAndDelete as dd
import snippingTool as st
import os
from threading import *
from tkinter import *
import ocr_logic as ocr
import image_compare
import threading
from datetime import datetime, timedelta

record = True
r_a = 0
r_v = 0
audio_num = 0
video_num = 0
snip_response = True
similarity_values=[]
image_data=[]
files_processed = 0
cur_time = 0

def init_recording(record_audio, record_video, s_r):

    global r_a, r_v, audio_num, video_num, record, snip_response, cur_time
    record = True
    r_a = record_audio
    r_v = record_video
    audio_num = 0
    video_num = 0
    snip_response = s_r

    if record_video == 1:
        record_video_thread = Thread(target=start_recording)
        record_video_thread.start()

    if record_audio == 1:
        cur_time = datetime.now()
        record_audio_thread = threading.Thread(target=record_speech)
        record_audio_thread.start()

def start_recording():
    global record, video_num

    while record == True:
        if snip_response == False:
            filename=st.calculate_dimension(video_num)
            video_num += 1
            Thread(target=gen_image_array(video_num-1,filename)).start()
            Thread(target=gen_image_text_array(video_num-1,filename)).start()
        else:
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
                Thread(target=gen_image_array(video_num-1,name)).start()
                Thread(target=gen_image_text_array(video_num-1,name)).start()
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

    global record, audio_num, cur_time
    while record == True:
        res = s.rec(audio_num, cur_time)
        if res != -1:
            audio_num += 1
            cur_time += timedelta(seconds=10)


def delete_dir():
    dd.delete_dir()

def gen_image_array(index,filename):
    if index==0:
        similarity_values.append(1)
        return
    directory= os.path.join(os.getcwd(),"Output","Screenshots")
    print(filename)
    new_file= os.path.join(os.getcwd(),filename)
    print(new_file)
    com_filename='screenshot'
    com_filename+=str(index-1)
    com_filename+='.png'

    comparing_file = os.path.join(os.getcwd(),'Output','Screenshots',com_filename)
    compare_value=image_compare.rms_diff(new_file,comparing_file)
    similarity_values.append(1)
    if compare_value<80:
        similarity_values[index-1]=0

def gen_image_text_array(index,filename):
    global files_processed
    directory= os.path.join(os.getcwd(),"Output","Screenshots")
    print(filename)
    filepath= os.path.join(os.getcwd(),filename)
    print(filepath)
    while len(image_data)-1<index:
        image_data.append('')
    image_data[index]=ocr.image_to_text(filepath)
    print(files_processed)
    print(filename)
    files_processed += 1