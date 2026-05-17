# Week 4 Progress – CampusFind

## ✔ Completed

| Task | Status |
|------|--------|
| Input validation system | ✅ |
| Validation decorator | ✅ |
| Activity logging decorator | ✅ |
| Item filtering by type | ✅ |
| Item filtering by category | ✅ |
| Item filtering by location | ✅ |
| Item filtering by status | ✅ |
| Item filtering by date | ✅ |
| Search system | ✅ |
| Claimed / Unclaimed status update | ✅ |
| Statistics cards on dashboard | ✅ |
| Improved web dashboard UI | ✅ |
| Responsive filter section | ✅ |
| External module integration | ✅ |

---

## What was done

During Week 4, we focused on implementing advanced project functionality and improving the overall usability of the web application.

The project now includes:

- A custom decorator for activity logging
- A custom decorator for input validation
- Validation rules for incorrect or incomplete item records
- A complete filtering and search system directly inside the web interface
- Item filtering by:
  - category
  - item type
  - location
  - status
  - date
- Status update system for claimed and unclaimed items
- Dashboard statistics cards
- Improved and more structured web interface

The filtering system was integrated into the Flask application using query parameters and dynamic rendering.

---

## Current Features

Users can currently:

- Add new lost or found items
- View all stored items
- Update item status
- Delete items
- Search items using keywords
- Filter items by:
  - type
  - category
  - location
  - status
  - date
- Save and reload data using JSON persistence
- Automatically log important system actions
- Receive validation errors for incorrect form submissions

---

## Current Project Structure

| File / Folder | Purpose |
|---------------|---------|
| `app.py` | Main Flask application and routes |
| `item.py` | Item class |
| `manager.py` | Main item management logic |
| `storage.py` | JSON storage management |
| `decorators.py` | Custom decorators for validation and logging |
| `items.json` | Stored item database |
| `activity_log.txt` | Logged system activity |
| `requirements.txt` | Required external modules |
| `templates/index.html` | Main dashboard page |
| `templates/add_item.html` | Add item form |
| `static/style.css` | CSS styling for the web interface |

---

## External Modules Used

| Module | Purpose |
|--------|---------|
| `flask` | Web framework and routing |
| `json` | Data storage and persistence |
| `datetime` | Date and time management |
| `uuid` | Unique item ID generation |
| `os` | File existence checking |
| `functools` | Decorator support |

---

## Plan for Week 5

| Task | Description |
|------|-------------|
| Final testing | Test all project features and edge cases |
| Bug fixing | Fix remaining issues and improve stability |
| UI polishing | Improve visual appearance and usability |
| JavaScript improvements | Add small interactive frontend features |
| README finalization | Prepare final project documentation |
| Diagram preparation | Create architecture, UML, and flowchart diagrams |
| Presentation preparation | Prepare slides and live demonstration |
| Code cleanup | Refactor and organize final code structure |

---

## Notes

The project now fully supports item management, filtering, validation, logging, and persistent storage through a web interface.

Week 4 focused mainly on advanced Flask functionality, decorators, filtering systems, and improving overall project usability.
