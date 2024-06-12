import random
import tkinter as tk
import pyautogui
import base64
import zlib
import tempfile
import pickle
from pathlib import Path

# Tooltip hover class
class Tooltip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tiproot = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tiproot or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() - 25
        y = y + cy + self.widget.winfo_rooty() - 70
        self.tiproot = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        tw.wm_attributes('-topmost', '1')
        tlabel = tk.Label(tw, text=self.text, justify=tk.LEFT, bg='white', relief=tk.SOLID, borderwidth=1, font='Gill')
        tlabel.pack(ipadx=1)

    def hidetip(self):
        tw = self.tiproot
        self.tiproot = None
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

def do_menu(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def open_equipment():
    eroot = tk.Toplevel(root)
    eroot.resizable(0, 0)
    ex = root.winfo_x() - 125
    ey = root.winfo_y() - 200
    eroot.geometry("+%d+%d" % (ex, ey))
    eroot.wm_attributes('-topmost', '1')

    sword_image = tk.PhotoImage(file = 'sword.png', master=eroot)
    weapon = tk.Button(eroot, text = "Weapon", image = sword_image, command=lambda: equip(0, eroot))
    weapon.image = sword_image
    headgear = tk.Button(eroot, text="Headgear", command=lambda: equip(1, eroot))
    chestpiece = tk.Button(eroot, text="Chest Piece", command=lambda: equip(2, eroot))
    leggings = tk.Button(eroot, text="Leggings", command=lambda: equip(3, eroot))
    boots = tk.Button(eroot, text="Boots", command=lambda: equip(4, eroot))

    weapon.pack()
    headgear.pack()
    chestpiece.pack()
    leggings.pack()
    boots.pack()

    # transparent icon
    ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
    eroot.iconbitmap(default=ICON_PATH)
    
    eroot.mainloop()

def equip(slot, eroot):
    iroot = tk.Toplevel(eroot)
    iroot.resizable(0, 0)
    ix = eroot.winfo_x() - 170
    iy = eroot.winfo_y() - 70
    iroot.geometry("+%d+%d" % (ix, iy))
    iroot.wm_attributes('-topmost', '1')

    for i in range(5):
        for j in range(5):
            b = tk.Button(iroot, height=1, width=3, command = iroot.destroy)
            b.grid(row=i, column=j)

def do_quit():
    with open('savefile.dat', 'wb') as f:
        pickle.dump([level, health, gold], f)
    quit()

# Saved stats
if (Path('savefile.dat').exists()):
    with open('savefile.dat', 'rb') as f:
        level, health, gold = pickle.load(f)
else:
    level = 1
    health = 100
    gold = 0

# Default variables
x = 2200
y = 1280
cycle = 0
check = 1
idle_num=[1, 2, 3, 4]
walk_left = [5, 6, 7]
walk_right = [8, 9, 10]
event_number = random.randrange(1, 2, 1)

root = tk.Tk()

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

    root.geometry('100x100+' + str(x) + '+' + str(y))
    character.configure(image = frame)
    root.after(1, event, cycle, check, event_number, x)

# Set event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        root.after(400, update, cycle, check, event_number, x)

    elif event_number in walk_left:
        check = 1
        print('walk left')
        root.after(100, update, cycle, check, event_number, x)

    elif event_number in walk_right:
        check = 2
        print('walk right')
        root.after(100, update, cycle, check, event_number, x)

# Make background transparent and always on top
root.config(highlightbackground='black')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'black')
root['bg'] = 'black'
root.wm_attributes('-topmost', '1')

character = tk.Label(root, bd=0, bg='black')
character.pack()

CreateToolTip(character, text = "Health: " + str(health) + "/100 \nStrength: 1 \nDefense: 1")

m = tk.Menu(root, tearoff = 0)
m.add_command(label="Inventory", command=open_equipment)
m.add_command(label="Exit", command=do_quit)
character.bind("<Button-3>", do_menu)

root.after(1, update, cycle, check, event_number, x)

root.mainloop()