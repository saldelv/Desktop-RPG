import random
import tkinter as tk
import pyautogui
import base64
import zlib
import tempfile
import pickle
from pathlib import Path
import os
from database import *

############################
#        Inventory         #
############################

# open equipment menu
def open_equipment():
    # create window
    eroot = tk.Toplevel(root)
    eroot.resizable(0, 0)
    ex = root.winfo_x() - 125
    ey = root.winfo_y() - 200
    eroot.geometry("+%d+%d" % (ex, ey))
    eroot.wm_attributes('-topmost', '1')
    
    # get equipped data
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

# get equipped data
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

    # create buttons with stats and images of equipped items and commands
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

# open inventory for equipping in a specific slot
def open_inventory(slot, eroot):
    # getting correct slot info
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
    
    # new window
    iroot = tk.Toplevel(eroot)
    iroot.resizable(0, 0)
    ix = eroot.winfo_x() - 170
    iy = eroot.winfo_y() - 70
    iroot.geometry("+%d+%d" % (ix, iy))
    iroot.wm_attributes('-topmost', '1')

    # creating grid of items in invetory with stats and images
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

# equipping new item
def new_equip(slot, current, iroot, eroot):
    print("e")
    global attack
    global defense

    # getting correct slot info
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
    
    # move item to equipped if empty and chage stats
    if not equiped[slot]:
        equiped[slot] = inv[current]
        inv.remove(inv[current])

        rows = func(equiped[slot])
        for row in rows:
            if slot > 0:
                defense += row[1]
            else:
                attack += row[1]

    # swap item with equipped if not empty and change stats
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
    
    # reload windows and tooltip
    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    iroot.destroy()
    eroot.destroy()
    open_equipment()

# unequip item
def remove_equip(slot, eroot):
    global attack
    global defense

    # get correct slot info
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

    # move item to inventory and change stats
    inv.append(equiped[slot])

    rows = func(equiped[slot])
    for row in rows:
        if slot > 0:
            defense -= row[1]
        else:
            attack -= row[1]
    
    equiped[slot] = ""

    # reload window and tooltip
    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    eroot.destroy()
    open_equipment()

# sell item
def sell_equip(slot, current, inv, a_root):
    global gold
    global attack
    global defense
    
    # get correct slot info
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

    # unequip, add gold and change stats if equipped
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

    # remove from inventory and add gold if not equipped
    else:
        rows = func(inv[current])
        for row in rows:
            gold += row[2]

        inv.remove(inv[current])
        a_root.destroy()

    # reload windows and tooltip
    UnbindToolTip(character)
    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

############################
#           Shop           #
############################

#open shop window
def open_shop():
    # new window
    sroot = tk.Toplevel(root)
    sroot.resizable(0, 0)
    sx = root.winfo_x() - 270
    sy = root.winfo_y() - 170
    sroot.geometry("+%d+%d" % (sx, sy))
    sroot.wm_attributes('-topmost', '1')

    #create buttons with each character in folder
    i = 0
    path = 'assets/character'
    for f in os.listdir(path):
        filepath = os.path.join(path, f)
        if not os.path.isdir(filepath):
            b = tk.Button(sroot)
            img = tk.PhotoImage(file = filepath, master=sroot)
            b.configure(image=img, command=lambda i = i: change_character(sroot, i))
            b.image = img
            b.grid(row = 0, column = i)

            # check if unlocked
            if shop_status[i] == True:
                CreateToolTip(b, text="Unlocked", h = 25, w = 0)
            else:
                CreateToolTip(b, text="Price: 150 Gold", h = 25, w = 0)

            i += 1

# change current character
def change_character(sroot, slot):
    global gold, character_slot
    # change character if unlocked
    if shop_status[slot] == True:
        character_slot = slot
        set_character()
        sroot.destroy()
    # check if character can be purchased and change
    else:
        if gold >= 150:
            gold -= 150
            shop_status[slot] = True
            character_slot = slot
            set_character()
            UnbindToolTip(character)
            CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)
            sroot.destroy()

############################
#        Character         #
############################

# create root
root = tk.Tk()

# Default variables
x = 2200
y = 1281
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
won = False

