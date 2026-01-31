from library_system import Library,User,Book
from library_system import Book,Novel,Magazine
from utils import helpers

library = Library("Best Library")
library.load("data/library.json")
while(True):
    try:
        choice = helpers.main_menu(library.name)
        if(choice=="1"):
            username= input("Your Username = ")
            password = input("Your password = ")
            username= "bob"
            password ="abcd"
            current_user = library.login(username,password)
            if not current_user:
                raise Exception("Invalid credentials.")  
            else:                
                while True:
                    option = helpers.library_Menu()
                    if option == '1':
                        print(library.show_all_books())                       
                    elif option =='2':
                        print(library.show_all_books())                       
                        book_name =input("Please Enter Book Name = ").title().casefold()
                        found_book = None
                        for book in library.books:
                            if book.title.title().casefold() == book_name:
                                found_book = book
                                break                                                                   
                        if found_book:
                            current_user.borrow_book(found_book)
                        else:
                            print("Book not found.")  
                            break            
                    elif option =='3':
                        print(current_user.list_borrowed_books())                       
                        book_name =input("Please Enter Book Name = ").title().casefold()
                        found_book = None
                        for book in library.books:
                            if book.title.title().casefold() == book_name:
                                found_book = book
                                break                                                                   
                        if found_book:
                            current_user.return_book(found_book)
                        else:
                            print("Book not found.")  
                            break                        
                    elif option == '4':  
                       print(current_user.list_borrowed_books())
                    elif option == '0':
                        library.save("data/library.json")
                        print("Data saved. Goodbye!")
                        break
        elif(choice=="2"):
            username= input("Your Username = ")
            password = input("Your password = ")
            current_user = User(username, password)
            library.add_user(current_user)
            print("Account created successfully.")
        else: break

    except Exception as ex: 
        print("Errror= ",ex,end='\n\n')

 

