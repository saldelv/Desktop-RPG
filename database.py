import sqlite3

def create_database():
    sqliteConnection = sqlite3.connect('sql.db')

    cursor = sqliteConnection.cursor()

    # weapons
    weapon_table = "CREATE TABLE weapons (name TEXT, attack INTEGER, value INTEGER)"
    cursor.execute(weapon_table)

    cursor.execute("INSERT INTO weapons VALUES ('Common Level 1 Sword', 5, 5)")
    cursor.execute("INSERT INTO weapons VALUES ('Uncommon Level 1 Sword', 7, 7)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Sword', 9, 9)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Sword', 11, 11)")
    cursor.execute("INSERT INTO weapons VALUES ('Lengendary Level 1 Sword', 13, 13)")


    # helmets
    helmet_table = "CREATE TABLE helmets (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(helmet_table)

    cursor.execute("INSERT INTO helmets VALUES ('Common Level 1 Helmet', 2, 1)")
    cursor.execute("INSERT INTO helmets VALUES ('Uncommon Level 1 Helmet', 3, 2)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Helmet', 4, 3)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Helmet', 5, 4)")
    cursor.execute("INSERT INTO weapons VALUES ('Lengendary Level 1 Helmet', 6, 5)")


    # chestpieces
    chestpiece_table = "CREATE TABLE chestpieces (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO chestpieces VALUES ('Common Level 1 Chestpiece', 4, 3)")
    cursor.execute("INSERT INTO chestpieces VALUES ('Uncommon Level 1 Chestpiece', 5, 5)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Chestpiece', 6, 7)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Chestpiece', 7, 9)")
    cursor.execute("INSERT INTO weapons VALUES ('Lengendary Level 1 Chestpiece', 8, 11)")

    # leggings
    chestpiece_table = "CREATE TABLE leggings (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO leggings VALUES ('Common Level 1 Leggings', 3, 2)")
    cursor.execute("INSERT INTO leggings VALUES ('Uncommon Level 1 Leggings', 4, 3)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Leggings', 5, 4)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Leggings', 6, 5)")
    cursor.execute("INSERT INTO weapons VALUES ('Lengendary Level 1 Leggings', 7, 6)")

    # boots
    chestpiece_table = "CREATE TABLE boots (name TEXT, defense INTEGER, value INTEGER)"
    cursor.execute(chestpiece_table)

    cursor.execute("INSERT INTO boots VALUES ('Common Level 1 Boots', 1, 1)")
    cursor.execute("INSERT INTO boots VALUES ('Uncommon Level 1 Boots', 2, 2)")
    cursor.execute("INSERT INTO weapons VALUES ('Rare Level 1 Boots', 3, 3)")
    cursor.execute("INSERT INTO weapons VALUES ('Epic Level 1 Boots', 4, 4)")
    cursor.execute("INSERT INTO weapons VALUES ('Lengendary Level 1 Boots', 5, 5)")

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

#create_database()
#print(get_weapon("Common Level 1 Sword"))
