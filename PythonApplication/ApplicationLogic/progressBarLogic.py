from tkinter import *
from tkinter import ttk
import fileCheckAndLength as fcl
import os
import ocr_logic as ocr
from threading import *

import speech_to_text_converter as srj



i = -1

def progress_bar_logic(progress, p_bar, percent):
    
    
    i = 0
    t_files = fcl.no_of_files()

    update_progress_bar(p_bar, percent, t_files)
    
    ed = Thread(target = extract_data(p_bar, percent, t_files))
    ed.start()

    speechRecog = Thread(target = extract_speech_data(p_bar, percent, t_files))
    speechRecog.start()

    progress.destroy()

    return 1

def update_progress_bar(p_bar, percent, t_files):
    global i
    i += 1
    p_bar['value'] = ((i/t_files) * 100)
    percent.set(str(p_bar['value'])[:5] + "% completed")
    p_bar.update_idletasks()

    
def extract_speech_data(p_bar, percent, t_files):
    speechData = []

    audioDirectory = os.getcwd() + "/Output/Audio"
    
    for filename in os.listdir(audioDirectory):
        f = os.path.join(audioDirectory, filename)
        if os.path.isfile(f):
            speechData.append(srj.recognize_speech(f, False))
            #print("Processed audio: ",i)
            update_progress_bar(p_bar, percent, t_files)
            
    print("Processed. Final speech data is: ", speechData)
    
    
    
def extract_data(p_bar, percent, t_files):
    data = ""
    #print("Total no of files are: ", t_files)
    
    directory = os.getcwd() + "/Output/Screenshots"
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            data += ocr.image_to_text(f)
            #print("Processed image: ",i)
            update_progress_bar(p_bar, percent, t_files)
            
    print("Processed. Final OCR data is: ", data)
            
