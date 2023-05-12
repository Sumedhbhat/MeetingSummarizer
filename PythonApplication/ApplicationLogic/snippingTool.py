from tkinter import *
import pyautogui
import os
import gc

start_x, start_y, current_x, current_y = 0, 0, 0, 0

def destroy_snip():
    snip_window = None
    gc.collect()

def take_bounded_screenshot(x1, y1, x2, y2, video_num):
    print("Capturing image")
    image = pyautogui.screenshot(region=(x1, y1, x2, y2))
    filename='screenshot'
    filename += str(video_num)
    filename += ".png"
    name = os.path.join('Output','Screenshots',filename)
    print(name)
    image.save(name)
    return name

def send_coords(s_x, s_y, c_x, c_y):
    print("Sending coords")
    global start_x, start_y, current_x, current_y
    start_x = s_x
    start_y = s_y
    current_x = c_x
    current_y = c_y

def calculate_dimension(n):
    global start_x, start_y, current_x, current_y
    filepath=''
    if start_x <= current_x and start_y <= current_y:
        filepath=take_bounded_screenshot(start_x, start_y, current_x - start_x, current_y - start_y,n)

    elif start_x >= current_x and start_y <= current_y:
        filepath=take_bounded_screenshot(current_x, start_y, start_x - current_x, current_y - start_y,n)

    elif start_x <= current_x and start_y >= current_y:
        filepath=take_bounded_screenshot(start_x, current_y, current_x - start_x, start_y - current_y,n)

    elif start_x >= current_x and start_y >= current_y:
        filepath=take_bounded_screenshot(current_x, current_y, start_x - current_x, start_y - current_y,n)
    return filepath
    

class Application():
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
    
        snip_window.title('Snipping Tool')
        snip_window.geometry('200x150')
        snip_window.resizable(False, False)

        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=1)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        self.snipButton = Button(self.buttonBar, width=20, text="Click to select area", command=self.create_screen_canvas)
        self.snipButton.pack(padx=10, pady=50)

        self.master_screen = Toplevel(snip_window)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def create_screen_canvas(self):
        self.master_screen.deiconify()
        snip_window.withdraw()

        self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.snip_surface.pack(fill=BOTH, expand=YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.display_rectangle_position()
        send_coords(self.start_x, self.start_y, self.current_x, self.current_y)
        self.exit_snip_mode()
        return event

    def exit_snip_mode(self):
        self.snip_surface.destroy()
        self.master_screen.withdraw()
        #snip_window.destroy()
        destroy_snip()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.snip_surface.canvasx(event.x)
        self.start_y = self.snip_surface.canvasy(event.y)
        self.snip_surface.create_rectangle(0, 0, 1, 1, outline='red', width=3, fill="maroon3")

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.snip_surface.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    def display_rectangle_position(self):
        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)

snip_window = None
app = None

def main_logic(s_w):
    global snip_window, app
    snip_window = s_w
    app = Application(snip_window)
    snip_window.focus_force()
    return None
    snip_window.mainloop()