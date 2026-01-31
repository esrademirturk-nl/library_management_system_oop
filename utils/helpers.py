def main_menu(library):
    print("-"*133)
    print(f"{'|':<132}","|")
    print(f"{'|':<45}",f"{"Welcaome To"+ library :<86}","|")
    print(f"{'|':<132}","|") 
    print(f"{'|':<45}",f"{ "Sign in":<20}",f"{'=  1':<65}","|")
    print(f"{'|':<45}",f"{ "Sing up":<20}",f"{'=  2':<65}","|")
    print(f"{'|':<132}","|")                                                                        
    print("-"*133)
    return  input("Choose your operation = ")

def library_Menu():
        print("-"*133)
        print(f"{'|':<132}","|") 
        print(f"{'|':<45}",f"{ "List all books":<25}",f"{'=  1':<60}","|")
        print(f"{'|':<45}",f"{ "Borrow a book":<25}",f"{'=  2':<60}","|")
        print(f"{'|':<45}",f"{ "Return a book":<25}",f"{'=  3':<60}","|")
        print(f"{'|':<45}",f"{ "Show my borrowed books":<25}",f"{'=  4':<60}","|")
        print(f"{'|':<45}",f"{ "Save and exit":<25}",f"{'=  0':<60}","|")
        print(f"{'|':<132}","|")                                                                        
        print("-"*133)
        return  input("Choose your operation = ")

