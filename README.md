# Week 2 Progress – CampusFind

## ✔ Completed

| Task | Status |
|------|--------|
| JSON storage | ✅ |
| StorageManager implementation | ✅ |
| Data persistence after restart | ✅ |
| Filtering by type | ✅ |
| Filtering by category | ✅ |
| Filtering by location | ✅ |
| Filtering by status | ✅ |
| Unique categories using set | ✅ |
| Unique locations using set | ✅ |
| Code cleanup and refactoring | ✅ |

---

## What was done

During Week 2, we implemented file-based data storage using JSON.  
The application can now save all lost and found items into a local JSON file and load them again when the program is restarted.

We also improved the filtering system and added separate functions for better code organization.

---

## Main improvements

| Area | Description |
|------|-------------|
| JSON storage | Items are saved into `items.json` |
| Data loading | Items are loaded automatically when the program starts |
| StorageManager | Handles saving and loading data |
| Filtering | Items can be filtered by type, category, location, and status |
| Sets | Unique categories and locations are displayed using sets |
| Refactoring | Console menu logic was separated into functions |

---

## Current State

The project currently works as a console-based application.  
Users can:

- Add lost or found items
- View all items
- Update item status
- Delete items
- Filter items
- Save and load data from a JSON file

---

## Plan for Week 3

| Task | Description |
|------|-------------|
| Flask setup | Create basic Flask application |
| Routes | Add routes for home page and item actions |
| HTML templates | Create basic pages for displaying and adding items |
| Backend connection | Connect Flask routes with existing Python logic |
| Web dashboard | Start moving from console interface to browser interface |
