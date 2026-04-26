from item import Item
from manager import LostFoundManager

manager = LostFoundManager()

item1 = Item("Wallet", "lost", "Accessories", "Library", "Black wallet")
item2 = Item("Phone", "found", "Electronics", "Cafeteria", "Samsung phone")

manager.add_item(item1)
manager.add_item(item2)

print("All items:")
for item in manager.list_items():
    print(f"ID: {item.id[:8].upper()} | {item}")

print("\nUpdate Status")
update_id = input("Enter item ID to update: ")
new_status = input("Enter new status: ")

for item in manager.list_items():
    if item.id.startswith(update_id):
        manager.update_status(item.id, new_status)
        print("Status updated")
        break

print("\nItems after update:")
for item in manager.list_items():
    print(f"ID: {item.id[:8].upper()} | {item}")