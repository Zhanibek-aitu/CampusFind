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

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]