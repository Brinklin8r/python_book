#! python3
# inventory.py
# RPG inventory script
from pathlib import Path
import pprint
import sys
import importlib

### Functions:
def displayItem(item, colWidths):
    print(item['name'].ljust(colWidths[0]),                                 \
          str(item['count']).rjust(colWidths[1]),                           \
          "{:.2f}".format(item['weight']).rjust(colWidths[2]),              \
          "${:.2f}".format(item['price']).rjust(colWidths[3]),              \
          sep=' | ', end= ' |\n')

def displayInventory(inventory):
    itemsWeight = 0.0
    itemsPrice = 0.00
    itemsCount = 0
    colWidths = [0] * len(inventory[0])         # List for Number of Columns
    totalWidth = 0

    for item in inventory:                      # Calculate column widths
        if colWidths[0]  < len(item['name']):
            colWidths[0] = len(item['name'])
        if colWidths[1]  < len(str(item['count'])):
            colWidths[1] = len(str(item['count']))
        if colWidths[2]  < len(str(item['weight'])):
            colWidths[2] = len(str(item['weight']))
        if colWidths[3]  < len(str(item['price'])) + 2:
            colWidths[3] = len(str(item['price'])) + 2
    
    for length in colWidths:                    # Calculate Width of Inventory Report
        totalWidth += length + 3                # Adjust for spacer character " | "
    totalWidth -= 1                             # Adjust for last character being " |"
    
    # Inventory Report Header
    print('-' * totalWidth)
    print('Item Name'.center(colWidths[0]), 'Count'.center(colWidths[1]),   \
          'Weight'.center(colWidths[2]),    'Price'.center(colWidths[3]),   \
          sep=' | ', end= ' |\n')
    print('-' * colWidths[0], '-' * colWidths[1],                           \
          '-' * colWidths[2], '-' * colWidths[3],                           \
          sep='-+-', end= '-|\n')

    # Inventory Report Item(s)
    for itemNum in range(1, len(inventory)):
        displayItem(inventory[itemNum], colWidths)
        itemsWeight += inventory[itemNum]['weight'] * inventory[itemNum]['count']
        itemsPrice  += inventory[itemNum]['price']  * inventory[itemNum]['count']
        itemsCount  += inventory[itemNum]['count']

    # Inventory Report Footer
    print('=' * totalWidth)
    print('Total Items:'.ljust(13),  str(itemsCount).rjust(10))
    print('Total Weight:'.ljust(13), "{:.2f}".format(itemsWeight).rjust(10))
    print('Total Value:'.ljust(13),  "${:.2f}".format(itemsPrice).rjust(10))

def saveInventory(inventory, saveFileName):
    saveFile = open(saveFileName, 'w')
    saveFile.write('inventory = ' + pprint.pformat(inventory) + '\n')
    saveFile.close()
    print(f'Inventory saved to {saveFileName}.')

def addItem(inventory, addItem):
    found = False
    for item in inventory:                      # Check if there is already an item by this name in inventory
        if addItem['name'] == item['name']:     # Increment count if found
            item['count'] += addItem['count']
            print(f"Found item {addItem['name']}, incremented count to {item['count']}.")
            found = True
            break
    if not found:                               # Add item if not already in inventory
        inventory.append(addItem)
        print(f"Added item {addItem['name']} to inventory.")

def removeItem(inventory, removeItem):
    found = False
    for item in inventory:                      # Check if there is an item by this name in inventory
        if removeItem['name'] == item['name']:  # Decrement count if found, and there are enough
            if item['count'] > removeItem['count']:
                item['count'] -= removeItem['count']
                print(f"Found item {removeItem['name']}, decremented count to {item['count']}.")
            elif item['count'] == removeItem['count']:
                inventory.remove(item)          # Remove item from bag if remove count is inventory count
                print(f"Found item {removeItem['name']}, removed all from inventory.")
            else:
                print(f"Found item {removeItem['name']}, but unable to decrement count as there are only {item['count']} in inventory.")
            found = True
            break
    if not found:                               # Item is not in inventory
        print(f"Item {removeItem['name']} not found in inventory.")

def updateItem(inventory, item):
    print('Update Item')

def getItem(forAddRemoveUpdate = ''):
    item = {'name'  : '', 
            'count' : 0, 
            'weight': 0.0, 
            'price' : 0.00}

    # Get Name from User
    # Find Item 

    return item

### Variables:
bag = []
saveFile = 'inventorySave.py'

### Main:
if Path(saveFile).is_file():                    # Load Saved Inventory
    savedInventory = importlib.import_module(Path(saveFile).stem)
    print(f'Reading Inventory from {saveFile}.')
    bag = savedInventory.inventory

if len(bag) == 0:
    # Initialize Inventory and Create Header Row if inventory is empty
    bag = [{'name'  : 'Item Name', 
            'count' : 'Count', 
            'weight': 'Weight', 
            'price' : 'Price'}]

while True:                                     # Main program
    # Switchboard
    while True:                                 # Get valid user input
        print(' RPG Inventory System '.center(38, '='))
        print('  d) Display Inventory')
        print('  a) Add Item(s) to Inventory')
        print('  r) Remove Item(s) from Inventory')
        print('  u) Update Item')
        print()
        print('  x) Save and Exit')
        print('\n> ', end='')
        choice = input()
        if choice == 'x':
            # Save Inventory and EXIT
            saveInventory(bag, saveFile)
            sys.exit()
        if choice == 'd' or choice == 'a' or choice == 'r' or choice == 'u':
            break                               # Process user input

    if choice == 'a':
        # Add Item to Inventory
        addItem(bag, {'name'  : 'Paper', 
                      'count' : 2,
                      'price' : .50, 
                      'weight': .75})

    if choice == 'r':
        # Remove Item(s) from Inventory
        removeItem(bag, {'name' : 'Gold', 
                        'count' : 1,
                        'price' : 1.0, 
                        'weight': 1})

    if choice == 'd':
        # Display Inventory
        displayInventory(bag)

    if choice == 'u':
        # Update Item to Inventory
        updateItem(bag, {'name'  : 'Rock', 
                         'count' : 2,
                         'price' : .7, 
                         'weight': 6.0})