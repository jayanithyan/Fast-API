# FastAPI Item Store API

A simple REST API built with **FastAPI** for creating, reading, updating, deleting, searching, filtering, and sorting items.

This project uses a **JSON file for storage** instead of a database, keeping the project lightweight and easy to understand.

---

## 🚀 Features

- Create an item
- Get all items
- Get an item by ID
- Update an item
- Delete an item
- Search items by name
- Filter items by price
- Sort items by price
- Pagination
- Item count
- Average item price
- Request validation using Pydantic
- Automatic API documentation
- Basic API tests

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **JSON**
- **Pytest**

---

## 📁 Project Structure

```text
Fast-API/
│
├── Main.py
├── router.py
├── schemas.py
├── storage.py
├── items.json
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    └── test_items.py