'''
Homework 3, Exercise 3
Kyle Bush
9/21/2020
This program stores a store inventory in a dictionary.
The user can add items, delete items, and print the inventory.
'''

def printInventory(inventory):
    print()
    print('Item'.ljust(20), 'Quantity'.ljust(8))
    for item, number in inventory.items():
        print(item.ljust(20), str(number).ljust(8))
    print()

def addItem(inventory, item):
    inventory.setdefault(item, 0)
    inventory[item] += 1
    print('Item added: ' + item + ', Quanity in Inventory: ' + str(inventory[item]))

def deleteItem(inventory, item):
    if item in inventory and inventory[item] >= 0:
        inventory[item] -= 1
        print('Item added: ' + item + ', Quanity in Inventory: ' + str(inventory[item]))
    else:
        print(item + ' is not in inventory.')

def main():
    inventory = {
        'Hand sanitizer': 10,
        'Soap': 6,
        'Kleenex': 11,
        'Lotion': 16,
        'Razors': 12
    }

    while True:
        print('MENU')
        print('1. Add Item')
        print('2. Delete Item')
        print('3. Print Inventory')
        print('4. Exit')
        menuSelection = input()

        if menuSelection == '1':
            print('Enter an item to add to the inventory.')
            item = input()
            addItem(inventory, item)
        elif menuSelection == '2':
            print('Enter an item to delete from the inventory.')
            item = input()
            deleteItem(inventory, item)
        elif menuSelection == '3':
            printInventory(inventory)
        elif menuSelection == '4':
            break
        else:
            print('Please enter a valid menu option.')

if __name__ == "__main__":
    main()
