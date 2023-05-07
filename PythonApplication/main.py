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

def check_before_start(record_audio, record_video, ask_user_window):
    global root
    if record_audio == 0 and record_video == 0:
        pass
    elif record_video == 0 and record_audio == 1:
        ask_user_window.destroy()
        record(record_audio, record_video, True)
    elif record_video == 1:
        ask_user_window.destroy()

        snip_response = messagebox.askyesno("SELECT", "Do you want to record your full screen?")
        if snip_response == False:
            st.main_logic()
            messagebox.showinfo("INFO!", "Please click the OK button once you have selected the recording area")
        record(record_audio, record_video, snip_response)

def ask_user():

    start["state"] = DISABLED
    start["text"] = "Started"
    start["width"] = 5

    record_screen = IntVar()
    record_audio = IntVar()

    ask_user_window = Toplevel(root)
    ask_user_window.geometry("220x145")
    ask_user_window.title("SELECT")
    ask_user_window_photo = PhotoImage(file="Images/choice.png")
    ask_user_window.iconphoto(False, ask_user_window_photo)
    ask_user_window.resizable(False, False)

    ask_user_text = Label(ask_user_window, text="What do you want to record?")
    ask_user_text_1 = Label(ask_user_window, text="You need to select one or more options")
    video_checkbox = Checkbutton(ask_user_window, text="Meeting screen", variable=record_screen, onvalue=1, offvalue=0)
    audio_checkbox = Checkbutton(ask_user_window, text="Audio", variable=record_audio, onvalue=1, offvalue=0)
    ok_button = Button(ask_user_window, text="OK", width=25, command=lambda : check_before_start(record_audio.get(), record_screen.get(), ask_user_window))

    ask_user_text.grid(row=0, column=0, sticky=W, pady=2)
    ask_user_text_1.grid(row=1, column=0, sticky=W, pady=2)
    video_checkbox.grid(row=2, column=0, sticky=W, pady=2)
    audio_checkbox.grid(row=3, column=0, sticky=W, pady=2)
    ok_button.grid(row=4, column=0)

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
    #entry = Entry(root, textvariable=file_name, width=18, font="arial 15")

    # Threading


    # Buttons
    global start 
    start = Button(root, text="Start", font="arial 22", bd=0, command=ask_user)
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