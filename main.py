import random
import tkinter as tk
import pyautogui

x = 2200
y = 1280
cycle = 0
check = 1
idle_num=[1, 2, 3, 4]
walk_left = [5, 6, 7]
walk_right = [8, 9, 10]
event_number = random.randrange(1, 2, 1)

window = tk.Tk()

idle = [tk.PhotoImage(file='stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_positive = [tk.PhotoImage(file='left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_negative = [tk.PhotoImage(file='right.gif', format = 'gif -index %i' %(i)) for i in range(2)]

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number

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
    label.configure(image = frame)
    window.after(1, event, cycle, check, event_number, x)

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

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
window['bg'] = 'black'

label = tk.Label(window, bd=0, bg='black')
label.pack()

window.after(1, update, cycle, check, event_number, x)

window.mainloop()