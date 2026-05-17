# CampusFind – Web-Based Lost & Found Management System

CampusFind is a web-based Lost & Found management system for campus items.  
It allows users to register, search, filter, update, and delete lost or found item records through a local Flask web interface.

---

## Project Purpose

The project was created to practice and demonstrate key Python programming concepts:

- Object-Oriented Programming
- Data structures
- File handling
- External modules
- Decorators
- Flask web development
- Basic frontend interactivity

---

## Main Features

| Feature | Description |
|--------|-------------|
| Add Item | Add lost or found items using a web form |
| View Items | Display all saved records on the dashboard |
| Update Status | Change item status to claimed or unclaimed |
| Delete Item | Remove item records from the system |
| Search | Search items by keyword |
| Filtering | Filter by type, category, location, status, and date |
| Validation | Prevent invalid or incomplete form submissions |
| Logging | Save important actions into an activity log |
| JSON Storage | Store and reload data using a local JSON file |
| Web UI | Use the system through a browser |
| JavaScript | Dark mode, quick search, delete confirmation, and character counter |

---

## Technologies Used

| Technology / Module | Purpose |
|---------------------|---------|
| Python 3 | Main programming language |
| Flask | Web server and routing |
| HTML / CSS | Web page structure and styling |
| JavaScript | Basic frontend interactivity |
| Jinja2 | Dynamic HTML rendering |
| JSON | Local data storage |
| `uuid` | Unique item ID generation |
| `datetime` | Date and log timestamps |
| `os` | File existence checking |
| `functools` | Decorator support |

---

## Project Structure

| File / Folder | Purpose |
|---------------|---------|
| `app.py` | Main Flask application and routes |
| `item.py` | Item class and object serialization |
| `manager.py` | Core item management logic |
| `storage.py` | JSON save/load system |
| `decorators.py` | Custom validation and logging decorators |
| `main.py` | Console version used during early testing |
| `items.json` | Local JSON database |
| `requirements.txt` | Required Python package list |
| `templates/` | HTML templates |
| `static/` | CSS and JavaScript files |

---

## How It Works

When the application starts, saved records are loaded from `items.json`.

When a user adds an item:

1. Flask receives form data from the HTML form.
2. The validation decorator checks the input.
3. A new `Item` object is created.
4. The item is stored in the manager list.
5. The updated data is saved back to `items.json`.

The system converts `Item` objects into dictionaries before saving them to JSON and converts dictionaries back into `Item` objects when loading data.

---

## Notes

- `items.json` acts as a simple local database.
- Each item has a unique UUID.
- The UUID is used internally for update and delete actions.
- `app.py` is used to run the final web version.
- `main.py` was used for console-based testing during development.
