# 📚 Library Management System (Python)

A beginner-friendly Library Management System built with **Python**.  
Manage books, users, and book lending via a **command-line interface**.  
All data is stored in **JSON files**, so information is persistent between program runs.

---

## 🚀 Features

### 📖 Book Management
- Add, view, and list all books  
- Support for `Book`, `Novel`, `Magazine`  
- Show borrowed status and borrower  

### 👤 User Management
- Register new users  
- Login existing users  
- Track borrowed books  

### 🔄 Borrow & Return System
- Borrow available books  
- Return borrowed books  
- Automatically update book availability  

---

## 🛠️ Technologies Used
- Python 3  
- JSON module (data storage)  
- `os` module (file handling)  
- Basic error handling (`try` / `except`)  

---

## 📁 Project Structure
project/
│
├── data/
│   ├── library.json       # Main library data
│   ├── users.json         # User backup
│   └── books.json         # Book backup
├── library_system/
│   ├── __init__.py
│   ├── library.py         # Library class
│   ├── user.py            # User class
│   ├── book.py            # Book, Novel, Magazine classes
├── utils/
│   └── helpers.py         # Menu helper functions
└── main.py                # Main program (CLI)

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.  
2. Run the project:

```bash
python main.py


