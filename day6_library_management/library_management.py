class Book():

    def __init__(self , book_id ,title, author):

        self.book_id = book_id
        self.author = author
        self.title = title
        self.is_book_available = True

    def borrow(self):
        if self.is_book_available:
            self.is_book_available = False
            return True
        return False

    def return_book(self):
        self.is_book_available = True

    def __str__(self):
        status = "Available" if self.is_book_available else "Borrowd"
        return f"{self.book_id} . {self.title} . {self.author} . {status}"




class Library():

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added")

    def view_books(self):
        if not self.books:
            print("No books available")
            return
        print("\n Library Books")
        print("-"*40)
        for book in self.books:
            print(book)

    def borrow_books(self, book_id):
        for book in self.books:
            if book.book_id ==book_id:
                if book.borrow():
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return
            print("Book not found")
    def return_books(self , book_id):
        for book in self.books:
            if book.book_id ==book_id:
                book.return_book()
                print("Book returned")
                return
            else:
                print("Book not found")
def show_menu():
    print("\n📖 LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            book_id = input("Enter book id: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(book_id , title, author)
            library.add_book(book)
        if choice == "2":
            library.view_books()
        if choice == "3":
            book_id = input("Enter book id: ")
            library.borrow_books(book_id)
        if choice == "4":
            book_id = input("Enter book id: ")
            library.return_books(book_id)
        if choice == "5":
            print("Thank you for using this program")
            print("/n Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()











