import random
import tkinter as tk
from tkinter import Toplevel, Label, LEFT, SOLID
import pyautogui

# Tooltip hover class
class Tooltip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() - 25
        y = y + cy + self.widget.winfo_rooty() - 70
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        tw.wm_attributes('-topmost', '1')
        tlabel = Label(tw, text=self.text, justify=LEFT, bg='white', relief=SOLID, borderwidth=1, font='Gill')
        tlabel.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
    
def CreateToolTip(widget, text):
    tooltip = Tooltip(widget)
    def enter(event):
        tooltip.showtip(text)
    def leave(event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Default variables
x = 2200
y = 1280
cycle = 0
check = 1
idle_num=[1, 2, 3, 4]
walk_left = [5, 6, 7]
walk_right = [8, 9, 10]
event_number = random.randrange(1, 2, 1)

window = tk.Tk()

# Set gifs
idle = [tk.PhotoImage(file='stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_positive = [tk.PhotoImage(file='left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_negative = [tk.PhotoImage(file='right.gif', format = 'gif -index %i' %(i)) for i in range(2)]


# Play gif and potentially change event
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number

# Update current event
def update(cycle, check, event_number, x):
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

    elif check == 1:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3

    elif check == 2:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += 3

    window.geometry('100x100+' + str(x) + '+' + str(y))
    character.configure(image = frame)
    window.after(1, event, cycle, check, event_number, x)

# Set event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)

    elif event_number in walk_left:
        check = 1
        print('walk left')
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in walk_right:
        check = 2
        print('walk right')
        window.after(100, update, cycle, check, event_number, x)

# Make background transparent and always on top
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
window['bg'] = 'black'
window.wm_attributes('-topmost', '1')

character = tk.Label(window, bd=0, bg='black')
character.pack()

CreateToolTip(character, text = "Health: 100/100 \nStrength: 1 \nDefense: 1")

window.after(1, update, cycle, check, event_number, x)

window.mainloop()