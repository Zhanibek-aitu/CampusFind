from CampusFInd.item import Item
from manager import LostFoundManager

manager = LostFoundManager()

item1 = Item("Wallet", "lost", "Accessories", "Library", "Black wallet")
item2 = Item("Phone", "found", "Electronics", "Cafeteria", "Samsung phone")

manager.add_item(item1)
manager.add_item(item2)

print("All items:")
for item in manager.list_items():
    print(item)