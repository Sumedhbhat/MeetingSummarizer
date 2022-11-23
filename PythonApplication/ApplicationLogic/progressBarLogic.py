from tkinter import *
from tkinter import ttk
import fileCheckAndLength as fcl
import os
import ocr_logic as ocr
from threading import *

#print(os.path.join(os.getcwd(), "../"))

def progress_bar_logic(p_bar, percent):


    #Check no of files
    t_files = fcl.no_of_files()
    
    for i in range(t_files + 1):
        p_bar['value'] = ((i/t_files) * 100)
        percent.set(str(p_bar['value']) + "% completed")
        p_bar.update_idletasks()


def progress_bar_logic(p_bar, percent):
    
    
    i = 0
    t_files = fcl.no_of_files()
    
    p_bar['value'] = ((i/t_files) * 100)
    percent.set("0% completed")
    p_bar.update_idletasks()
    
    ed = Thread(target = extract_data(p_bar, percent, t_files))
    ed.start()
    
    
    
def extract_data(p_bar, percent, t_files):
    data = ""
    i = 1
    print("Total no of files are: ", t_files)
    
    directory = os.getcwd() + "/Output/Screenshots"
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            data += ocr.image_to_text(f)
            print("Processed image: ",i)
            p_bar['value'] = ((i/t_files) * 100)
            percent.set(str(p_bar['value'])[:5] + "% completed")
            i += 1
            p_bar.update_idletasks()
            
    print("processed. Final data is: ", data)
            
