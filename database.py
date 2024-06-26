import sqlite3
import sqlalchemy

def create_database():

    #items
    engine = sqlalchemy.create_engine('sqlite:///sql.db')
    meta = sqlalchemy.MetaData()

    for i in range(5):
        num = 1

        match i:
            case 0:
                table_name = 'weapons'
                name = "Sword"
                stat = 'attack'
            case 1:
                table_name = 'helmets'
                name = "Helmet"
                stat = 'defense'
            case 2:
                table_name = 'chestpieces'
                name = "Chestpiece"
                stat = 'defense'
            case 3:
                table_name = 'leggings'
                name = "Leggings"
                stat = 'defense'
            case 4:
                table_name = 'boots'
                name = "Boots"
                stat = 'defense'

        table = sqlalchemy.Table(
            table_name, meta,
            sqlalchemy.Column('name', sqlalchemy.String),
            sqlalchemy.Column(stat, sqlalchemy.Integer),
            sqlalchemy.Column('value', sqlalchemy.Integer),
        )

        meta.create_all(engine)

        for j in range(5):
            for k in range(5):
                match j:
                    case 0:
                        rarity = "Common"
                    case 1:
                        rarity = "Uncommon"
                    case 2:
                        rarity = "Rare"
                    case 3:
                        rarity = "Epic"
                    case 4:
                        rarity = "Legendary"
                level = str(k + 1)
                full = rarity + " Level " + level + " " + name

                if i == 0:
                    ins = table.insert().values(name = full, attack = num, value = num)
                else:
                    ins = table.insert().values(name = full, defense = num, value = num)
                conn = engine.connect()
                conn.execute(ins)
                conn.commit()
                
                num += 5
            num -= 24
    
    # enemies
    enemies = sqlalchemy.Table(
            'enemies', meta,
            sqlalchemy.Column('name', sqlalchemy.String),
            sqlalchemy.Column('health', sqlalchemy.Integer),
            sqlalchemy.Column('attack', sqlalchemy.Integer),
            sqlalchemy.Column('defense', sqlalchemy.Integer),
            sqlalchemy.Column('experience', sqlalchemy.Integer),
        )
    
    meta.create_all(engine)

    
    conn = engine.connect()
    conn.execute(enemies.insert(), [
        {'name':'Level 1 Slime', 'health':20, 'attack':1, 'defense':1, 'experience':5},
        {'name':'Level 2 Slime', 'health':30, 'attack':5, 'defense':3, 'experience':5},
        {'name':'Level 3 Slime', 'health':40, 'attack':15, 'defense':5, 'experience':5},
        {'name':'Level 4 Slime', 'health':50, 'attack':30, 'defense':8, 'experience':5},
        {'name':'Level 5 Slime', 'health':60, 'attack':40, 'defense':10, 'experience':5},

        {'name':'Level 1 Wolf', 'health':20, 'attack':8, 'defense':3, 'experience':10},
        {'name':'Level 2 Wolf', 'health':30, 'attack':15, 'defense':8, 'experience':10},
        {'name':'Level 3 Wolf', 'health':40, 'attack':25, 'defense':12, 'experience':10},
        {'name':'Level 4 Wolf', 'health':50, 'attack':35, 'defense':15, 'experience':10},
        {'name':'Level 5 Wolf', 'health':60, 'attack':50, 'defense':20, 'experience':10},

        {'name':'Level 1 Goblin', 'health':20, 'attack':10, 'defense':5, 'experience':15},
        {'name':'Level 2 Goblin', 'health':30, 'attack':20, 'defense':10, 'experience':15},
        {'name':'Level 3 Goblin', 'health':40, 'attack':30, 'defense':15, 'experience':15},
        {'name':'Level 4 Goblin', 'health':50, 'attack':50, 'defense':20, 'experience':15},
        {'name':'Level 5 Goblin', 'health':60, 'attack':70, 'defense':30, 'experience':15},
    ])
    
    conn.commit()

def get_query(table_name, name):
    engine = sqlalchemy.create_engine('sqlite:///sql.db')
    meta = sqlalchemy.MetaData()
    sqlalchemy.MetaData.reflect(meta, bind=engine)
    table = meta.tables[table_name]
    query = table.select()
    query = query.where(table.c.name == name)
    with engine.connect() as conn:
        result = conn.execute(query)
    return result


if __name__ == "__main__":
    #create_database()
    get_query("weapons", "Common Level 1 Sword")
    get_query("helmets", "Legendary Level 1 Helmet")
    get_query("enemies", "Level 1 Slime")