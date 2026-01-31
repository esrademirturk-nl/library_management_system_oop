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
```text
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
```
---
## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/esrademirturk-nl/library_management_system_oop.git

3. Run the project:
   ```bash
   python main.py

---
## 📋 Program Flow

- On startup, a **login screen** is shown.  
- The user can **log in** or **create a new account**.  
- ## 📋 Menu Options
   1. List all books  
   2. Borrow a book  
   3. Return a book  
   4. Show my borrowed books  
   5. Save and exit 
- On exit, all data is **saved to a JSON file**.  
- On the next run, the system **loads the saved state** and continues.


