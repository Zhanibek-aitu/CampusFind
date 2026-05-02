import json
import os

from item import Item


class StorageManager:
    def __init__(self, filename="items.json"):
        self.filename = filename

    def save_items(self, items):
        items_as_dicts = []

        for item in items:
            items_as_dicts.append(item.to_dict())

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(items_as_dicts, file, indent=4)

    def load_items(self):
        if not os.path.exists(self.filename):
            return []

        if os.path.getsize(self.filename) == 0:
            return []

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        items = []

        for item_data in data:
            item = Item.from_dict(item_data)
            items.append(item)

        return items