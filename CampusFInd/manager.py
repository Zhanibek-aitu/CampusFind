class LostFoundManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items

    def delete_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                return True
        return False

    def update_status(self, item_id, new_status):
        for item in self.items:
            if item.id == item_id:
                item.status = new_status
                return True
        return False

    def filter_by_type(self, item_type):
        return [
            item for item in self.items
            if item.item_type.lower() == item_type.lower()
        ]

    def filter_by_category(self, category):
        return [
            item for item in self.items
            if item.category.lower() == category.lower()
        ]

    def filter_by_location(self, location):
        return [
            item for item in self.items
            if item.location.lower() == location.lower()
        ]

    def filter_by_status(self, status):
        return [
            item for item in self.items
            if item.status.lower() == status.lower()
        ]

    def get_unique_categories(self):
        return set(item.category for item in self.items)

    def get_unique_locations(self):
        return set(item.location for item in self.items)