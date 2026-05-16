from datetime import datetime
from functools import wraps

from flask import request, render_template, g


def log_action(action_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if request.method == "POST":
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                with open("activity_log.txt", "a", encoding="utf-8") as file:
                    file.write(
                        f"{current_time} - {action_name} | "
                        f"Route: {request.path} | "
                        f"Method: {request.method}\n"
                    )

            return result

        return wrapper

    return decorator


def validate_item_form(categories, valid_item_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method != "POST":
                return func(*args, **kwargs)

            name = request.form.get("name", "").strip()
            item_type = request.form.get("item_type", "").strip().lower()
            category = request.form.get("category", "").strip()
            location = request.form.get("location", "").strip()
            description = request.form.get("description", "").strip()

            errors = []

            if not name or len(name) < 2:
                errors.append("Item name must be at least 2 characters long.")

            if item_type not in valid_item_types:
                errors.append("Item type must be either lost or found.")

            if category not in categories:
                errors.append("Please select a valid category.")

            if not location or len(location) < 2:
                errors.append("Location must be at least 2 characters long.")

            if not description or len(description) < 3:
                errors.append("Description must be at least 3 characters long.")

            if errors:
                return render_template(
                    "add_item.html",
                    categories=categories,
                    errors=errors,
                    name_value=name,
                    item_type_value=item_type,
                    category_value=category,
                    location_value=location,
                    description_value=description
                )

            g.validated_item_data = {
                "name": name,
                "item_type": item_type,
                "category": category,
                "location": location,
                "description": description
            }

            return func(*args, **kwargs)

        return wrapper

    return decorator