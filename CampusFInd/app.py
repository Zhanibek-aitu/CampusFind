from flask import Flask, render_template, request, redirect, url_for, g

from manager import LostFoundManager
from storage import StorageManager
from item import Item
from decorators import log_action, validate_item_form


app = Flask(__name__)

manager = LostFoundManager()
storage = StorageManager()
manager.items = storage.load_items()

CATEGORIES = [
    "Electronics",
    "Documents",
    "Keys",
    "Clothing",
    "Bags",
    "Books",
    "Accessories",
    "Other"
]

VALID_ITEM_TYPES = ["lost", "found"]
VALID_STATUSES = ["claimed", "unclaimed"]


def filter_items(items, search_query, item_type, category, location, status, date):
    filtered_items = []

    search_query = search_query.lower().strip()
    item_type = item_type.lower().strip()
    category = category.strip()
    location = location.lower().strip()
    status = status.lower().strip()
    date = date.strip()

    for item in items:
        matches = True

        if search_query:
            searchable_text = (
                    item.name + " " +
                    item.category + " " +
                    item.location + " " +
                    item.description
            ).lower()

            if search_query not in searchable_text:
                matches = False

        if item_type:
            if item.item_type.lower() != item_type:
                matches = False

        if category:
            if item.category != category:
                matches = False

        if location:
            if location not in item.location.lower():
                matches = False

        if status:
            if item.status.lower() != status:
                matches = False

        if date:
            if item.date != date:
                matches = False

        if matches:
            filtered_items.append(item)

    return filtered_items


@app.route('/')
def index():
    all_items = manager.list_items()

    search_query = request.args.get('search', '')
    item_type = request.args.get('item_type', '')
    category = request.args.get('category', '')
    location = request.args.get('location', '')
    status = request.args.get('status', '')
    date = request.args.get('date', '')

    filtered_items = filter_items(
        all_items,
        search_query,
        item_type,
        category,
        location,
        status,
        date
    )

    total_count = len(all_items)
    lost_count = len([item for item in all_items if item.item_type == "lost"])
    found_count = len([item for item in all_items if item.item_type == "found"])
    claimed_count = len([item for item in all_items if item.status == "claimed"])

    return render_template(
        'index.html',
        items=filtered_items,
        categories=CATEGORIES,
        total_count=total_count,
        lost_count=lost_count,
        found_count=found_count,
        claimed_count=claimed_count,
        search_value=search_query,
        item_type_value=item_type,
        category_value=category,
        location_value=location,
        status_value=status,
        date_value=date
    )


@app.route('/add', methods=['GET', 'POST'])
@validate_item_form(CATEGORIES, VALID_ITEM_TYPES)
@log_action("Item add")
def add_item():
    if request.method == 'POST':
        item_data = g.validated_item_data

        new_item = Item(
            item_data["name"],
            item_data["item_type"],
            item_data["category"],
            item_data["location"],
            item_data["description"]
        )

        manager.add_item(new_item)
        storage.save_items(manager.items)

        return redirect(url_for('index'))

    return render_template(
        'add_item.html',
        categories=CATEGORIES,
        errors=[],
        name_value="",
        item_type_value="",
        category_value="",
        location_value="",
        description_value=""
    )


@app.route('/update/<item_id>', methods=['POST'])
@log_action("Item status update")
def update_item(item_id):
    new_status = request.form.get('new_status', '').strip().lower()

    if new_status in VALID_STATUSES:
        manager.update_status(item_id, new_status)
        storage.save_items(manager.items)

    return redirect(url_for('index'))


@app.route('/delete/<item_id>', methods=['POST'])
@log_action("Item delete")
def delete_item(item_id):
    manager.delete_item(item_id)
    storage.save_items(manager.items)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)