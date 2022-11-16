import whisper
import os

file_path = os.path.join(os.curdir, "..", "Audio", "out0.wav")

model = whisper.load_model("small")
result = model.transcribe('harvard.wav')
print(result)
