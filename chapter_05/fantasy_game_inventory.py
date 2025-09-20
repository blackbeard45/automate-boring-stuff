def display_inventory(inventory):
    total_items = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(f"{v} {k}")
        total_items += v
    print(f"Total number of items: {total_items}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
            
dragons_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

add_to_inventory(inventory, dragons_loot)
display_inventory(inventory)