# default gifs
idle = [tk.PhotoImage(file='assets/character/' + str(0) + '/stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_positive = [tk.PhotoImage(file='assets/character/' + str(0) + '/left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
walk_negative = [tk.PhotoImage(file='assets/character/' + str(0) + '/right.gif', format = 'gif -index %i' %(i)) for i in range(2)]
fight = [tk.PhotoImage(file='assets/character/' + str(0) + '/attack.gif', format = 'gif -index %i' %(i)) for i in range(2)]

# Set gifs
def set_character():
    global idle, walk_positive, walk_negative, fight
    idle = [tk.PhotoImage(file='assets/character/' + str(character_slot) + '/stand.gif', format = 'gif -index %i' %(i)) for i in range(2)]
    walk_positive = [tk.PhotoImage(file='assets/character/' + str(character_slot) + '/left.gif', format = 'gif -index %i' %(i)) for i in range(2)]
    walk_negative = [tk.PhotoImage(file='assets/character/' + str(character_slot) + '/right.gif', format = 'gif -index %i' %(i)) for i in range(2)]
    fight = [tk.PhotoImage(file='assets/character/' + str(character_slot) + '/attack.gif', format = 'gif -index %i' %(i)) for i in range(2)]


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
    # change movement speed and update variables if moving for a battle
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
    # check which animation to play
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
        cycle, event_number = gif_work(cycle, fight, event_number, 1, 9)

    # move character
    root.geometry('100x100+' + str(x) + '+' + str(y))
    character.configure(image = frame)
    
    # don't randomly change event if battling
    if in_battle:
        if battle_moved < battle_distance:
            root.after(100, update, cycle, 1, event_number, x)
        else:
            root.after(400, update, cycle, 3, event_number, x)
    elif finished_battle:
        root.after(100, update, cycle, 2, event_number, x)
    # randomly change event when not in battle
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

# spawn enemy after certain time
def spawn_enemy():
    timer = 0

    # creating random enemy in random location
    enemy = tk.Label(enemy_root, bd=0, bg='black')

    enemy.place(x = random.randrange(0, 400), y = -50)

    type = random.randrange(0, 3)
    match type:
            case 0:
                name = 'Slime'
            case 1:
                name = 'Wolf'
            case 2:
                name = 'Goblin'

    root.after(1, play_enemy(enemy, 0, name))

    # click on enemy to start battle
    enemy.bind("<Button-1>", lambda event: start_battle(enemy))

    # get and assign enemy stats
    enemy.health = 0
    enemy.max_health = 0
    enemy.attack = 0
    enemy.defense = 0
    enemy.experience = 0

    rows = get_enemies('Level ' + str(level) + " " + name)
    for row in rows:
        enemy.health = row[1]
        enemy.max_health = row[1]
        enemy.attack = row[2]
        enemy.defense = row[3]
        enemy.experience = row[4]

    CreateToolTip(enemy, text = "Level " + str(level) + " " + name + "\nHealth: " + str(enemy.health), h = 0, w = 50)

    # spawn next enemy and despawn current enemy after certain times
    root.after(60000, lambda: despawn_enemy(enemy))
    root.after(30000, spawn_enemy)

# unload enemy
def despawn_enemy(enemy):
    enemy.destroy()

# play enemy gif
def play_enemy(enemy, current_frame, name):
    img = [tk.PhotoImage(file='assets/enemies/' + name + '.gif', format = 'gif -index %i' %(i)) for i in range(6)]
    frame = img[current_frame]
    enemy.configure(image = frame)
    enemy.image = frame
    current_frame = current_frame + 1
    if current_frame == len(img):
        current_frame = 0
    global won
    # get rid of enemy if defeated in battle
    if not won:
        root.after(200, lambda: play_enemy(enemy, current_frame, name))
    else:
        despawn_enemy(enemy)
        won = False

# start battle
def start_battle(enemy):
    global in_battle, battle_distance
    # set battle variable and calculate distance to enemy
    if not in_battle:
        in_battle = True
        battle_distance = (x - 1850) + (300-enemy.winfo_x())
    
    # create health labels and start fighting if moved to enemy
    if battle_moved >= battle_distance:
        enemy_health = tk.Label(enemy_root, text = "Enemy:\n" + str(enemy.health) + "/" + str(enemy.max_health))
        enemy_health.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
        player_health = tk.Label(enemy_root, text = "Player:\n" + str(health) + "/" + str(max_health))
        player_health.place(x = enemy.winfo_x() + 260, y = enemy.winfo_y() + 50)
        root.after(400, lambda: update_battle(enemy, enemy_health, player_health))
    # keep moving until reached enemy
    else:
        root.after(100, lambda: start_battle(enemy))

# fighting
def update_battle(enemy, enemy_health, player_health):
    global health, experience, in_battle, finished_battle, battle_distance, battle_moved, level, max_health, won
    # update healths based on stats
    enemy.health -= max(attack - (enemy.defense * 0.5), 0)
    health -= max(enemy.attack - (defense * 0.5), 0)
    enemy_health.configure(text = "Enemy:\n" + str(max(enemy.health, 0)) + "/" + str(enemy.max_health))
    player_health.configure(text = "Player:\n" + str(max(health, 0)) + "/" + str(max_health))

    # players wins battle
    if enemy.health <= 0:
        print("win")
        # gain experience and level up
        experience += enemy.experience
        if experience >= 100 and level < 5:
            level = level + 1
            experience = experience - 100
            max_health += 20
        health = max_health

        UnbindToolTip(character)
        CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)
        
        # set variables to end battle and move back
        won = True
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()

        # random drop slot
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

        # random drop rarity
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
        
        # give drop to player and show label
        print(drop)
        text = tk.Label(enemy_root, text = "Win!")
        if drop != "" and len(inv) < 25:
            inv.append(drop)
            text.configure(text = "Win! \nObtained " + drop)
        text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
        root.after(3000, lambda: destroy_text(text))

    # player loses battle
    elif health <= 0:
        # set variables to end battle and move back
        print("lose")
        health = max_health
        enemy.health = enemy.max_health
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()
        text = tk.Label(enemy_root, text = "Lose...")
        text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
        root.after(3000, lambda: destroy_text(text))

    # battle ties if no damage is done
    elif health == max_health and enemy.health == enemy.max_health:
        # set variables to end battle and move back
        print("draw")
        in_battle = False
        finished_battle = True
        battle_distance = 0
        battle_moved = 0
        player_health.destroy()
        enemy_health.destroy()
        text = tk.Label(enemy_root, text = "Draw")
        text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
        root.after(3000, lambda: destroy_text(text))

    # next turn of attacking
    else:
        print("next turn")
        root.after(1000, lambda: update_battle(enemy, enemy_health, player_health))

    # destroys drop text after certain time
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
    
# creates tool tip with text and relative location
def CreateToolTip(widget, text, h, w):
    tooltip = Tooltip(widget)
    def enter(set_event):
        tooltip.showtip(text, h, w)
    def leave(set_event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# deletes tooltip
def UnbindToolTip(widget):
    widget.unbind('<Enter>')
    widget.unbind('<Leave')

# creates right click menues
def do_menu(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

############################
#          Stats           #
############################

# saves stats and inventory
def do_quit():
    with open('savefile.dat', 'wb') as f:
        pickle.dump([level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory, character_slot, shop_status], f)

    quit()

# loads stats and inventory
if (Path('savefile.dat').exists()):
    with open('savefile.dat', 'rb') as f:
        level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory, character_slot, shop_status = pickle.load(f)
else:
    #stats for starting game for the first time
    level = 1
    experience = 0
    health = 20
    gold = 160
    attack = 7
    defense = 1
    equiped = ["", "", "", "", ""]
    weapon_inventory = ["Common Level 1 Sword"]
    helmet_inventory = []
    chestpiece_inventory = []
    leggings_inventory = []
    boots_inventory = []
    character_slot = 0
    shop_status = [True, False, False, False, False]

    # creates database on first run
    create_database()
# update max health and character based on saved data
max_health = health
set_character()

############################
#           Main           #
############################

if __name__ == "__main__":

    # make background transparent and always on top
    root.config(highlightbackground='black')
    root.overrideredirect(True)
    root.wm_attributes('-transparentcolor', 'black')
    root['bg'] = 'black'
    root.wm_attributes('-topmost', '1')

    # create character label, tooltip, and right click menu
    character = tk.Label(root, bd=0, bg='black')
    character.pack()

    CreateToolTip(character, text = "Level: " + str(level) + "\nExperience: " + str(experience) + "\nHealth: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold), h = 150, w = -25)

    m = tk.Menu(root, tearoff = 0)
    m.add_command(label="Equipment", command=open_equipment)
    m.add_command(label="Shop", command=open_shop)
    m.add_command(label="Exit", command=do_quit)
    character.bind("<Button-3>", lambda event, menu = m: do_menu(event, menu))

    # create enemy window and label
    enemy_root = tk.Toplevel(root)
    enemy_root.config(highlightbackground='black')
    enemy_root.overrideredirect(True)
    enemy_root.wm_attributes('-transparentcolor', 'black')
    enemy_root['bg'] = 'black'
    enemy_root.wm_attributes('-topmost', '1')

    # area for enemies to spawn
    enemy_root.geometry("+%d+%d" % (x - 800, y))
    enemy_root.geometry('700x500')

    # start animating character
    root.after(1, update, cycle, check, event_number, x)
    # start spawning enemies after certain time
    enemy_root.after(3000, spawn_enemy)

    root.mainloop()