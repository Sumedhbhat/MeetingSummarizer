import gc
import os
import sys
import time
import platform

sys.path.append(os.path.join(os.getcwd() , "ApplicationLogic"))
sys.path.append(os.path.join(os.getcwd() , "OCR"))
sys.path.append(os.path.join(os.getcwd() , "SpeechToTextConverter"))
sys.path.append(os.path.join(os.getcwd() , "ComparisonOfImages"))
sys.path.append(os.path.join(os.getcwd() , "Summarizer"))

import fileCheckAndLength as fcl
import progressBarLogic as pbl
import directoryCheckAndDelete as dc
import recordingLogic as rec
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import *
from fpdf import FPDF
from datetime import datetime
from pathlib import Path


def record():
    # Start button
    start["state"] = DISABLED
    start["text"] = "Started"
    start["width"] = 5

    # Pause, resume and stop button
    pause["state"] = "normal"
    resume["state"] = "normal"
    stop["state"] = "normal"
    dc.delete_dir()
    dc.check_dir()
    t1 = Thread(target=rec.start_recording)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("start time",current_time)
    t1.start()

    # rec.record_speech()
    t2 = Thread(target=rec.record_speech)
    t2.start()


def stop_record():

    # Disable states
    start["state"] = DISABLED
    start["text"] = "Start"
    stop["state"] = DISABLED
    pause["state"] = DISABLED
    resume["state"] = DISABLED

    # Stop recording
    rec.stop_recording()
    
    #Check whether file exists
    does_file_exists = fcl.check_file_exists()

    if does_file_exists:
        progress_thread = Thread(target = progress_bar)
        progress_thread.start()
    else:
        messagebox.showerror("File Error", "Something went wrong! Please try again later.")

def write_to_file(rtnValue):

    try:
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        date_time_str = str(date_time_str)
        date_time_str += ".pdf"
        date_time_str = date_time_str.replace(" ","")
        date_time_str = date_time_str.replace(":","")
        date_time_str = date_time_str.replace("-","")

        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()

        pdf.set_font('Arial', 'BU', 16)
        pdf.cell(60)
        pdf.cell(60, 10, 'SUMMARY OF THE MEETING', 0, 1, 'C')
        pdf.cell(0, 3, "\n", 0, 1, 'L')

        rtnValue = rtnValue.encode('latin-1', 'replace').decode('latin-1')
        pdf.set_font('Times', '', 12)
        pdf.multi_cell(0, 5, rtnValue, 0, 1, 'L')
        
        downloads_path = str(Path.home() / "Downloads")

        if platform.system() == 'Windows':
            print("In Windows")
            download_location = downloads_path + '\\' + date_time_str
        else:
            print("In other OS")
            download_location = downloads_path + '/' + date_time_str

        pdf.output(download_location, 'F')

        return download_location
    
    except:
        messagebox.showerror("Length Error", "Something went wrong! Please try again later.")
        sys.exit(0)

def progress_bar():

    #print("Root is: ",root)
    # Create new window
    progress = Toplevel(root)
    progress.title("Generating summary...")
    progress.geometry("300x75")
    progress_photo = PhotoImage(file="Images/summary.png")
    progress.iconphoto(False, progress_photo)
    progress.resizable(False, False)

    # Progress bar
    p_bar = ttk.Progressbar(progress, orient=HORIZONTAL, length=450)
    p_bar.pack(padx=10,pady=10)

    percent = StringVar()

    percent_label = Label(progress, textvariable=percent)
    percent_label.pack()

    rtnValue = pbl.progress_bar_logic(progress, p_bar, percent)

    if rtnValue != -1:
        loc = write_to_file(rtnValue)
        os.startfile(loc)
        messagebox.showinfo("SUCCESS", "Summary has been generated. \nLocation - "+loc)
    start["state"] = "normal"

    rec.delete_dir()
    
def gar_collector():
    root = None
    gc.collect()
    sys.exit(0) 
    
def main_logic():

    # Basic
    global root
    root = Tk()
    root.geometry("400x600")
    root.title("JOTE - Note Summarizer")
    root.config(bg="#fff")
    root.resizable(False, False)

    # icon
    photo = PhotoImage(file="Images/recording.png")
    root.iconphoto(False, photo)

    # background image
    bg_image_yellow = PhotoImage(file=os.path.join("Images","yellow.png"))
    Label(root, image=bg_image_yellow, bg="#fff").place(x=-2, y=35)

    bg_image_blue = PhotoImage(file=os.path.join("Images","blue.png"))
    Label(root, image=bg_image_blue, bg="#fff").place(x=223, y=200)

    # Heading
    hd = Label(root, text="JOTE - Note Summarizer",
            bg="#fff", font="arial 15 bold")
    hd.pack(pady=10)

    name_img = PhotoImage(file=os.path.join("Images","recording.png"))
    Label(root, image=name_img, bd=0).pack(pady=30)

    # Entry
    file_name = StringVar()
    entry = Entry(root, textvariable=file_name, width=18, font="arial 15")
    entry.place(x=100, y=310)

    # Threading


    # Buttons
    global start 
    start = Button(root, text="Start", font="arial 22", bd=0, command=record)
    start.place(x=140, y=230)

    pause_btn = PhotoImage(file=os.path.join("Images","pause.png"))
    global pause 
    pause = Button(root, image=pause_btn, bd=0, bg="#fff",
                state="disabled", command=rec.pause_recording)
    pause.place(x=50, y=450)

    resume_btn = PhotoImage(file=os.path.join("Images","resume.png"))
    global resume 
    resume = Button(root, image=resume_btn, bd=0, bg="#fff",
                    state="disabled", command=rec.resume_recording)
    resume.place(x=150, y=450)

    stop_btn = PhotoImage(file=os.path.join("Images","stop.png"))
    global stop 
    stop = Button(root, image=stop_btn, bd=0, bg="#fff",
                state="disabled", command=stop_record)
    stop.place(x=250, y=450)

    root.protocol('WM_DELETE_WINDOW', gar_collector)

    root.mainloop()

    


main_thread = Thread(target=main_logic)
main_thread.start()