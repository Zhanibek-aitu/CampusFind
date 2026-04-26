import uuid
from datetime import datetime

class Item:
    def __init__(self, name, item_type, category, location, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.item_type = item_type
        self.category = category
        self.location = location
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.status = "unclaimed"

    def __str__(self):
        return f"{self.name} | {self.category} | {self.location} | {self.status}"