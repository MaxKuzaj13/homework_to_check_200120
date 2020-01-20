from tabulate import tabulate

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    inv_keys= list(inventory.keys())
    inv_val=list(inventory.values())

    for i in range(len(inv_keys)):
        print(str(inv_keys[i]) + ' : ' + str(inv_val[i]))

display_inventory(inventory)
print(""" 
After dragon:

""")


def add_to_inventory(inventory, dragon_loot):
    inv_keys= list(inventory.keys())
    inv_val=list(inventory.values())
    temp = 0

    for i in range(len(dragon_loot)):
        for inv in range(len(inv_keys)):
            if dragon_loot[i] in inv_keys and inv_keys[inv] == dragon_loot[i]:
                #temp = inv_val[inv]
                inventory[dragon_loot[i]] = inv_val[inv] + 1
                inv_val[inv] +=1

            elif dragon_loot[i] in inv_keys and inv_keys != dragon_loot[i]:
                pass
            else:
                inventory[dragon_loot[i]] = 1

def print_table(inventory, order):
    inv_keys= list(inventory.keys())
    inv_val=list(inventory.values())
    list_invent=[]

    for i in range(len(inv_keys)):
        list_invent.append([str(inv_keys[i]), str(inv_val[i])])

    if order == 'count,desc':
        list_invent.sort(reverse = True, key = lambda count: int(count[1]))
    elif order == 'count,asc':
        list_invent.sort( key = lambda count: int(count[1]))
    else:
        list_invent.sort()
    #print(list_invent)
    print('-------------------------')
    print(tabulate(list_invent, headers=["item name","count"], tablefmt="github"))
    print('-------------------------')
    
def import_inventory(inventory, filename):
    with open(filename, 'r') as file: # Use file to refer to the file object
        data = file.read()
        add_to_item=data.split(',')
        file.close()
        add_to_inventory(inventory, dragon_loot = add_to_item)


def export_inventory(inventory):
    string_inventory = ''
    with open('export_inventory.csv', 'w') as file: # Use file to refer to the file object
        for inv, number in inventory.items():
            string_inventory += (inv + ',') * number
        file.write(string_inventory[:-3])


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, dragon_loot)

display_inventory(inventory)
print_table(inventory, order = 'Null')

import_inventory(inventory, filename = "import_inventory.csv")

display_inventory(inventory)
print_table(inventory, order = 'count,desc')

export_inventory(inventory)
