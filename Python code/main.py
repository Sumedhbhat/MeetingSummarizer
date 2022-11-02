from tkinter import *
import recordingLogic as rec
from threading import *
import directoryCheck as dc


#Basic
root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

#icon
photo = PhotoImage(file = "Images/recording.png")
root.iconphoto(False, photo)

#background image
bgImageYellow = PhotoImage(file = "Images/yellow.png")
Label(root, image = bgImageYellow, bg="#fff").place(x=-2, y=35)

bgImageBlue = PhotoImage(file = "Images/blue.png")
Label(root, image = bgImageBlue, bg="#fff").place(x=223, y=200)

#Heading
hd = Label(root, text="JOTE - Note Summerizer", bg="#fff", font="arial 15 bold")
hd.pack(pady=10)

nameImg = PhotoImage(file="Images/recording.png")
Label(root, image=nameImg, bd=0).pack(pady=30)

#Entry
fileName = StringVar()
entry = Entry(root, textvariable=fileName, width=18, font="arial 15")
entry.place(x=100, y=310)

#Threading

def record():
    start["state"] = DISABLED
    dc.checkDir()
    t1 = Thread(target = rec.startRecording)
    t1.start()

    t2 = Thread(target = rec.recordSpeech)
    t2.start()

def stopRecord():
    start["state"] = NORMAL
    rec.stopRecording()

#Buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=record)
start.place(x=140, y=230)

pauseBtn = PhotoImage(file="Images/pause.png")
pause = Button(root, image=pauseBtn, bd=0, bg="#fff", command=rec.pauseRecording)
pause.place(x=50, y=450)

resumeBtn = PhotoImage(file="Images/resume.png")
resume = Button(root, image=resumeBtn, bd=0, bg="#fff", command=rec.resumeRecording)
resume.place(x=150, y=450)

stopBtn = PhotoImage(file="Images/stop.png")
stop = Button(root, image=stopBtn, bd=0, bg="#fff", command=stopRecord)
stop.place(x=250, y=450)




root.mainloop()
