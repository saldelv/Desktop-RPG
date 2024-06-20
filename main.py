import random
import tkinter as tk
import pyautogui
import base64
import zlib
import tempfile
import pickle
from pathlib import Path
from database import *

############################
#        Inventory         #
############################

def open_equipment():
    eroot = tk.Toplevel(root)
    eroot.resizable(0, 0)
    ex = root.winfo_x() - 125
    ey = root.winfo_y() - 200
    eroot.geometry("+%d+%d" % (ex, ey))
    eroot.wm_attributes('-topmost', '1')
    
    weapon = get_equipped(0, eroot)
    headgear = get_equipped(1, eroot)
    chestpiece = get_equipped(2, eroot)
    leggings = get_equipped(3, eroot)
    boots = get_equipped(4, eroot)

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

def get_equipped(slot, eroot):
    match slot:
        case 0:
            func = get_weapon
            empty = 'Empty Sword.png'
            item = "Sword"
        case 1:
            func = get_helmet
            empty = 'Empty Helmet.png'
            item = "Helmet"
        case 2:
            func = get_chestpiece
            empty = 'Empty Chestpiece.png'
            item = "Chestpiece"
        case 3:
            func = get_leggings
            empty = 'Empty Leggings.png'
            item = "Leggings"
        case 4:
            func = get_boots
            empty = 'Empty Boots.png'
            item = "Boots"

    button = tk.Button(eroot, command=lambda: open_inventory(slot, eroot))
    if equiped[slot] != "":
        img = tk.PhotoImage(file = 'assets/items/' + equiped[slot] + '.png', master=eroot)
        rows = func(equiped[slot])
        for row in rows:
            if slot == 0:
                stat = "Attack: "
            else:
                stat = "Defense: "
            CreateToolTip(button, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]), h = 25, w = 0)

        em = tk.Menu(root, tearoff = 0)
        em.add_command(label="Unequip", command=lambda: remove_equip(slot, eroot))
        em.add_command(label="Sell", command=lambda: sell_equip(slot, -1, [], eroot))
        button.bind("<Button-3>", lambda event, menu = em: do_menu(event, menu))
    else:
        img = tk.PhotoImage(file = 'assets/items/' + empty, master=eroot)
        CreateToolTip(button, text=item, h = 25, w = 0)
    button.configure(image=img)
    button.image = img
    
    return button


def open_inventory(slot, eroot):
    match slot:
        case 0:
            inv = weapon_inventory
            func = get_weapon
        case 1:
            inv = helmet_inventory
            func = get_helmet
        case 2:
            inv = chestpiece_inventory
            func = get_chestpiece
        case 3:
            inv = leggings_inventory
            func = get_leggings
        case 4:
            inv = boots_inventory
            func = get_boots
    
    iroot = tk.Toplevel(eroot)
    iroot.resizable(0, 0)
    ix = eroot.winfo_x() - 170
    iy = eroot.winfo_y() - 70
    iroot.geometry("+%d+%d" % (ix, iy))
    iroot.wm_attributes('-topmost', '1')

    index = 0
    for i in range(5):
        for j in range(5):
            b = tk.Button(iroot)
            if index < len(inv):
                if inv[index]:
                    img = tk.PhotoImage(file = "assets/items/" + inv[index] + ".png", master=iroot)
                    current = index
                    b.configure(image=img, command=lambda: new_equip(slot, current, iroot, eroot))
                    b.image = img

                    rows = func(inv[index])
                    for row in rows:
                        if slot == 0:
                            stat = "Attack: "
                        else:
                            stat = "Defense: "
                        CreateToolTip(b, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]), h = 25, w = 0)
                    
                    im = tk.Menu(root, tearoff = 0)
                    im.add_command(label="Sell", command=lambda: sell_equip(slot, current, inv, iroot))
                    b.bind("<Button-3>", lambda event, menu = im: do_menu(event, menu))

                index += 1
            else:
                img = tk.PhotoImage(file = "assets/items/empty.png", master=iroot)
                b.configure(image=img)
                b.image=img

            b.grid(row=i, column=j)

def new_equip(slot, current, iroot, eroot):
    global attack
    global defense

    match slot:
        case 0:
            inv = weapon_inventory
            func = get_weapon
        case 1:
            inv = helmet_inventory
            func = get_helmet
        case 2:
            inv = chestpiece_inventory
            func = get_chestpiece
        case 3:
            inv = leggings_inventory
            func = get_leggings
        case 4:
            inv = boots_inventory
            func = get_boots
    
    if not equiped[slot]:
        equiped[slot] = inv[current]
        inv.remove(inv[current])

        rows = func(equiped[slot])
        for row in rows:
            if slot > 0:
                defense += row[1]
            else:
                attack += row[1]

    else:
        rows = func(equiped[slot])
        for row in rows:
            if slot > 0:
                defense -= row[1]
            else:
                attack -= row[1]
        
        temp = equiped[slot]
        equiped[slot] = inv[current]
        inv[current] = temp

        rows = func(equiped[slot])
        for row in rows:
            if slot > 0:
                defense += row[1]
            else:
                attack += row[1]
    
    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    iroot.destroy()
    eroot.destroy()
    open_equipment()

