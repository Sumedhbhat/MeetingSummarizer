import soundcard as sc
import soundfile as sf
import time
import os 
from recordingLogic import files_processed
from threading import Thread
import speech_to_text_converter as srj

audio_data=[]

def rec(audio_num):
    filename='out'+str(audio_num)+'.wav'
    OUTPUT_FILE_NAME = os.path.join('Output','Audio',filename)
    SAMPLE_RATE = 48000              # [Hz]. sampling rate.
    RECORD_SEC = 10              # [sec]. duration recording audio.

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print(OUTPUT_FILE_NAME)
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print(OUTPUT_FILE_NAME)
        directory= os.path.join(os.getcwd(),"Output","Audio")
        print(directory)
        print(os.listdir(directory))
        Thread(target=gen_speech_data,args=(i,OUTPUT_FILE_NAME,)).start()
        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

def gen_speech_data(index,filename):
    global files_processed
    filepath = os.path.join(os.getcwd(),'Output','Audio',filename)
    result=srj.speech_convertor(filepath)
    while len(audio_data)-1<index:
        audio_data.append('')
    print("Audio Data result")
    audio_data[index]=result
    files_processed+=1
    print(audio_data)