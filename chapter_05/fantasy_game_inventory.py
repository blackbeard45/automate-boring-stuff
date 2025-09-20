def display_inventory(inventory):
    total_items = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(f"{v} {k}")
        total_items += v
    print(f"Total number of items: {total_items}")

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)
