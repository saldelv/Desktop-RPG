import tkinter as tk
import base64
import zlib
import tempfile
import os
from character import *
from menus import *

class Shop:
    def __init__(self, root, character, character_root):
        self.root = root
        self.character = character
        self.character_root = character_root

    #open shop window
    def open_shop(self):
        # new window
        sroot = tk.Toplevel(self.root)
        sroot.resizable(0, 0)
        sx = self.root.winfo_x() - 270
        sy = self.root.winfo_y() - 170
        sroot.geometry("+%d+%d" % (sx, sy))
        sroot.wm_attributes('-topmost', '1')

        # transparent icon
        ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
        'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)
        sroot.iconbitmap(default=ICON_PATH)

        #create buttons with each character in folder
        i = 0
        path = 'assets/character'
        for f in os.listdir(path):
            filepath = os.path.join(path, f)
            if not os.path.isdir(filepath):
                b = tk.Button(sroot)
                img = tk.PhotoImage(file = filepath, master=sroot)
                b.configure(image=img, command=lambda i = i: self.change_character(sroot, i))
                b.image = img
                b.grid(row = 0, column = i)

                # check if unlocked
                if self.character.shop_status[i] == True:
                    CreateToolTip(b, text="Unlocked", h = 25, w = 0)
                else:
                    CreateToolTip(b, text="Price: 150 Gold", h = 25, w = 0)

                i += 1

    # change current character
    def change_character(self, sroot, slot):
        # change character if unlocked
        if self.character.shop_status[slot] == True:
            self.character.character_slot = slot
            sroot.destroy()
        # check if character can be purchased and change
        else:
            if self.character.gold >= 150:
                self.character.gold -= 150
                self.character.shop_status[slot] = True
                self.character.character_slot = slot
                UnbindToolTip(self.character_root)
                CreateToolTip(self.character_root, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)
                sroot.destroy()
