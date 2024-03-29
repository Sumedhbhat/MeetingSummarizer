import soundcard as sc
import soundfile as sf
import time
import os 
from threading import Thread
import speech_to_text_converter as srj
import recordingLogic as rl
from datetime import datetime, timedelta


audio_data=[]

def rec(audio_num, start_time):
    filename='out'+str(audio_num)+'.wav'
    OUTPUT_FILE_NAME = os.path.join('Output','Audio',filename)
    SAMPLE_RATE = 48000              # [Hz]. sampling rate.
    RECORD_SEC = 10              # [sec]. duration recording audio.

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        #print(current_time)
        #print(OUTPUT_FILE_NAME)
        directory= os.path.join(os.getcwd(),"Output","Audio")
        #print(directory)
        #print(os.listdir(directory))
        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        bef_save_time = datetime.now()
        difference = (bef_save_time - start_time).total_seconds()

        if difference < 9:
            return -1
        else:
            sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
            Thread(target=gen_speech_data,args=(audio_num,OUTPUT_FILE_NAME,)).start()
            return 1

def gen_speech_data(index,filename):
    filepath = os.path.join(os.getcwd(),filename)
    result=srj.speech_convertor(filepath)
    while len(audio_data)-1<index:
        audio_data.append('')
    #print("Audio Data result")
    audio_data[index]=result
    rl.files_processed+=1
    #print(audio_data)