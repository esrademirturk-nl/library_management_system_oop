import os
import json
from .user import User
from .book import Book,Magazine,Novel 
class Library():
    def __init__(self,name):
        self.name = name
        self.books = []
        self.users = []
   
    def add_book(self,book):
        self.books.append(book)

    def add_user(self,user):
        self.users.append(user)
        return True

    def show_all_books(self):  
        return "\n".join(
            f"Title: {book.title}, Author: {book.author}, "
            f"Year: {book.publication_year}, "
            f"Status: {'Available' if not book.is_borrowed else 'Borrowed'}, "
            f"Borrowed By: {book.borrowed_by if book.borrowed_by !=None else '-'}"
            for book in self.books
        )
        
    def login(self,name, password):          
        for user in self.users:    
            if user.name == name :
                if user.password == password:
                    return user
                else :
                    raise Exception( "Username or password is incorrect!")
            
        raise Exception("There is no such username. Please first sign up!")
                
    def save(self,file_name):  #saves all data to JSON
        try:
            data={
                "name": self.name,
                "users": [user.to_dict() for user in self.users],
                "books": [book.to_dict() for book in self.books]
            }
            users= data["users"]
            books=data["books"]
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data,f)
            with open("data/users.json", "w", encoding="utf-8") as f:
                json.dump(users,f)
            with open("data/books.json", "w", encoding="utf-8") as f:
                json.dump(books,f)
        except Exception as e:
            print(f"Dosya kaydedilemedi: {e}")

    def load(self,filename):  #loads data from JSON and restores relationships
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
            self.books = []
        for b in data["books"]:
            if "genre" in b:
                book = Novel(
                b["title"],
                b["author"],
                b["publication_year"],
                b["genre"]
                )
            elif "issue" in b:
                book = Magazine(
                b["title"],
                b["author"],
                b["publication_year"],
                b["issue"]
                )
            else:
                book = Book(
                b["title"],
                b["author"],
                b["publication_year"]
                )

            book.is_borrowed = b["is_borrowed"]
            book.borrowed_by = b["borrowed_by"]
            self.books.append(book)

    # USERS
        self.users = []
        for u in data["users"]:
            user = User(u["name"], u["password"])
            user.borrowed_books = u["borrowed_books"]
            self.users.append(user)