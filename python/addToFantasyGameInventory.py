from FantasyGameInventory import display
def addToInventory(inventory, loot):
    for i in loot:
        if i not in inventory:
            inventory[i] =0
        inventory[i] += 1
    return inventory

if __name__ == "__main__":
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = {'gold coin': 42, 'rope':1}
    inventory = addToInventory(inventory,dragonLoot)
    display(inventory)