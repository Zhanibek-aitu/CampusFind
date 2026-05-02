import uuid
from datetime import datetime


class Item:
    def __init__(
            self,
            name,
            item_type,
            category,
            location,
            description,
            item_id=None,
            date=None,
            status="unclaimed"
    ):
        self.id = item_id if item_id else str(uuid.uuid4())
        self.name = name
        self.item_type = item_type
        self.category = category
        self.location = location
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "item_type": self.item_type,
            "category": self.category,
            "location": self.location,
            "description": self.description,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            item_type=data["item_type"],
            category=data["category"],
            location=data["location"],
            description=data["description"],
            item_id=data["id"],
            date=data["date"],
            status=data["status"]
        )

    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.item_type} | "
            f"{self.category} | "
            f"{self.location} | "
            f"{self.status}"
        )