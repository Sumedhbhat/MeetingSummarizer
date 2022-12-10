import soundcard as sc
import soundfile as sf
import os 

i = 0

def rec():
    global i
    filename='out'+str(i)+'.wav'
    OUTPUT_FILE_NAME = os.path.join('Output','Audio',filename)
    SAMPLE_RATE = 48000              # [Hz]. sampling rate.
    RECORD_SEC = 10                  # [sec]. duration recording audio.

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
        
        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
    i += 1
