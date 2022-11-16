'''

import pyaudio 
import time
import speech_recognition as sr


# detect devices:
p = pyaudio.PyAudio()
host_info = p.get_host_api_info_by_index(0)    
device_count = host_info.get('deviceCount')
devices = []

# iterate between devices:
for i in range(0, device_count):
    device = p.get_device_info_by_host_api_device_index(0, i)
    devices.append(device['name'])

print(devices)

di = 0
for ele in devices:
    if "speaker" in ele or "Speaker" in ele:
        di = devices.index(ele)
        print(di)
        break



r = sr.Recognizer()

mic = sr.Microphone()


        

#print(sr.Microphone.list_microphone_names())

#mic = sr.Microphone(device_index=di)


with sr.Microphone() as source:                                                                       
    print("Speak:")
    audio = r.listen(source)


try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

'''


import soundcard as sc
import soundfile as sf

i = 0

def rec():
    global i
    OUTPUT_FILE_NAME = "Audio/out"+str(i)+".wav"    # file name.
    SAMPLE_RATE = 48000              # [Hz]. sampling rate.
    RECORD_SEC = 10                  # [sec]. duration recording audio.

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
        
        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    i += 1
