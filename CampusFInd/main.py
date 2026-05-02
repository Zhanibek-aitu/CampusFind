from item import Item
from manager import LostFoundManager
from storage import StorageManager


def print_items(items):
    if len(items) == 0:
        print("No items found.")
    else:
        for item in items:
            print(f"ID: {item.id[:8].upper()} | {item}")


def find_item_by_short_id(items, short_id):
    for item in items:
        if item.id.startswith(short_id.lower()):
            return item
    return None


def add_item_menu(manager, storage):
    name = input("Item name: ")
    item_type = input("Type (lost/found): ")
    category = input("Category: ")
    location = input("Location: ")
    description = input("Description: ")

    item = Item(name, item_type, category, location, description)
    manager.add_item(item)
    storage.save_items(manager.items)

    print("Item added and saved.")


def update_status_menu(manager, storage):
    update_id = input("Enter first characters of item ID: ")
    new_status = input("Enter new status (claimed/unclaimed): ")

    item = find_item_by_short_id(manager.list_items(), update_id)

    if item:
        manager.update_status(item.id, new_status)
        storage.save_items(manager.items)
        print("Status updated and saved.")
    else:
        print("Item not found.")


def delete_item_menu(manager, storage):
    delete_id = input("Enter first characters of item ID: ")

    item = find_item_by_short_id(manager.list_items(), delete_id)

    if item:
        manager.delete_item(item.id)
        storage.save_items(manager.items)
        print("Item deleted and saved.")
    else:
        print("Item not found.")


def filter_items_menu(manager):
    print("\nFilter by:")
    print("1. Type")
    print("2. Category")
    print("3. Location")
    print("4. Status")
    print("5. Show unique categories")
    print("6. Show unique locations")

    choice = input("Choose filter option: ")

    if choice == "1":
        item_type = input("Enter type (lost/found): ")
        print_items(manager.filter_by_type(item_type))

    elif choice == "2":
        category = input("Enter category: ")
        print_items(manager.filter_by_category(category))

    elif choice == "3":
        location = input("Enter location: ")
        print_items(manager.filter_by_location(location))

    elif choice == "4":
        status = input("Enter status (claimed/unclaimed): ")
        print_items(manager.filter_by_status(status))

    elif choice == "5":
        categories = manager.get_unique_categories()

        if len(categories) == 0:
            print("No categories found.")
        else:
            print("Unique categories:")
            for category in categories:
                print("-", category)

    elif choice == "6":
        locations = manager.get_unique_locations()

        if len(locations) == 0:
            print("No locations found.")
        else:
            print("Unique locations:")
            for location in locations:
                print("-", location)

    else:
        print("Invalid filter option.")


def main():
    manager = LostFoundManager()
    storage = StorageManager()

    manager.items = storage.load_items()

    print("CampusFind - Lost & Found System")

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Show all items")
        print("3. Update item status")
        print("4. Delete item")
        print("5. Filter items")
        print("6. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item_menu(manager, storage)

        elif choice == "2":
            print("\nAll items:")
            print_items(manager.list_items())

        elif choice == "3":
            update_status_menu(manager, storage)

        elif choice == "4":
            delete_item_menu(manager, storage)

        elif choice == "5":
            filter_items_menu(manager)

        elif choice == "6":
            storage.save_items(manager.items)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


main()