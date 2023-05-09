import whisper
import os
import time
import replicate

recognized_text = []


def recognize_speech(audioFile, newFile):
    file_path = os.path.join(os.curdir, audioFile) 
    model = whisper.load_model("base")
    result = model.transcribe(file_path, language='en')
    if newFile or len(recognized_text) == 0:
        recognized_text.append(result['text'])
    else:
        recognized_text[len(recognized_text)-1] += result['text']
    return result['transcription']
    #print(os.path.exists(file_path))
    #print(file_path)
    #print(os.path.exists(file_path))

def speech_convertor(audio_file):
    output = replicate.run(
    "openai/whisper:e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc",
    input={"audio": open(audio_file, "rb")}
    )
    print(output['transcription'])
    print(audio_file)
    return output['transcription']

def get_final_speech_output():
    return recognized_text

# # Speech Recognition function to convert Speech to Text
# def SpeechRecognition(audioFile, newFile):
#     file_path = os.path.join(os.curdir, audioFile) 
#     model = whisper.load_model("base")
#     result = model.transcribe(file_path, language='en')
#     if newFile or len(recognizedText) == 0:
#         recognizedText.append(result['text'])
#     else:
#         recognizedText[len(recognizedText)-1] += result['text']
#     return recognizedText