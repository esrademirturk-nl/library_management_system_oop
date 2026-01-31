class Book():
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        self.borrowed_by = None
    
    def show_info(self):
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Publication Year: {self.publication_year}, "
            f"Borrowed: {self.is_borrowed}, "
            f"Borrowed By: {self.borrowed_by}"
        )
    
    def borrow_book(self,user):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user
            return True
        return False

    def return_book(self):
        if not self.is_borrowed:
            return False 
        else:
            self.is_borrowed = False
            self.borrowed_by = None
            return True

    def to_dict(self):
        return {"title" : self.title,
                "author" : self.author,
                "publication_year": self.publication_year,
                "is_borrowed" : self.is_borrowed,
                "borrowed_by" : self.borrowed_by}
    
    
class Magazine(Book):
    def __init__(self, title, author, publication_year,issue):
        super().__init__(title, author, publication_year)
        self.issue = issue
    
    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        return data
        

class Novel(Book):
    def __init__(self, title, author, publication_year,genre):
        super().__init__(title, author, publication_year)
        self.genre = genre
    
    def to_dict(self):
        data =  super().to_dict()
        data["genre"] = self.genre
        return data





