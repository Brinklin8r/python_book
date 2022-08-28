#! python3
# testCasesInventory.py
# Test Cases for Inventory.py

import unittest
import io
import sys
from inventory import Slot, Inventory

class SlotTestCase(unittest.TestCase):
    """Test for Slot class in 'inventory.py'"""

    def testSlotNameOnly(self):
        """Test passing a slot only a name."""
        testSlot = Slot("Name Only")
        self.assertEqual(testSlot.itemName, "Name Only" )
        self.assertEqual(testSlot.itemCount, 1 )
        self.assertEqual(testSlot.itemWeight, 0.0 )
        self.assertEqual(testSlot.itemPrice, 0.0 )

    def testSlotNameCount(self):
        """Test passing a slot name and item count."""
        testSlot = Slot("Name Count", 3)
        self.assertEqual(testSlot.itemName, "Name Count" )
        self.assertEqual(testSlot.itemCount, 3 )
        self.assertEqual(testSlot.itemWeight, 0.0 )
        self.assertEqual(testSlot.itemPrice, 0.0 )

    def testSlotNameWeight(self):
        """Test passing a slot name and item weight."""
        testSlot = Slot("Name Weight", itemWeight= 8.1)
        self.assertEqual(testSlot.itemName, "Name Weight" )
        self.assertEqual(testSlot.itemCount, 1 )
        self.assertEqual(testSlot.itemWeight, 8.1 )
        self.assertEqual(testSlot.itemPrice, 0.0 )

    def testSlotNamePrice(self):
        """Test passing a slot name and item price."""
        testSlot = Slot("Name Price", itemPrice= 3.10 )
        self.assertEqual(testSlot.itemName, "Name Price" )
        self.assertEqual(testSlot.itemCount, 1 )
        self.assertEqual(testSlot.itemWeight, 0.0 )
        self.assertEqual(testSlot.itemPrice, 3.1 )

    def testSlotFullItem(self):
        """Test passing full slot information."""
        testSlot = Slot("Full Item", 5, 4.0, 1.10)
        self.assertEqual(testSlot.itemName, "Full Item" )
        self.assertEqual(testSlot.itemCount, 5 )
        self.assertEqual(testSlot.itemWeight, 4.0 )
        self.assertEqual(testSlot.itemPrice, 1.10 )

