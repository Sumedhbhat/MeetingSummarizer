import whisper
import os
import time

recognizedText = []


def recognize_speech(audioFile, newFile):
    file_path = os.path.join(os.curdir, audioFile) 
    #print(os.path.exists(file_path))
    #print(file_path)
    #print(os.path.exists(file_path))
    model = whisper.load_model("base")
    result = model.transcribe(file_path, language='en')
    if newFile or len(recognizedText) == 0:
        recognizedText.append(result['text'])
    else:
        recognizedText[len(recognizedText)-1] += result['text']
    return recognizedText