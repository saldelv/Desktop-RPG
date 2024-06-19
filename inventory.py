import base64
import zlib
import tempfile
from main import *

def open_equipment():
    eroot = tk.Toplevel(root)
    eroot.resizable(0, 0)
    ex = root.winfo_x() - 125
    ey = root.winfo_y() - 200
    eroot.geometry("+%d+%d" % (ex, ey))
    eroot.wm_attributes('-topmost', '1')
    
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

    button = tk.Button(eroot, command=lambda: open_inventory(slot, eroot))
    if equiped[slot] != "":
        img = tk.PhotoImage(file = 'assets/items/' + equiped[slot] + '.png', master=eroot)
        rows = func(equiped[slot])
        for row in rows:
            if slot == 0:
                stat = "Attack: "
            else:
                stat = "Defense: "
            CreateToolTip(button, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]))

        em = tk.Menu(root, tearoff = 0)
        em.add_command(label="Unequip", command=lambda: remove_equip(slot, eroot))
        em.add_command(label="Sell", command=lambda: sell_equip(slot, -1, [], eroot))
        button.bind("<Button-3>", lambda event, menu = em: do_menu(event, menu))
    else:
        img = tk.PhotoImage(file = 'assets/items/' + empty, master=eroot)
        CreateToolTip(button, text=item)
    button.configure(image=img)
    button.image = img
    
    return button


def open_inventory(slot, eroot):
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
    
    iroot = tk.Toplevel(eroot)
    iroot.resizable(0, 0)
    ix = eroot.winfo_x() - 170
    iy = eroot.winfo_y() - 70
    iroot.geometry("+%d+%d" % (ix, iy))
    iroot.wm_attributes('-topmost', '1')

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
                        CreateToolTip(b, text = str(row[0]) + "\n" + stat + str(row[1]) + "\nValue: " + str(row[2]))
                    
                    im = tk.Menu(root, tearoff = 0)
                    im.add_command(label="Sell", command=lambda: sell_equip(slot, current, inv, iroot))
                    b.bind("<Button-3>", lambda event, menu = im: do_menu(event, menu))

                index += 1
            else:
                img = tk.PhotoImage(file = "assets/items/empty.png", master=iroot)
                b.configure(image=img)
                b.image=img

            b.grid(row=i, column=j)

def new_equip(slot, current, iroot, eroot):
    global attack
    global defense

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
    
    if not equiped[slot]:
        equiped[slot] = inv[current]
        inv.remove(inv[current])

        rows = func(equiped[slot])
        for row in rows:
            if slot > 0:
                defense += row[1]
            else:
                attack += row[1]

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
    
    UnbindToolTip(character)
    CreateToolTip(character, text = "Health: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold))

    iroot.destroy()
    eroot.destroy()
    open_equipment()

def remove_equip(slot, eroot):
    global attack
    global defense

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

    inv.append(equiped[slot])

    rows = func(equiped[slot])
    for row in rows:
        if slot > 0:
            defense -= row[1]
        else:
            attack -= row[1]
    
    equiped[slot] = ""

    UnbindToolTip(character)
    CreateToolTip(character, text = "Health: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold))

    eroot.destroy()
    open_equipment()

def sell_equip(slot, current, inv, a_root):
    global gold
    global attack
    global defense
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

    else:
        rows = func(inv[current])
        for row in rows:
            gold += row[2]

        inv.remove(inv[current])
        a_root.destroy()

    UnbindToolTip(character)
    CreateToolTip(character, text = "Health: " + str(health) + "\nAttack: " + str(attack) + "\nDefense: " + str(defense) + "\nGold: " + str(gold))