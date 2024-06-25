import pickle

class Character:
    def __init__(self, level, experience, health, gold, attack, defense, equiped, weapon_inventory, helmet_inventory, chestpiece_inventory, leggings_inventory, boots_inventory, character_slot, shop_status):
        self.level = level
        self.experience = experience
        self.health = health
        self.max_health =health
        self.gold = gold
        self.attack = attack
        self.defense = defense
        self.equiped = equiped
        self.weapon_inventory = weapon_inventory
        self.helmet_inventory = helmet_inventory
        self.chestpiece_inventory = chestpiece_inventory
        self.leggings_inventory = leggings_inventory
        self.boots_inventory = boots_inventory
        self.character_slot = character_slot
        self.shop_status = shop_status

    # saves stats and inventory
    def save(self):
        with open('savefile.dat', 'wb') as f:
            pickle.dump([self.level, self.experience, self.health, self.gold, self.attack, self.defense, self.equiped, self.weapon_inventory, self.helmet_inventory, self.chestpiece_inventory, self.leggings_inventory, self.boots_inventory, self.character_slot, self.shop_status], f)