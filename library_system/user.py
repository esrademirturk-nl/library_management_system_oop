class User():
    def __init__(self,name,password):
        self.name= name 
        self.password = password
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.borrow_book(self.name):
            self.borrowed_books.append(book)
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
        
    def return_book(self,book):
        if book not in self.borrowed_books:
            print("You did not borrow this book.")
            return
        book.return_book()
        self.borrowed_books.remove(book)
        print("Book returned successfully.")
 
    def list_borrowed_books(self):
        if not self.borrowed_books:
            return "You have not borrowed any books."
        return "\n".join(           
            f"{book.show_info()}"
            for book in self.borrowed_books
        )
      
    def to_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": [book.to_dict() for book in self.borrowed_books]
        }
    

  