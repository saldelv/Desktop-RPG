import sqlite3

def create_database():
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    # weapons
    weapon_table = "CREATE TABLE weapons (name TEXT, attack INTEGER, value INTEGER)"
    cursor.execute(weapon_table)

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 1 Sword', 1, 1)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 1 Sword', 2, 2)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Sword', 3, 3)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Sword', 4, 4)")
    cursor.execute("INSERT INTO weapons VALUES ('Legendary Level 1 Sword', 5, 5)")

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 2 Sword', 6, 6)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 2 Sword', 7, 7)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 2 Sword', 8, 8)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 2 Sword', 9, 9)")
    cursor.execute("INSERT INTO weapons VALUES ('Legendary Level 2 Sword', 10, 10)")

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 3 Sword', 11, 11)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 3 Sword', 12, 12)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 3 Sword', 13, 13)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 3 Sword', 14, 14)")
    cursor.execute("INSERT INTO weapons VALUES ('Legendary Level 3 Sword', 15, 15)")

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 4 Sword', 16, 16)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 4 Sword', 17, 17)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 4 Sword', 18, 18)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 4 Sword', 19, 19)")
    cursor.execute("INSERT INTO weapons VALUES ('Legendary Level 4 Sword', 20, 20)")

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 5 Sword', 21, 21)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 5 Sword', 22, 22)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 5 Sword', 23, 23)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 5 Sword', 24, 24)")
    cursor.execute("INSERT INTO weapons VALUES ('Legendary Level 5 Sword', 25, 25)")


    # helmets
    helmet_table = "CREATE TABLE helmets (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(helmet_table)

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 1 Helemt', 1, 1)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 1 Helemt', 2, 2)")
    cursor.execute("INSERT INTO helmets VALUES ('Rare Level 1 Helemt', 3, 3)")
    cursor.execute("INSERT INTO helmets VALUES ('Epic Level 1 Helemt', 4, 4)")
    cursor.execute("INSERT INTO helmets VALUES ('Legendary Level 1 Helemt', 5, 5)")

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 2 Helemt', 6, 6)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 2 Helemt', 7, 7)")
    cursor.execute("INSERT INTO helmets VALUES ('Rare Level 2 Helemt', 8, 8)")
    cursor.execute("INSERT INTO helmets VALUES ('Epic Level 2 Helemt', 9, 9)")
    cursor.execute("INSERT INTO helmets VALUES ('Legendary Level 2 Helemt', 10, 10)")

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 3 Helemt', 11, 11)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 3 Helemt', 12, 12)")
    cursor.execute("INSERT INTO helmets VALUES ('Rare Level 3 Helemt', 13, 13)")
    cursor.execute("INSERT INTO helmets VALUES ('Epic Level 3 Helemt', 14, 14)")
    cursor.execute("INSERT INTO helmets VALUES ('Legendary Level 3 Helemt', 15, 15)")

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 4 Helemt', 16, 16)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 4 Helemt', 17, 17)")
    cursor.execute("INSERT INTO helmets VALUES ('Rare Level 4 Helemt', 18, 18)")
    cursor.execute("INSERT INTO helmets VALUES ('Epic Level 4 Helemt', 19, 19)")
    cursor.execute("INSERT INTO helmets VALUES ('Legendary Level 4 Helemt', 20, 20)")

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 5 Helemt', 21, 21)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 5 Helemt', 22, 22)")
    cursor.execute("INSERT INTO helmets VALUES ('Rare Level 5 Helemt', 23, 23)")
    cursor.execute("INSERT INTO helmets VALUES ('Epic Level 5 Helemt', 24, 24)")
    cursor.execute("INSERT INTO helmets VALUES ('Legendary Level 5 Helemt', 25, 25)")

    # chestpieces
    chestpiece_table = "CREATE TABLE chestpieces (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 1 Chestpiece', 1, 1)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 1 Chestpiece', 2, 2)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Rare Level 1 Chestpiece', 3, 3)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Epic Level 1 Chestpiece', 4, 4)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Legendary Level 1 Chestpiece', 5, 5)")

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 2 Chestpiece', 6, 6)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 2 Chestpiece', 7, 7)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Rare Level 2 Chestpiece', 8, 8)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Epic Level 2 Chestpiece', 9, 9)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Legendary Level 2 Chestpiece', 10, 10)")

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 3 Chestpiece', 11, 11)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 3 Chestpiece', 12, 12)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Rare Level 3 Chestpiece', 13, 13)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Epic Level 3 Chestpiece', 14, 14)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Legendary Level 3 Chestpiece', 15, 15)")

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 4 Chestpiece', 16, 16)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 4 Chestpiece', 17, 17)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Rare Level 4 Chestpiece', 18, 18)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Epic Level 4 Chestpiece', 19, 19)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Legendary Level 4 Chestpiece', 20, 20)")

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 5 Chestpiece', 21, 21)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 5 Chestpiece', 22, 22)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Rare Level 5 Chestpiece', 23, 23)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Epic Level 5 Chestpiece', 24, 24)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Legendary Level 5 Chestpiece', 25, 25)")

    # leggings
    chestpiece_table = "CREATE TABLE leggings (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 1 Leggings', 1, 1)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 1 Leggings', 2, 2)")
    cursor.execute("INSERT INTO leggings VALUES ('Rare Level 1 Leggings', 3, 3)")
    cursor.execute("INSERT INTO leggings VALUES ('Epic Level 1 Leggings', 4, 4)")
    cursor.execute("INSERT INTO leggings VALUES ('Legendary Level 1 Leggings', 5, 5)")

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 2 Leggings', 6, 6)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 2 Leggings', 7, 7)")
    cursor.execute("INSERT INTO leggings VALUES ('Rare Level 2 Leggings', 8, 8)")
    cursor.execute("INSERT INTO leggings VALUES ('Epic Level 2 Leggings', 9, 9)")
    cursor.execute("INSERT INTO leggings VALUES ('Legendary Level 2 Leggings', 10, 10)")

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 3 Leggings', 11, 11)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 3 Leggings', 12, 12)")
    cursor.execute("INSERT INTO leggings VALUES ('Rare Level 3 Leggings', 13, 13)")
    cursor.execute("INSERT INTO leggings VALUES ('Epic Level 3 Leggings', 14, 14)")
    cursor.execute("INSERT INTO leggings VALUES ('Legendary Level 3 Leggings', 15, 15)")

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 4 Leggings', 16, 16)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 4 Leggings', 17, 17)")
    cursor.execute("INSERT INTO leggings VALUES ('Rare Level 4 Leggings', 18, 18)")
    cursor.execute("INSERT INTO leggings VALUES ('Epic Level 4 Leggings', 19, 19)")
    cursor.execute("INSERT INTO leggings VALUES ('Legendary Level 4 Leggings', 20, 20)")

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 5 Leggings', 21, 21)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 5 Leggings', 22, 22)")
    cursor.execute("INSERT INTO leggings VALUES ('Rare Level 5 Leggings', 23, 23)")
    cursor.execute("INSERT INTO leggings VALUES ('Epic Level 5 Leggings', 24, 24)")
    cursor.execute("INSERT INTO leggings VALUES ('Legendary Level 5 Leggings', 25, 25)")

    # boots
    chestpiece_table = "CREATE TABLE boots (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO boots VALUES ('Common Level 1 Boots', 1, 1)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 1 Boots', 2, 2)")
    cursor.execute("INSERT INTO boots VALUES ('Rare Level 1 Boots', 3, 3)")
    cursor.execute("INSERT INTO boots VALUES ('Epic Level 1 Boots', 4, 4)")
    cursor.execute("INSERT INTO boots VALUES ('Legendary Level 1 Boots', 5, 5)")

    cursor.execute("INSERT INTO boots VALUES ('Common Level 2 Boots', 6, 6)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 2 Boots', 7, 7)")
    cursor.execute("INSERT INTO boots VALUES ('Rare Level 2 Boots', 8, 8)")
    cursor.execute("INSERT INTO boots VALUES ('Epic Level 2 Boots', 9, 9)")
    cursor.execute("INSERT INTO boots VALUES ('Legendary Level 2 Boots', 10, 10)")

    cursor.execute("INSERT INTO boots VALUES ('Common Level 3 Boots', 11, 11)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 3 Boots', 12, 12)")
    cursor.execute("INSERT INTO boots VALUES ('Rare Level 3 Boots', 13, 13)")
    cursor.execute("INSERT INTO boots VALUES ('Epic Level 3 Boots', 14, 14)")
    cursor.execute("INSERT INTO boots VALUES ('Legendary Level 3 Boots', 15, 15)")

    cursor.execute("INSERT INTO boots VALUES ('Common Level 4 Boots', 16, 16)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 4 Boots', 17, 17)")
    cursor.execute("INSERT INTO boots VALUES ('Rare Level 4 Boots', 18, 18)")
    cursor.execute("INSERT INTO boots VALUES ('Epic Level 4 Boots', 19, 19)")
    cursor.execute("INSERT INTO boots VALUES ('Legendary Level 4 Boots', 20, 20)")

    cursor.execute("INSERT INTO boots VALUES ('Common Level 5 Boots', 21, 21)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 5 Boots', 22, 22)")
    cursor.execute("INSERT INTO boots VALUES ('Rare Level 5 Boots', 23, 23)")
    cursor.execute("INSERT INTO boots VALUES ('Epic Level 5 Boots', 24, 24)")
    cursor.execute("INSERT INTO boots VALUES ('Legendary Level 5 Boots', 25, 25)")

    # enemies
    chestpiece_table = "CREATE TABLE enemies (name TEXT, health INTEGER, attack INTEGER, defense INTEGER, experience INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO enemies VALUES ('Level 1 Slime', 20, 1, 1, 5)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 2 Slime', 30, 5, 3, 5)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 3 Slime', 40, 15, 5, 5)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 4 Slime', 50, 30, 8, 5)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 5 Slime', 60, 40, 10, 5)")

    cursor.execute("INSERT INTO enemies VALUES ('Level 1 Wolf', 20, 8, 3, 10)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 2 Wolf', 30, 15, 8, 10)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 3 Wolf', 40, 25, 12, 10)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 4 Wolf', 50, 35, 15, 10)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 5 Wolf', 60, 50, 20, 10)")

    cursor.execute("INSERT INTO enemies VALUES ('Level 1 Goblin', 20, 10, 5, 15)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 2 Goblin', 30, 20, 10, 15)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 3 Goblin', 40, 30, 15, 15)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 4 Goblin', 50, 50, 20, 15)")
    cursor.execute("INSERT INTO enemies VALUES ('Level 5 Goblin', 60, 70, 30, 15)")

    sqliteConnection.commit()

    cursor.close()
    sqliteConnection.close()

def get_weapon(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, attack, value FROM weapons WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

def get_helmet(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, defense, value FROM helmets WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

def get_chestpiece(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, defense, value FROM chestpieces WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

def get_leggings(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, defense, value FROM leggings WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

def get_boots(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, defense, value FROM boots WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

def get_enemies(name):
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    rows = cursor.execute("SELECT name, health, attack, defense, experience FROM enemies WHERE name = ?", (name,),).fetchall()

    cursor.close()
    sqliteConnection.close()

    return rows

if __name__ == "__main__":
    create_database()
    print(get_weapon("Common Level 1 Sword"))
    print(get_helmet("Legendary Level 1 Helmet"))
    print(get_chestpiece("Rare Level 1 Chestpiece"))
    print(get_leggings("Common Level 1 Leggings"))
    print(get_boots("Common Level 1 Boots"))