def remove_equip(slot, eroot):
    global attack
    global defense

    match slot:
        case 0:
            inv = weapon_inventory
            func = get_weapon
        case 1:
            inv = helmet_inventory
            func = get_helmet
        case 2:
            inv = chestpiece_inventory
            func = get_chestpiece
        case 3:
            inv = leggings_inventory
            func = get_leggings
        case 4:
            inv = boots_inventory
            func = get_boots

    inv.append(equiped[slot])

    rows = func(equiped[slot])
    for row in rows:
        if slot > 0:
            defense -= row[1]
        else:
            attack -= row[1]
    
    equiped[slot] = ""

    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    eroot.destroy()
    open_equipment()

def sell_equip(slot, current, inv, a_root):
    global gold
    global attack
    global defense
    match slot:
            case 0:
                func = get_weapon
            case 1:
                func = get_helmet
            case 2:
                func = get_chestpiece
            case 3:
                func = get_leggings
            case 4:
                func = get_boots

    if current < 0:
        rows = func(equiped[slot])
        for row in rows:
            gold += row[2]
            if slot > 0:
                defense -= row[1]
            else:
                attack -= row[1]
        
        equiped[slot] = ""

        a_root.destroy()
        open_equipment()

    else:
        rows = func(inv[current])
        for row in rows:
            gold += row[2]

        inv.remove(inv[current])
        a_root.destroy()

    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

############################
#        Character         #
############################

root = tk.Tk()

# Default variables
x = 2200
y = 1280
cycle = 0
check = 1
idle_num=[1, 2, 3, 4]
walk_left = [5, 6, 7]
walk_right = [8, 9, 10]
event_number = random.randrange(1, 2, 1)
in_battle = False
battle_distance = 0
battle_moved = 0
finished_battle = False

