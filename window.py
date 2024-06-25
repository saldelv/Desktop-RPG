import random
import tkinter as tk
from character import *
from menus import *
from inventory import *
from shop import *

class Window:
    def __init__(self, character):
        self.root = tk.Tk()
        self.x = 2200
        self.y = 1281
        self.cycle = 0
        self.check = 1
        self.idle_num=[1, 2, 3, 4]
        self.walk_left = [5, 6, 7]
        self.walk_right = [8, 9, 10]
        self.event_number = random.randrange(1, 2, 1)
        self.in_battle = False
        self.battle_distance = 0
        self.battle_moved = 0
        self.finished_battle = False
        self.won = False
        self.character_label = tk.Label(self.root, bd=0, bg='black')
        self.idle = [tk.PhotoImage(file='assets/character/' + str(0) + '/stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.walk_positive = [tk.PhotoImage(file='assets/character/' + str(0) + '/left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.walk_negative = [tk.PhotoImage(file='assets/character/' + str(0) + '/right.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.fight = [tk.PhotoImage(file='assets/character/' + str(0) + '/attack.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.character = character

    def set_window(self):
        # make background transparent and always on top
        self.root.config(highlightbackground='black')
        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', 'black')
        self.root['bg'] = 'black'
        self.root.wm_attributes('-topmost', '1')

    def set_label(self):
        # create character label, tooltip, and right click menu
        self.character_label.pack()

        CreateToolTip(self.character_label, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)

        m = tk.Menu(self.root, tearoff = 0)
        m.add_command(label="Equipment", command=self.go_equipment)
        m.add_command(label="Shop", command=self.go_shop)
        m.add_command(label="Exit", command=lambda: do_quit(self.character))
        self.character_label.bind("<Button-3>", lambda event, menu = m: do_menu(event, menu))

    def start(self):
        # start animating character
         self.root.after(1,  self.update,  self.cycle,  self.check,  self.event_number, self.x)
         self.root.mainloop()

    # Set gifs
    def set_character(self):
        self.idle = [tk.PhotoImage(file='assets/character/' + str(self.character.character_slot) + '/stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.walk_positive = [tk.PhotoImage(file='assets/character/' + str(self.character.character_slot) + '/left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.walk_negative = [tk.PhotoImage(file='assets/character/' + str(self.character.character_slot) + '/right.gif', format = 'gif -index %i' %(i)) for i in range(2)]
        self.fight = [tk.PhotoImage(file='assets/character/' + str(self.character.character_slot) + '/attack.gif', format = 'gif -index %i' %(i)) for i in range(2)]


    # Play gif and potentially change event
    def gif_work(self, cycle, frames, event_number, first_num, last_num):
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            event_number = random.randrange(first_num, last_num + 1, 1)
        return cycle, event_number

    # Update current event
    def update(self, cycle, check, event_number, x):
        # change movement speed and update variables if moving for a battle
        if self.in_battle or self.finished_battle:
            if self.finished_battle:
                movex = 15
                if x >= 2200:
                    self.finished_battle = False
            elif self.battle_moved < self.battle_distance:
                movex = 15
                self.battle_moved += movex
            else:
                movex = 0
        else:
            movex = 3
        # check which animation to play
        self.set_character()
        if check == 0:
            frame = self.idle[cycle]
            cycle, event_number = self.gif_work(cycle, self.idle, event_number, 1, 9)

        elif check == 1:
            frame = self.walk_positive[cycle]
            cycle, event_number = self.gif_work(cycle, self.walk_positive, event_number, 1, 9)
            x -= movex

        elif check == 2:
            frame = self.walk_negative[cycle]
            cycle, event_number = self.gif_work(cycle, self.walk_negative, event_number, 1, 9)
            x += movex 

        elif check == 3:
            frame = self.fight[cycle]
            cycle, event_number = self.gif_work(cycle, self.fight, event_number, 1, 9)

        # move character
        self.root.geometry('100x100+' + str(x) + '+' + str(self.y))
        self.character_label.configure(image = frame)
        
        # don't randomly change event if battling
        if self.in_battle:
            if self.battle_moved < self.battle_distance:
                self.root.after(100, self.update, cycle, 1, event_number, x)
            else:
                self.root.after(400, self.update, cycle, 3, event_number, x)
        elif self.finished_battle:
            self.root.after(100, self.update, cycle, 2, event_number, x)
        # randomly change event when not in battle
        else:
            self.root.after(1, self.set_event, cycle, check, event_number, x)

    # Set event
    def set_event(self, cycle, check, event_number, x):
        if not self.in_battle:
            if event_number in self.idle_num:
                check = 0
                print('idle')
                self.root.after(400, self.update, cycle, check, event_number, x)

            elif event_number in self.walk_left:
                check = 1
                print('walk left')
                self.root.after(100, self.update, cycle, check, event_number, x)

            elif event_number in self.walk_right:
                check = 2
                print('walk right')
                self.root.after(100, self.update, cycle, check, event_number, x)

    def go_equipment(self):
        inventory = Inventory(self.root, self.character, self.character_label)
        inventory.open_equipment()

    def go_shop(self):
        shop = Shop(self.root, self.character, self.character_label)
        shop.open_shop()