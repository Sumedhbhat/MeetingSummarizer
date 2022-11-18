from tkinter import *
from tkinter import ttk
import fileCheckAndLength as fcl


def progress_bar_logic(p_bar, percent):


    #Check no of files
    t_files = fcl.no_of_files()
    
    for i in range(t_files + 1):
        p_bar['value'] = ((i/t_files) * 100)
        percent.set(str(p_bar['value']) + "% completed")
        p_bar.update_idletasks()