# Set gifs
idle = [tk.PhotoImage(file='assets/character/stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_positive = [tk.PhotoImage(file='assets/character/left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_negative = [tk.PhotoImage(file='assets/character/right.gif', format = 'gif -index %i' %(i)) for i in range(2)]
fight = [tk.PhotoImage(file='assets/character/attack.gif', format = 'gif -index %i' %(i)) for i in range(2)]


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
    global battle_moved, finished_battle
    if in_battle or finished_battle:
        if finished_battle:
            movex = 15
            if x >= 2200:
                finished_battle = False
        elif battle_moved < battle_distance:
            movex = 15
            battle_moved += movex
        else:
            movex = 0
    else:
        movex = 3
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

    elif check == 1:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= movex

    elif check == 2:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += movex 

    elif check == 3:
        frame = fight[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += movex 

    root.geometry('100x100+' + str(x) + '+' + str(y))
    character.configure(image = frame)
    if in_battle:
        if battle_moved < battle_distance:
            root.after(100, update, cycle, 1, event_number, x)
        else:
            root.after(400, update, cycle, 3, event_number, x)
    elif finished_battle:
        root.after(100, update, cycle, 2, event_number, x)
    else:
        root.after(1, set_event, cycle, check, event_number, x)

# Set event
def set_event(cycle, check, event_number, x):
    if not in_battle:
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

############################
#         Battles          #
############################

def spawn_enemy():
    timer = 0

    enemy = tk.Label(enemy_root, bd=0, bg='black')

    enemy.place(x = random.randrange(0, 400), y = -50)
    root.after(1, play_enemy(enemy, 0))

    enemy.bind("<Button-1>", lambda event: start_battle(enemy))

    enemy.health = 100
    enemy.max_health = 100
    enemy.attack = 1
    enemy.defense = 1
    enemy.experience = 10
    CreateToolTip(enemy, text = "Slime" + "\nHealth: " + str(enemy.health), h = 0, w = 50)

    root.after(60000, lambda: despawn_enemy(enemy))
    root.after(30000, spawn_enemy)

def despawn_enemy(enemy):
    enemy.destroy()

def play_enemy(enemy, current_frame):
    img = [tk.PhotoImage(file='assets/enemies/slime.gif', format = 'gif -index %i' %(i)) for i in range(6)]
    frame = img[current_frame]
    enemy.configure(image = frame)
    enemy.image = frame
    current_frame = current_frame + 1
    if current_frame == len(img):
        current_frame = 0
    if not finished_battle:
        root.after(200, lambda: play_enemy(enemy, current_frame))
    else:
        despawn_enemy(enemy)

def start_battle(enemy):
    global in_battle, battle_distance
    if not in_battle:
        in_battle = True
        battle_distance = (x - 1850) + (310-enemy.winfo_x())
    
    if battle_moved >= battle_distance:
        enemy_health = tk.Label(enemy_root, text = "Enemy:\n" + str(enemy.health) + "/" + str(enemy.max_health))
        enemy_health.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
        player_health = tk.Label(enemy_root, text = "Player:\n" + str(health) + "/" + str(max_health))
        player_health.place(x = enemy.winfo_x() + 225, y = enemy.winfo_y() + 50)
        root.after(400, lambda: update_battle(enemy, enemy_health, player_health))
    else:
        root.after(100, lambda: start_battle(enemy))

def update_battle(enemy, enemy_health, player_health):
    global health, experience, in_battle, finished_battle, battle_distance, battle_moved, level
    enemy.health -= max(attack - enemy.defense, 0)
    health -= max(enemy.attack - defense, 0)
    enemy_health.configure(text = "Enemy:\n" + str(max(enemy.health, 0)) + "/" + str(enemy.max_health))
    player_health.configure(text = "Player:\n" + str(max(health, 0)) + "/" + str(max_health))

    if enemy.health <= 0:
        print("win")
        experience += enemy.experience
        if experience >= 100 and level < 5:
            level = level + 1
            experience = experience - 100
        health = max_health

        UnbindToolTip(character)
        CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)
        
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()

        match random.randrange(0, 5):
            case 0:
                inv = weapon_inventory
                name = "Sword"
            case 1:
                inv = helmet_inventory
                name = "Helmet"
            case 2:
                inv = chestpiece_inventory
                name = "Chestpiece"
            case 3:
                inv = leggings_inventory
                name = "Leggings"
            case 4:
                inv = boots_inventory
                name = "Boots"

        chance = random.randrange(0, 100)
        if (chance > 95):
            drop = "Legendary Level " + str(level) + " " + name
        elif (chance > 85):
            drop = "Epic Level " + str(level) + " " + name
        elif (chance > 70):
            drop = "Rare Level " + str(level) + " " + name
        elif (chance > 50):
            drop = "Uncommon Level " + str(level) + " " + name
        elif (chance > 20):
            drop = "Common Level " + str(level) + " " + name
        else:
            drop = ""
        
        print(drop)
        if drop != "":
            inv.append(drop)
            drop_text = tk.Label(enemy_root, text = "Obtained " + drop)
            drop_text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
            root.after(3000, lambda: destroy_text(drop_text))

    elif health <= 0:
        print("lose")
        health = max_health
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()

    elif health == 100 and enemy.health == 100:
        print("draw")
        health = max_health
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()

    else:
        print("next turn")
        root.after(200, lambda: update_battle(enemy, enemy_health, player_health))

    def destroy_text(drop_text):
        drop_text.destroy()

############################
#          Menus           #
############################

# Tooltip hover class
class Tooltip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tiproot = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text, h, w):
        self.text = text
        if self.tiproot or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + w
        y = y + cy + self.widget.winfo_rooty() - h
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
    
def CreateToolTip(widget, text, h, w):
    tooltip = Tooltip(widget)
    def enter(set_event):
        tooltip.showtip(text, h, w)
    def leave(set_event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def UnbindToolTip(widget):
    widget.unbind('<Enter>')
    widget.unbind('<Leave')

def do_menu(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

############################
#          Stats           #
############################

def do_quit():
    with open('savefile.dat', 'wb') as f:
        pickle.dump([level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory], f)

    quit()

# Saved stats
if (Path('savefile.dat').exists()):
    with open('savefile.dat', 'rb') as f:
        level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory = pickle.load(f)
else:
    level = 1
    experience = 0
    health = 100
    gold = 0
    attack = 7
    defense = 1
    equiped = ["", "", "", "", ""]
    weapon_inventory = ["Common Level 1 Sword", "Uncommon Level 1 Sword"]
    helmet_inventory = ["Legendary Level 1 Helmet"]
    chestpiece_inventory = ["Rare Level 1 Chestpiece"]
    leggings_inventory = []
    boots_inventory = []
max_health = health

############################
#           Main           #
############################

if __name__ == "__main__":

    # Make background transparent and always on top
    root.config(highlightbackground='black')
    root.overrideredirect(True)
    root.wm_attributes('-transparentcolor', 'black')
    root['bg'] = 'black'
    root.wm_attributes('-topmost', '1')

    character = tk.Label(root, bd=0, bg='black')
    character.pack()

    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    m = tk.Menu(root, tearoff = 0)
    m.add_command(label="Equipment", command=open_equipment)
    m.add_command(label="Exit", command=do_quit)
    character.bind("<Button-3>", lambda event, menu = m: do_menu(event, menu))

    enemy_root = tk.Toplevel(root)
    enemy_root.config(highlightbackground='black')
    enemy_root.overrideredirect(True)
    enemy_root.wm_attributes('-transparentcolor', 'black')
    enemy_root['bg'] = 'black'
    enemy_root.wm_attributes('-topmost', '1')

    enemy_root.geometry("+%d+%d" % (x - 800, y))
    enemy_root.geometry('700x500')

    root.after(1, update, cycle, check, event_number, x)
    enemy_root.after(3000, spawn_enemy)

    root.mainloop()