from tkinter import *
from tkinter import ttk
import fileCheckAndLength as fcl
import os
import ocr_logic as ocr
from threading import Thread

import speech_to_text_converter as srj
import image_compare

i = -1

def progress_bar_logic(progress, p_bar, percent):
    i = 0
    t_files = fcl.no_of_files()
    update_progress_bar(p_bar, percent, t_files)

    files,file_check_values=check_image_similarity(p_bar,percent,t_files)
    ed = Thread(target = extract_data(p_bar, percent, len(files)+t_files,files))
    ed.start()

    speechRecog = Thread(target = extract_speech_data(p_bar, percent, len(files)+t_files,file_check_values))
    speechRecog.start()

    progress.destroy()

    return 1

def update_progress_bar(p_bar, percent, t_files):
    global i
    i += 1
    p_bar['value'] = ((i/t_files) * 100)
    percent.set(str(p_bar['value'])[:5] + "% completed")
    p_bar.update_idletasks()
    
def extract_speech_data(p_bar, percent, t_files,file_check_values):
    audioDirectory = os.path.join(os.getcwd() , "Output","Audio")
    files_in_directory=os.listdir(audioDirectory)
    for index,filename in enumerate(files_in_directory):
        f = os.path.join(audioDirectory, filename)
        if os.path.isfile(f):
            srj.recognize_speech(f, file_check_values[index])
            #print("Processed audio: ",i)
            update_progress_bar(p_bar, percent, t_files)
    speechData=srj.get_final_speech_output()
    print("Processed. Final speech data is: ", speechData)
    print("Length of the data is ", len( speechData ))
    
def extract_data(p_bar, percent, t_files,files):
    data =[] 
    #print("Total no of files are: ", t_files)
    directory = os.path.join(os.getcwd() , "Output","Screenshots")
    for filename in files:
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            data.append(ocr.image_to_text(f))
            #print("Processed image: ",i)
            update_progress_bar(p_bar, percent, t_files)
    print("Processed. Final OCR data is: ", data)
    print("Length of the data is ", len( data ))
            

def check_image_similarity(p_bar,percent,t_files):
    files=[]
    file_check_values=[]
    latest_file=''
    directory= os.getcwd()+"/Output/Screenshots"
    
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if latest_file=='':
            latest_file=f
            files.append(f)
            file_check_values.append(False)
        else:
            finalResult=image_compare.rms_diff(latest_file,f)
            latest_file=f
            if finalResult>=80:
                files.append(f)
                file_check_values.append(True)
            else:
                files[len(files)-1]=f
                file_check_values.append(False)
    return files,file_check_values