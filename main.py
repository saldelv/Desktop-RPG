import pyautogui
from pathlib import Path
from database import *
from character import *
from window import *
from enemy import *

if __name__ == "__main__":

    # loads stats and inventory
    if (Path('savefile.dat').exists()):
        with open('savefile.dat', 'rb') as f:
            level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory, character_slot, shop_status = pickle.load(f)
    else:
        #stats for starting game for the first time
        level = 1
        experience = 0
        health = 20
        gold = 0
        attack = 1
        defense = 1
        equiped = ["", "", "", "", ""]
        weapon_inventory = ["Common Level 1 Sword"]
        helmet_inventory = ["Common Level 1 Helmet"]
        chestpiece_inventory = ["Common Level 1 Chestpiece"]
        leggings_inventory = ["Common Level 1 Leggings"]
        boots_inventory = ["Common Level 1 Boots"]
        character_slot = 0
        shop_status = [True, False, False, False, False]

        # creates database on first run
        create_database()

    # create character stats
    character = Character(level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory, character_slot, shop_status)

    # create main window
    window = Window(character)
    window.set_window()
    window.set_label()

    # start enemy spawning
    enemy = Enemy(character, window, window.root, window.x, window.y, window.character_label)
    enemy.set_window()

    window.start()