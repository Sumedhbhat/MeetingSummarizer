from tkinter import *
from tkinter import ttk
import fileCheckAndLength as fcl


def progressBarLogic(pBar, percent):


    #Check no of files
    tFiles = fcl.noOfFiles()
    
    for i in range(tFiles + 1):
        pBar['value'] = ((i/tFiles) * 100)
        percent.set(str(pBar['value']) + "% completed")
        pBar.update_idletasks()
