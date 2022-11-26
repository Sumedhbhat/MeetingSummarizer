from tkinter import *
from tkinter import ttk
from threading import *
import os
import sys

sys.path.append(os.getcwd() + "\ApplicationLogic")
sys.path.append(os.getcwd() + "\OCR")


# Basic
root = Tk()
root.geometry("400x600")
root.title("JOTE - Note Summarizer")
root.config(bg="#fff")
root.resizable(False, False)

# icon
photo = PhotoImage(file="Images/recording.png")
root.iconphoto(False, photo)

# background image
bg_image_yellow = PhotoImage(file="Images/yellow.png")
Label(root, image=bg_image_yellow, bg="#fff").place(x=-2, y=35)

bg_image_blue = PhotoImage(file="Images/blue.png")
Label(root, image=bg_image_blue, bg="#fff").place(x=223, y=200)

# Heading
hd = Label(root, text="JOTE - Note Summerizer",
           bg="#fff", font="arial 15 bold")
hd.pack(pady=10)

name_img = PhotoImage(file="Images/recording.png")
Label(root, image=name_img, bd=0).pack(pady=30)

# Entry
file_name = StringVar()
entry = Entry(root, textvariable=file_name, width=18, font="arial 15")
entry.place(x=100, y=310)

# Threading


def record():
    # Start button
    start["state"] = DISABLED
    start["text"] = "Started"
    start["width"] = 5

    # Pause, resume and stop button
    pause["state"] = "normal"
    resume["state"] = "normal"
    stop["state"] = "normal"

    dc.check_dir()
    t1 = Thread(target=rec.start_recording)
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

    # Check whether file exists
    does_file_exists = fcl.check_file_exists()

    if does_file_exists:
        progress_bar()
    else:
        print("ERROR")


def progress_bar():

    # Create new window
    progress = Toplevel(root)
    progress.title("Generating summary...")
    progress.geometry("500x100")

    # Progress bar
    p_bar = ttk.Progressbar(progress, orient=HORIZONTAL, length=500)
    p_bar.pack(pady=10)

    percent = StringVar()

    percent_label = Label(progress, textvariable=percent)
    percent_label.pack()

    download_btn = Button(
        progress, text="Download the summary", state="disabled").pack()

    pbl.progress_bar_logic(p_bar, percent)

    #downloadBtn["state"] = "normal"


# Buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=record)
start.place(x=140, y=230)

pause_btn = PhotoImage(file="Images/pause.png")
pause = Button(root, image=pause_btn, bd=0, bg="#fff",
               state="disabled", command=rec.pause_recording)
pause.place(x=50, y=450)

resume_btn = PhotoImage(file="Images/resume.png")
resume = Button(root, image=resume_btn, bd=0, bg="#fff",
                state="disabled", command=rec.resume_recording)
resume.place(x=150, y=450)

stop_btn = PhotoImage(file="Images/stop.png")
stop = Button(root, image=stop_btn, bd=0, bg="#fff",
              state="disabled", command=stop_record)
stop.place(x=250, y=450)


root.mainloop()
