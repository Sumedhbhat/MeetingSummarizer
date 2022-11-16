from tkinter import *
from tkinter import ttk
import recordingLogic as rec
from threading import *
import directoryCheck as dc
import progressBarLogic as pbl
import fileCheckAndLength as fcl

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
bgImageYellow = PhotoImage(file="Images/yellow.png")
Label(root, image=bgImageYellow, bg="#fff").place(x=-2, y=35)

bgImageBlue = PhotoImage(file="Images/blue.png")
Label(root, image=bgImageBlue, bg="#fff").place(x=223, y=200)

# Heading
hd = Label(root, text="JOTE - Note Summerizer",
           bg="#fff", font="arial 15 bold")
hd.pack(pady=10)

nameImg = PhotoImage(file="Images/recording.png")
Label(root, image=nameImg, bd=0).pack(pady=30)

# Entry
fileName = StringVar()
entry = Entry(root, textvariable=fileName, width=18, font="arial 15")
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

    dc.checkDir()
    t1 = Thread(target=rec.startRecording)
    t1.start()

    t2 = Thread(target=rec.recordSpeech)
    t2.start()


def stopRecord():

    # Disable states
    start["state"] = DISABLED
    start["text"] = "Start"
    stop["state"] = DISABLED
    pause["state"] = DISABLED
    resume["state"] = DISABLED

    # Stop recording
    rec.stopRecording()

    # Check whether file exists
    doesFileExists = fcl.checkFileExists()

    if doesFileExists:
        progressBar()
    else:
        print("ERROR")


def progressBar():

    # Create new window
    progress = Toplevel(root)
    progress.title("Generating summary...")
    progress.geometry("500x100")

    # Progress bar
    pBar = ttk.Progressbar(progress, orient=HORIZONTAL, length=500)
    pBar.pack(pady=10)

    percent = StringVar()

    percentLabel = Label(progress, textvariable=percent)
    percentLabel.pack()

    downloadBtn = Button(
        progress, text="Download the summary", state="disabled").pack()

    pbl.progressBarLogic(pBar, percent)

    #downloadBtn["state"] = "normal"


# Buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=record)
start.place(x=140, y=230)

pauseBtn = PhotoImage(file="Images/pause.png")
pause = Button(root, image=pauseBtn, bd=0, bg="#fff",
               state="disabled", command=rec.pauseRecording)
pause.place(x=50, y=450)

resumeBtn = PhotoImage(file="Images/resume.png")
resume = Button(root, image=resumeBtn, bd=0, bg="#fff",
                state="disabled", command=rec.resumeRecording)
resume.place(x=150, y=450)

stopBtn = PhotoImage(file="Images/stop.png")
stop = Button(root, image=stopBtn, bd=0, bg="#fff",
              state="disabled", command=stopRecord)
stop.place(x=250, y=450)


mainloop()
