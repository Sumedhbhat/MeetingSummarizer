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
import snippingTool as st
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import *
from fpdf import FPDF
from datetime import datetime
from pathlib import Path
import pywinctl as pwc
from pywinauto import application
import pygetwindow

def maximize(window_chosen, options, window_selector,record_audio, record_video, snip_response):
    if window_chosen.get() not in options:
        pass
    else:
        global root
        app_name = window_chosen.get()
        app = application.Application().connect(title=app_name)
        main_window = app.top_window()
        main_window.minimize()
        main_window.maximize()
        window_selector.destroy()

        if snip_response == False:

            snip_window = Tk()
            st.main_logic(snip_window)

            try:
                while snip_window.state() == 'normal':
                    messagebox.showinfo("INFO!", "Please click the OK button once you have selected the recording area")
        
            except:
                pass
        
        record(record_audio, record_video, snip_response)

def select_window_to_record(record_audio, record_video, snip_response):
    global root
    window_selector = Toplevel(root)
    window_selector.geometry("350x100")
    window_selector.title("Select window")
    window_selector.resizable(False, False)

    allow_label = Label(window_selector, text="Choose which screen or window to record")
    allow_label.place(x=0,y=0)

    options = list(pwc.getAllTitles())

    window_chosen = StringVar()
    window_chosen.set("Select window or screen")
    
    window_dropdown = OptionMenu(window_selector, window_chosen , *options )
    window_dropdown.place(x=10,y=30)

    window_button = Button(window_selector, text="OK", command=lambda: maximize(window_chosen, options, window_selector, record_audio, record_video, snip_response))
    window_button.place(x=300,y=70) 



def check_before_start(record_audio, record_video):
    global root
    swtr_res = False
    if record_audio == 0 and record_video == 0:
        pass
    elif record_video == 0 and record_audio == 1:
        record(record_audio, record_video, True)
    elif record_video == 1:

        snip_response = messagebox.askyesno("SELECT", "Do you want to record your full screen?")

        select_window_to_record(record_audio, record_video, snip_response)

def ask_user():

    start["state"] = DISABLED
    start["text"] = "Started"
    start["width"] = 5

    record_screen = IntVar()
    record_audio = IntVar()

    audio_response = messagebox.askyesno("REQUIRED", "Do you want to record the meeting audio?")
    video_response = messagebox.askyesno("REQUIRED", "Do you want to record the meeting screen?")

    while audio_response == False and video_response == False:
        messagebox.showwarning("NEEDED!", "JOTE can't work without audio and video. Either audio or video or both are needed.")
        audio_response = messagebox.askyesno("REQUIRED", "Do you want to record the meeting audio?")
        video_response = messagebox.askyesno("REQUIRED", "Do you want to record the meeting screen?")

    if audio_response == True:
        record_audio = 1
    else:
        record_audio = 0

    if video_response == True:
        record_screen = 1
    else:
        record_screen = 0

    check_before_start(record_audio, record_screen)

def show_disclaimer():
    disclaimer_message = "To generate the summary, system audio will be recorded and screenshots of your meeting will be taken frequently. However, once you click the start button, you can select whether to record audio, video or not. All the recorded audio and screenshots are stored locally in your system. Once the summary is generated, JOTE deletes all of these recordings and screenshots."

    response = messagebox.askokcancel("DISCLAIMER", disclaimer_message)

    if response == True:
        ask_user()
    else:
        gar_collector()

def record(record_audio, record_video, snip_response):
    global root
    # Start button
    start["state"] = DISABLED
    start["text"] = "Started"
    start["width"] = 5

    # Pause, resume and stop button
    pause["state"] = "normal"
    resume["state"] = DISABLED
    stop["state"] = "normal"
    dc.delete_dir()
    dc.check_dir()

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("start time",current_time)

    print("Audio : {}, Video : {}".format(record_audio, record_video))

    rec.init_recording(record_audio, record_video, snip_response)

    root.iconify()


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
    root.config(bg="white")
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
    #entry = Entry(root, textvariable=file_name, width=18, font="arial 15")

    # Threading


    # Buttons
    global start 
    start = Button(root, text="Start", font="arial 22", bd=0, command=show_disclaimer)
    start.place(x=140, y=230)

    pause_btn = PhotoImage(file=os.path.join("Images","pause.png"))
    global pause 
    pause = Button(root, image=pause_btn, bd=0, bg="#fff",
                state="disabled", command=lambda : rec.pause_recording(stop, resume, pause))
    pause.place(x=50, y=450)

    resume_btn = PhotoImage(file=os.path.join("Images","resume.png"))
    global resume 
    resume = Button(root, image=resume_btn, bd=0, bg="#fff",
                    state="disabled", command=lambda:rec.resume_recording(stop, resume, pause))
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

