# Week 3 Progress – CampusFind

## ✔ Completed

| Task | Status |
|------|--------|
| Flask setup | ✅ |
| Basic Flask routes | ✅ |
| HTML templates created | ✅ |
| Connection between Flask and backend | ✅ |
| Display all items in browser | ✅ |
| Add item through web form | ✅ |
| Update item status | ✅ |
| Delete item | ✅ |
| JSON persistence with Flask | ✅ |
| Basic web dashboard | ✅ |

---

## What was done

During Week 3, we converted the console-based application into a simple web-based system using Flask.

The project now includes:

- A Flask application: `app.py`
- HTML templates for displaying and adding items
- Routes for adding, updating, and deleting items
- Integration between the web interface and the existing Python backend logic
- Persistent JSON storage connected to the Flask application

The application can now be accessed and used directly through a web browser.

---

## Current Features

Users can currently:

- View all lost and found items
- Add new items through a web form
- Update item status: claimed / unclaimed
- Delete items
- Save and load data automatically using JSON

---

## Current Project Structure

| File / Folder | Purpose |
|---------------|---------|
| `app.py` | Flask application and routes |
| `item.py` | Item class |
| `manager.py` | Main logic for managing items |
| `storage.py` | JSON saving and loading |
| `main.py` | Console version for testing |
| `items.json` | Stored item data |
| `requirements.txt` | Required external modules |
| `templates/index.html` | Main web page |
| `templates/add_item.html` | Form for adding new items |

---

## Plan for Week 4

| Task | Description |
|------|-------------|
| Input validation | Prevent empty or invalid form submissions |
| Custom decorators | Add decorators for logging and validation |
| UI improvements | Improve layout, colors, spacing, and usability |
| Additional filtering | Add filtering directly in the web interface |
| Code cleanup | Refactor repeated logic and improve readability |
| Testing | Test all main functions and fix bugs |

---

## Notes

The project is now functioning as a basic web application.

Future work will focus on improving user experience, validation, and overall project stability.
