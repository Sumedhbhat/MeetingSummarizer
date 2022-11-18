import whisper
import os
import time

recognizedText = []


def SpeechRecognition(audioFile, newFile):
    file_path = os.path.join(os.curdir, audioFile) 
    print(os.path.exists(file_path))
    print(file_path)
    print(os.path.exists(file_path))
    model = whisper.load_model("base")
    #try:
    result = model.transcribe(file_path, language='en')
    if newFile or len(recognizedText) == 0:
        recognizedText.append(result['text'])
    else:
        recognizedText[len(recognizedText)-1] += result['text']
    print(recognizedText)
    return True
    '''except:
        print("error Occurred")
        #print(result)
        return False'''


SpeechRecognition('out1.wav', False)
#SpeechRecognition('harvard.wav', False)