class InventoryTestCase(unittest.TestCase):
    """Test for Inventory class in 'inventory.py'"""

    def setUp(self):
        """Create a base Slot objects for test methods."""
        self.itemFull       = Slot("Tunic of Cool", 1, 100, 100.77)
        self.emptyInventory = Inventory()
        self.itemsInventory = Inventory()
        self.itemsInventory.inventory = [
            Slot("Sword of Awesome", 1, 10, 1000.0),
            Slot("Gold", 90, 1, 1.0),
            Slot("Shield of Light (+1)", 1, 10, 2500.0),
            Slot("Rope (50 feet)", 2, 1.2, 25.0),
            Slot("Rock", 25, 5.5, 0.03),
            Slot("Paper", 20, 0.75, 0.5)
        ]
                                    
    def testInventoryAddItemFullItemEmptyList(self):
        """Test adding an item to an empty inventory list."""
        self.assertIsInstance(self.emptyInventory, Inventory)
        self.emptyInventory.addItem(self.itemFull)
        self.assertIn(self.itemFull, self.emptyInventory.inventory)

    def testInventoryAddItemFullItemItemList(self):
        """Test adding an item to an existing inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.itemsInventory.addItem(self.itemFull)
        self.assertIn(self.itemFull, self.itemsInventory.inventory)

    def testInventoryAddItemDuplicateItemItemList(self):
        """Test adding a duplicate item to an existing inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.dupeItem = Slot("Gold", 20, 11.7)
        self.itemsInventory.addItem(self.dupeItem)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Gold":
                self.assertEqual(item.itemName  , "Gold")
                self.assertEqual(item.itemCount , 110)
                self.assertEqual(item.itemWeight, 1.0)
                self.assertEqual(item.itemPrice , 1.0)

    def testInventoryDeleteItemAllItem(self):
        """Test deleting an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.deleteItem = Slot("Sword of Awesome")
        self.itemsInventory.deleteItem(self.deleteItem)
        self.assertNotIn(self.deleteItem, self.itemsInventory.inventory)

    def testInventoryDeleteItemOneItem(self):
        """Test deleting one of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.deleteItem = Slot("Gold")
        self.itemsInventory.deleteItem(self.deleteItem, 1)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Gold":
                self.assertEqual(item.itemName  , "Gold")
                self.assertEqual(item.itemCount , 89)
                self.assertEqual(item.itemWeight, 1.0)
                self.assertEqual(item.itemPrice , 1.0)

    def testInventoryDeleteItemMultipleItem(self):
        """Test deleting multiple of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.deleteItem = Slot("Paper")
        self.itemsInventory.deleteItem(self.deleteItem, 10)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Paper":
                self.assertEqual(item.itemName  , "Paper")
                self.assertEqual(item.itemCount , 10)
                self.assertEqual(item.itemWeight, .75)
                self.assertEqual(item.itemPrice , .5)

    def testInventoryDeleteItemNonItem(self):
        """Test deleting  of an item not in inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.deleteItem = Slot("No Exists")
        self.itemsInventory.deleteItem(self.deleteItem)
        self.assertNotIn(self.deleteItem, self.itemsInventory.inventory)

    def testInventoryUpdateItemItemCount(self):
        """Test updating the itemCount of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.updateItem = Slot("Paper", 30)
        self.itemsInventory.updateItem(self.updateItem)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Paper":
                self.assertEqual(item.itemName  , "Paper")
                self.assertEqual(item.itemCount , 30)
                self.assertEqual(item.itemWeight, 0)
                self.assertEqual(item.itemPrice , 0)

    def testInventoryUpdateItemItemWeight(self):
        """Test updating the itemWeight of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.updateItem = Slot("Paper", itemWeight= 3.1)
        self.itemsInventory.updateItem(self.updateItem)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Paper":
                self.assertEqual(item.itemName  , "Paper")
                self.assertEqual(item.itemCount , 1)
                self.assertEqual(item.itemWeight, 3.1)
                self.assertEqual(item.itemPrice , 0)

    def testInventoryUpdateItemItemPrice(self):
        """Test updating the itemPrice of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.updateItem = Slot("Paper", itemPrice= 1.1)
        self.itemsInventory.updateItem(self.updateItem)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Paper":
                self.assertEqual(item.itemName  , "Paper")
                self.assertEqual(item.itemCount , 1)
                self.assertEqual(item.itemWeight, 0)
                self.assertEqual(item.itemPrice , 1.1)

    def testInventoryUpdateItemAll(self):
        """Test updating all the properties of an item from inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.updateItem = Slot("Paper", 33, 6.8, 4.38)
        self.itemsInventory.updateItem(self.updateItem)
        for item in self.itemsInventory.inventory:
            if item.itemName == "Paper":
                self.assertEqual(item.itemName  , "Paper")
                self.assertEqual(item.itemCount , 33)
                self.assertEqual(item.itemWeight, 6.8)
                self.assertEqual(item.itemPrice , 4.38)

    def testInventoryUpdateItemNonItem(self):
        """Test deleting an item not in inventory list."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.updateItem = Slot("No Exists")
        self.itemsInventory.updateItem(self.updateItem)
        self.assertNotIn(self.updateItem, self.itemsInventory.inventory)

    def testInventoryDisplayInventory(self):
        """Test the displayInventory function."""
        self.assertIsInstance(self.itemsInventory, Inventory)
        self.expectedDisplay = """--------------------------------------------------
     Item Name       | Count | Weight |  Price   |
---------------------+-------+--------+----------|
Sword of Awesome     |     1 |  10.00 | $1000.00 |
Gold                 |    90 |   1.00 |    $1.00 |
Shield of Light (+1) |     1 |  10.00 | $2500.00 |
Rope (50 feet)       |     2 |   1.20 |   $25.00 |
Rock                 |    25 |   5.50 |    $0.03 |
Paper                |    20 |   0.75 |    $0.50 |
==================================================
Total Items:         139
Total Weight:     264.90
Total Value:    $3650.75
"""     # https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        self.capturedOutput = io.StringIO()         # Create StringIO object
        sys.stdout = self.capturedOutput            #  and redirect stdout.
        self.itemsInventory.displayInventory()      # Call function.
        sys.stdout = sys.__stdout__                 # Reset redirect.
        self.assertEqual(self.capturedOutput.getvalue(), self.expectedDisplay)

unittest.main(verbosity=2)