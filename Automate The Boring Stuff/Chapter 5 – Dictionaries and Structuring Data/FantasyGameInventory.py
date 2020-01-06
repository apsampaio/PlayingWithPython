playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(dict):
    total = 0
    keys = list(dict.keys())
    for itens in range(len(keys)):
        print(f'{dict.get(keys[itens])} {keys[itens]}')
        total += dict.get(keys[itens])
    print(f'Total number of items: {total}')


def add_to_inventory(inventory:dict, loot:list):
    itensToAdd = []
    for itens in loot:
        if itens not in itensToAdd:
            itensToAdd.append(itens)
    for iten in itensToAdd:
        if inventory.get(iten, False):
           inventory[iten] += loot.count(iten) 
        else:
            inventory[iten] = loot.count(iten)
    return inventory


print(add_to_inventory(playerInventory, dragonLoot))
display_inventory(playerInventory)