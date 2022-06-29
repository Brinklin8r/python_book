#! python3
# rpg.py
# RPG script
from inventory import Slot, Inventory

item1 = Slot('Default Knife')
item2 = Slot('Full Item', 5, 4.0, 1.10)
item3 = Slot('To be deleted', 3, 1.0, 7.15)
item4 = Slot('fourth item', 1, 1, 2)
dupeItem = Slot('Default Knife', 2, 10)
noItem = Slot('Not in Inventory')

bag = Inventory()

bag.addItem(item1)
bag.addItem(item2)
bag.addItem(item3)
bag.addItem(item4)
bag.addItem(dupeItem)
bag.displayInventory()

bag.deleteItem(item1)
bag.displayInventory()
bag.deleteItem(noItem)
bag.displayInventory()
bag.deleteItem(item3, 3)
bag.displayInventory()
bag.deleteItem(item2, 100)
bag.displayInventory()

bag.updateItem(Slot('Default Knife', 6, 1.9, 20.5))
bag.displayInventory()
bag.updateItem(noItem)
bag.displayInventory()

bag.saveInventory('inventorySave.py')

bag.readInventory('inventoryRead.py')
bag.displayInventory()
