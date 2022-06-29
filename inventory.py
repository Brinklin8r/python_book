#! python3
# inventory.py
# RPG CRUD inventory management script v2

class Slot():
    '''Simple inventory slot model.'''

    def __init__(self, itemName, itemCount=1, itemWeight=0.0, itemPrice=0.0):
        self.itemName = itemName
        self.itemCount = itemCount
        self.itemWeight = itemWeight
        self.itemPrice = itemPrice

    def displayItem(self, columnWidths):
        '''Displays a single inventory item.'''
        print(self.itemName.ljust(columnWidths[0]),
              str(self.itemCount).rjust(columnWidths[1]),
              "{:.2f}".format(self.itemWeight).rjust(columnWidths[2]),
              "${:.2f}".format(self.itemPrice).rjust(columnWidths[3]),
              sep=' | ', end=' |\n')

################################################################################


class Inventory():
    '''Simple inventory management model.'''

    def __init__(self):
        self.inventory = []

    # Add item to inventory.
    def addItem(self, item):
        '''Adds an item to the inventory.'''
        # Check if there is already an item with the same name.
        found = False
        for slot in self.inventory:
            # Yes: update count
            if slot.itemName == item.itemName:
                slot.itemCount += item.itemCount
                found = True
                break
        if not(found):
            # No: add item
            self.inventory.append(item)

    # Remove item from inventory.
    def deleteItem(self, item, delCount=1):
        '''Removes an item to the inventory.'''
        # Check if there is an item with the same name.
        found = False
        slotCount = 0
        for slot in self.inventory:
            # Yes: update count if there are enough.
            if slot.itemName == item.itemName:
                if slot.itemCount > delCount:
                    slot.itemCount -= delCount
                    print(
                        f'Removed {delCount} of {item.itemName}s from your inventory.')
                elif delCount == slot.itemCount:
                    del self.inventory[slotCount]
                    print(f'Removed all {item.itemName}s from your inventory.')
                else:
                    # ERROR if not enough.
                    print(
                        f'Unable to delete {delCount} {item.itemName}s.  You only have {slot.itemCount}!')
                found = True
                break
            slotCount += 1
        if not(found):
            # No: ERROR
            print(f'Unable to delete {item.itemName}s.  You have none!')

    # Update item in inventory.
    def updateItem(self, item):
        '''Updates an item's info in the inventory.'''
        # Check if there is already an item with the same name.
        found = False
        for slot in self.inventory:
            # Yes: update info
            if slot.itemName == item.itemName:
                slot.itemCount = item.itemCount
                slot.itemWeight = item.itemWeight
                slot.itemPrice = item.itemPrice
                print(f'Updated {item.itemName} with new values.')
                found = True
                break
        if not(found):
            # No: ERROR
            print(f'Unable to find item {item.itemName}.')

    # Display inventory.
    def displayInventory(self):
        '''Displays the inventory report including total weight, total item count
            and total item price.'''
        # for item in self.inventory:
        #     print(item.itemName)
        #     print(item.itemCount)
        #     print(item.itemWeight)
        #     print(item.itemPrice)
        itemsWeight = 0.0
        itemsPrice = 0.00
        itemsCount = 0
        # List of length of column headers.
        colWidths = [9, 5, 6, 5]
        totalWidth = 0

        for item in self.inventory:                      # Calculate column widths
            if colWidths[0] < len(item.itemName):
                colWidths[0] = len(item.itemName)
            if colWidths[1] < len(str(item.itemCount)):
                colWidths[1] = len(str(item.itemCount))
            if colWidths[2] < len(str(item.itemWeight)) + 1:    # 2nd decimal
                colWidths[2] = len(str(item.itemWeight)) + 1
            if colWidths[3] < len(str(item.itemPrice)) + 2:     # $ and 2nd decimal
                colWidths[3] = len(str(item.itemPrice)) + 2

        for length in colWidths:                        # Calculate Width of Inventory Report
            totalWidth += length + 3                    # Adjust for spacer character " | "
        totalWidth -= 1                                 # Adjust for last character being " |"

        # Inventory Report Header
        print('-' * totalWidth)
        print('Item Name'.center(colWidths[0]), 'Count'.center(colWidths[1]),
              'Weight'.center(colWidths[2]),    'Price'.center(colWidths[3]),
              sep=' | ', end=' |\n')
        print('-' * colWidths[0], '-' * colWidths[1],
              '-' * colWidths[2], '-' * colWidths[3],
              sep='-+-', end='-|\n')

        # Inventory Report Item(s)
        for item in self.inventory:
            item.displayItem(colWidths)
            itemsWeight += item.itemWeight * item.itemCount
            itemsPrice += item.itemPrice * item.itemCount
            itemsCount += item.itemCount

        # Inventory Report Footer
        print('=' * totalWidth)
        print('Total Items:'.ljust(13),  str(itemsCount).rjust(10))
        print('Total Weight:'.ljust(13),
              "{:.2f}".format(itemsWeight).rjust(10))
        print('Total Value:'.ljust(13),
              "${:.2f}".format(itemsPrice).rjust(10))

    # Save inventory.
    def saveInventory(self, saveFileName):
        '''Saves inventory to a file.'''
        saveFile = open(saveFileName, 'w')
        for item in self.inventory:
            saveFile.write(item.itemName + ',' + str(item.itemCount) +
                           ',' + str(item.itemWeight) + ',' +
                           str(item.itemPrice) + '\n')
        saveFile.close()
        print(f'Inventory saved to {saveFileName}.')

    # Read inventory.
    def readInventory(self, readFileName):
        '''Read inventory from a file.'''
        readFile = open(readFileName)
        for line in readFile.readlines():
            test = line.split(',')
            self.addItem(Slot(test[0], int(test[1]),
                         float(test[2]), float(test[3])))
        readFile.close()
        print(f'Inventory read from {readFileName}.')
