import tkinter as tk
import base64
import zlib
import tempfile
from database import *
from character import *
from menus import *

class Inventory:
    def __init__(self, root, character, character_label):
        self.root = root
        self.character = character
        self.character_label = character_label

    # open equipment menu
    def open_equipment(self):
        # create window
        eroot = tk.Toplevel(self.root)
        eroot.resizable(0, 0)
        ex = self.root.winfo_x() - 125
        ey = self.root.winfo_y() - 200
        eroot.geometry("+%d+%d" % (ex, ey))
        eroot.wm_attributes('-topmost', '1')
        
        # get equipped data
        weapon = self.get_equipped(0, eroot)
        headgear = self.get_equipped(1, eroot)
        chestpiece = self.get_equipped(2, eroot)
        leggings = self.get_equipped(3, eroot)
        boots = self.get_equipped(4, eroot)

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
    def get_equipped(self, slot, eroot):
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
        button = tk.Button(eroot, command=lambda: self.open_inventory(slot, eroot))
        if self.character.equiped[slot] != "":
            img = tk.PhotoImage(file = 'assets/items/' + self.character.equiped[slot] + '.png', master=eroot)
            rows = func(self.character.equiped[slot])
            for row in rows:
                if slot == 0:
                    stat = "Attack: "
                else:
                    stat = "Defense: "
                CreateToolTip(button, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]), h = 75, w = -75)

            em = tk.Menu(self.root, tearoff = 0)
            em.add_command(label="Unequip", command=lambda: self.remove_equip(slot, eroot))
            em.add_command(label="Sell", command=lambda: self.sell_equip(slot, -1, [], eroot))
            button.bind("<Button-3>", lambda event, menu = em: do_menu(event, menu))
        else:
            img = tk.PhotoImage(file = 'assets/items/' + empty, master=eroot)
            CreateToolTip(button, text=item, h = 25, w = 0)
        button.configure(image=img)
        button.image = img
        
        return button

    # open inventory for equipping in a specific slot
    def open_inventory(self, slot, eroot):
        # getting correct slot info
        match slot:
            case 0:
                inv = self.character.weapon_inventory
                func = get_weapon
            case 1:
                inv = self.character.helmet_inventory
                func = get_helmet
            case 2:
                inv = self.character.chestpiece_inventory
                func = get_chestpiece
            case 3:
                inv = self.character.leggings_inventory
                func = get_leggings
            case 4:
                inv = self.character.boots_inventory
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
                    img = tk.PhotoImage(file = "assets/items/" + inv[index] + ".png", master=iroot)
                    current = index
                    b.configure(image=img, command=lambda: self.new_equip(slot, current, iroot, eroot))
                    b.image = img

                    rows = func(inv[index])
                    for row in rows:
                        if slot == 0:
                            stat = "Attack: "
                        else:
                            stat = "Defense: "
                        CreateToolTip(b, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]), h = 75, w = -75)
                    
                    im = tk.Menu(self.root, tearoff = 0)
                    im.add_command(label="Sell", command=lambda: self.sell_equip(slot, current, inv, iroot))
                    b.bind("<Button-3>", lambda event, menu = im: do_menu(event, menu))

                    index += 1
                else:
                    img = tk.PhotoImage(file = "assets/items/empty.png", master=iroot)
                    b.configure(image=img)
                    b.image=img

                b.grid(row=i, column=j)

    # equipping new item
    def new_equip(self, slot, current, iroot, eroot):

        # getting correct slot info
        match slot:
            case 0:
                inv = self.character.weapon_inventory
                func = get_weapon
            case 1:
                inv = self.character.helmet_inventory
                func = get_helmet
            case 2:
                inv = self.character.chestpiece_inventory
                func = get_chestpiece
            case 3:
                inv = self.character.leggings_inventory
                func = get_leggings
            case 4:
                inv = self.character.boots_inventory
                func = get_boots
        
        # move item to equipped if empty and chage stats
        if not self.character.equiped[slot]:
            self.character.equiped[slot] = inv[current]
            inv.remove(inv[current])

            rows = func(self.character.equiped[slot])
            for row in rows:
                if slot > 0:
                    self.character.defense += row[1]
                else:
                    self.character.attack += row[1]

        # swap item with equipped if not empty and change stats
        else:
            rows = func(self.character.equiped[slot])
            for row in rows:
                if slot > 0:
                    self.character.defense -= row[1]
                else:
                    self.character.attack -= row[1]
            
            temp = self.character.equiped[slot]
            self.character.equiped[slot] = inv[current]
            inv[current] = temp

            rows = func(self.character.equiped[slot])
            for row in rows:
                if slot > 0:
                    self.character.defense += row[1]
                else:
                    self.character.attack += row[1]
        
        # reload windows and tooltip
        UnbindToolTip(self.character_label)
        CreateToolTip(self.character_label, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)

        iroot.destroy()
        eroot.destroy()
        self.open_equipment()

    # unequip item
    def remove_equip(self, slot, eroot):

        # get correct slot info
        match slot:
            case 0:
                inv = self.character.weapon_inventory
                func = get_weapon
            case 1:
                inv = self.character.helmet_inventory
                func = get_helmet
            case 2:
                inv = self.character.chestpiece_inventory
                func = get_chestpiece
            case 3:
                inv = self.character.leggings_inventory
                func = get_leggings
            case 4:
                inv = self.character.boots_inventory
                func = get_boots

        # move item to inventory and change stats
        inv.append(self.character.equiped[slot])

        rows = func(self.character.equiped[slot])
        for row in rows:
            if slot > 0:
                self.character.defense -= row[1]
            else:
                self.character.attack -= row[1]
        
        self.character.equiped[slot] = ""

        # reload window and tooltip
        UnbindToolTip(self.character_label)
        CreateToolTip(self.character_label, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)

        eroot.destroy()
        self.open_equipment()

    # sell item
    def sell_equip(self, slot, current, inv, a_root):
        
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
            rows = func(self.character.equiped[slot])
            for row in rows:
                self.character.gold += row[2]
                if slot > 0:
                    self.character.defense -= row[1]
                else:
                    self.character.attack -= row[1]
            
            self.character.equiped[slot] = ""

            a_root.destroy()
            self.open_equipment()

        # remove from inventory and add gold if not equipped
        else:
            rows = func(inv[current])
            for row in rows:
                self.character.gold += row[2]

            inv.remove(inv[current])
            a_root.destroy()

        # reload windows and tooltip
        UnbindToolTip(self.character_label)
        CreateToolTip(self.character_label, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)
