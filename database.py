import sqlite3

def create_database():
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    #items
    for i in range(1, 6):
        num = 0
        match i:
            case 1:
                weapon_table = "CREATE TABLE weapons (name TEXT, attack INTEGER, value INTEGER)"
                cursor.execute(weapon_table)
                name = "Sword"
                for j in range(1, 6):
                    for k in range(1, 6):
                        match j:
                            case 1:
                                rarity = "Common"
                            case 2:
                                rarity = "Uncommon"
                            case 3:
                                rarity = "Rare"
                            case 4:
                                rarity = "Epic"
                            case 5:
                                rarity = "Legendary"
                        level = str(k)
                        full = rarity + " Level " + level + " " + name
                        cursor.execute("INSERT INTO weapons VALUES (?, ?, ?)",(full, k, k))
                        num += 5
                    num -= 19
            case 2:
                helmet_table = "CREATE TABLE helmets (name TEXT, defense INTEGER, value INTEGER)"
                cursor.execute(helmet_table)
                name = "Helmet"
                for j in range(1, 6):
                    for k in range(1, 6):
                        match j:
                            case 1:
                                rarity = "Common"
                            case 2:
                                rarity = "Uncommon"
                            case 3:
                                rarity = "Rare"
                            case 4:
                                rarity = "Epic"
                            case 5:
                                rarity = "Legendary"
                        level = str(k)
                        full = rarity + " Level " + level + " " + name
                        cursor.execute("INSERT INTO helmets VALUES (?, ?, ?)",(full, k, k))
                        num += 5
                    num -= 19
            case 3:
                chestpiece_table = "CREATE TABLE chestpieces (name TEXT, defense INTEGER, value INTEGER)"
                cursor.execute(chestpiece_table)
                name = "Chestpiece"
                for j in range(1, 6):
                    for k in range(1, 6):
                        match j:
                            case 1:
                                rarity = "Common"
                            case 2:
                                rarity = "Uncommon"
                            case 3:
                                rarity = "Rare"
                            case 4:
                                rarity = "Epic"
                            case 5:
                                rarity = "Legendary"
                        level = str(k)
                        full = rarity + " Level " + level + " " + name
                        cursor.execute("INSERT INTO chestpieces VALUES (?, ?, ?)",(full, k, k))
                        num += 5
                    num -= 19
            case 4:
                leggings_table = "CREATE TABLE leggings (name TEXT, defense INTEGER, value INTEGER)"
                cursor.execute(leggings_table)
                name = "Leggings"
                for j in range(1, 6):
                    for k in range(1, 6):
                        match j:
                            case 1:
                                rarity = "Common"
                            case 2:
                                rarity = "Uncommon"
                            case 3:
                                rarity = "Rare"
                            case 4:
                                rarity = "Epic"
                            case 5:
                                rarity = "Legendary"
                        level = str(k)
                        full = rarity + " Level " + level + " " + name
                        cursor.execute("INSERT INTO leggings VALUES (?, ?, ?)",(full, k, k))
                        num += 5
                    num -= 19
            case 5:
                boots_table = "CREATE TABLE boots (name TEXT, defense INTEGER, value INTEGER)"
                cursor.execute(boots_table)
                name = "Boots"
                for j in range(1, 6):
                    for k in range(1, 6):
                        match j:
                            case 1:
                                rarity = "Common"
                            case 2:
                                rarity = "Uncommon"
                            case 3:
                                rarity = "Rare"
                            case 4:
                                rarity = "Epic"
                            case 5:
                                rarity = "Legendary"
                        level = str(k)
                        full = rarity + " Level " + level + " " + name
                        cursor.execute("INSERT INTO boots VALUES (?, ?, ?)",(full, k, k))
                        num += 5
                    num -= 19

    # enemies
    enemy_table = "CREATE TABLE enemies (name TEXT, health INTEGER, attack INTEGER, defense INTEGER, experience INTEGER)"
    cursor.execute(enemy_table)

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