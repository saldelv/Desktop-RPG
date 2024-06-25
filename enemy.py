import tkinter as tk
import random
from menus import *
from database import *

class Enemy:
    def __init__(self, character, window, root, x, y, character_label):
        self.character = character
        self.window = window
        self.root = root
        self.enemy_root = tk.Toplevel(root)
        self.x = x
        self.y = y
        self.character_label = character_label

    # saves stats and inventory
    def set_window(self):
        # create enemy window and label
        self.enemy_root.config(highlightbackground='black')
        self.enemy_root.overrideredirect(True)
        self.enemy_root.wm_attributes('-transparentcolor', 'black')
        self.enemy_root['bg'] = 'black'
        self.enemy_root.wm_attributes('-topmost', '1')

        # area for enemies to spawn
        self.enemy_root.geometry("+%d+%d" % (self.x - 800, self.y))
        self.enemy_root.geometry('700x500')

        # start spawning enemies after certain time
        self.enemy_root.after(3000, self.spawn_enemy)

    # spawn enemy after certain time
    def spawn_enemy(self):

        # creating random enemy in random location
        enemy = tk.Label(self.enemy_root, bd=0, bg='black')

        enemy.place(x = random.randrange(0, 400), y = -50)

        type = random.randrange(0, 3)
        match type:
                case 0:
                    name = 'Slime'
                case 1:
                    name = 'Wolf'
                case 2:
                    name = 'Goblin'

        self.root.after(1, self.play_enemy(enemy, 0, name))

        # click on enemy to start battle
        enemy.bind("<Button-1>", lambda event: self.start_battle(enemy))

        # get and assign enemy stats
        enemy.health = 0
        enemy.max_health = 0
        enemy.attack = 0
        enemy.defense = 0
        enemy.experience = 0

        rows = get_enemies('Level ' + str(self.character.level) + " " + name)
        for row in rows:
            enemy.health = row[1]
            enemy.max_health = row[1]
            enemy.attack = row[2]
            enemy.defense = row[3]
            enemy.experience = row[4]

        CreateToolTip(enemy, text = "Level " + str(self.character.level) + " " + name + "\nHealth: " + str(enemy.health), h = 0, w = 50)

        # spawn next enemy and despawn current enemy after certain times
        self.root.after(60000, lambda: self.despawn_enemy(enemy))
        self.root.after(30000, self.spawn_enemy)

    # unload enemy
    def despawn_enemy(self, enemy):
        enemy.destroy()

    # play enemy gif
    def play_enemy(self, enemy, current_frame, name):
        img = [tk.PhotoImage(file='assets/enemies/' + name + '.gif', format = 'gif -index %i' %(i)) for i in range(6)]
        frame = img[current_frame]
        enemy.configure(image = frame)
        enemy.image = frame
        current_frame = current_frame + 1
        if current_frame == len(img):
            current_frame = 0
        # get rid of enemy if defeated in battle
        if not self.window.won:
            self.root.after(200, lambda: self.play_enemy(enemy, current_frame, name))
        else:
            self.despawn_enemy(enemy)
            self.window.won = False

    # start battle
    def start_battle(self, enemy):
        # set battle variable and calculate distance to enemy
        if not self.window.in_battle:
            self.window.in_battle = True
            self.window.battle_distance = (self.x - 1850) + (300-enemy.winfo_x())
        
        # create health labels and start fighting if moved to enemy
        if self.window.battle_moved >= self.window.battle_distance:
            enemy_health = tk.Label(self.enemy_root, text = "Enemy:\n" + str(enemy.health) + "/" + str(enemy.max_health))
            enemy_health.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
            player_health = tk.Label(self.enemy_root, text = "Player:\n" + str(self.character.health) + "/" + str(self.character.max_health))
            player_health.place(x = enemy.winfo_x() + 260, y = enemy.winfo_y() + 50)
            self.root.after(400, lambda: self.update_battle(enemy, enemy_health, player_health))
        # keep moving until reached enemy
        else:
            self.root.after(100, lambda: self.start_battle(enemy))

    # fighting
    def update_battle(self, enemy, enemy_health, player_health):
        # update healths based on stats
        enemy.health -= max(self.character.attack - (enemy.defense * 0.5), 0)
        self.character.health -= max(enemy.attack - (self.character.defense * 0.5), 0)
        enemy_health.configure(text = "Enemy:\n" + str(max(enemy.health, 0)) + "/" + str(enemy.max_health))
        player_health.configure(text = "Player:\n" + str(max(self.character.health, 0)) + "/" + str(self.character.max_health))

        # players wins battle
        if enemy.health <= 0:
            print("win")
            # gain experience and level up
            self.character.experience += enemy.experience
            if self.character.experience >= 100 and self.character.level < 5:
                self.character.level = self.character.level + 1
                self.character.experience = self.character.experience - 100
                self.character.max_health += 20
            self.character.health = self.character.max_health

            UnbindToolTip(self.character_label)
            CreateToolTip(self.character_label, text = "Level: " + str(self.character.level) + "\nExperience: " + str(self.character.experience) + "\nHealth: " + str(self.character.health) + "\nAttack: " + str(self.character.attack) + "\nDefense: " + str(self.character.defense) + "\nGold: " + str(self.character.gold), h = 150, w = -25)
            
            # set variables to end battle and move back
            self.window.won = True
            self.window.in_battle = False
            self.window.finished_battle = True
            self.window.battle_distance = 0
            self.window.battle_moved = 0
            player_health.destroy()
            enemy_health.destroy()

            # random drop slot
            match random.randrange(0, 5):
                case 0:
                    inv = self.character.weapon_inventory
                    name = "Sword"
                case 1:
                    inv = self.character.helmet_inventory
                    name = "Helmet"
                case 2:
                    inv = self.character.chestpiece_inventory
                    name = "Chestpiece"
                case 3:
                    inv = self.character.leggings_inventory
                    name = "Leggings"
                case 4:
                    inv = self.character.boots_inventory
                    name = "Boots"

            # random drop rarity
            chance = random.randrange(0, 100)
            if (chance > 95):
                drop = "Legendary Level " + str(self.character.level) + " " + name
            elif (chance > 85):
                drop = "Epic Level " + str(self.character.level) + " " + name
            elif (chance > 70):
                drop = "Rare Level " + str(self.character.level) + " " + name
            elif (chance > 50):
                drop = "Uncommon Level " + str(self.character.level) + " " + name
            elif (chance > 20):
                drop = "Common Level " + str(self.character.level) + " " + name
            else:
                drop = ""
            
            # give drop to player and show label
            print(drop)
            text = tk.Label(self.enemy_root, text = "Win!")
            if drop != "" and len(inv) < 25:
                inv.append(drop)
                text.configure(text = "Win! \nObtained " + drop)
            text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
            self.root.after(3000, lambda: destroy_text(text))

        # player loses battle
        elif self.character.health <= 0:
            # set variables to end battle and move back
            print("lose")
            self.character.health = self.character.max_health
            enemy.health = enemy.max_health
            self.window.in_battle = False
            self.window.finished_battle = True
            self.window.battle_distance = 0
            self.window.battle_moved = 0
            player_health.destroy()
            enemy_health.destroy()
            text = tk.Label(self.enemy_root, text = "Lose...")
            text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
            self.root.after(3000, lambda: destroy_text(text))

        # battle ties if no damage is done
        elif self.character.health == self.character.max_health and enemy.health == enemy.max_health:
            # set variables to end battle and move back
            print("draw")
            self.window.in_battle = False
            self.window.finished_battle = True
            self.window.battle_distance = 0
            self.window.battle_moved = 0
            player_health.destroy()
            enemy_health.destroy()
            text = tk.Label(self.enemy_root, text = "Draw")
            text.place(x = enemy.winfo_x(), y = enemy.winfo_y() + 50)
            self.root.after(3000, lambda: destroy_text(text))

        # next turn of attacking
        else:
            print("next turn")
            self.root.after(1000, lambda: self.update_battle(enemy, enemy_health, player_health))

        # destroys drop text after certain time
        def destroy_text(drop_text):
            drop_text.destroy()