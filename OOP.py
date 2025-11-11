class Object: # This is a class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        return 'Hello' # Without this return, the function will return None

obj1 = Object("John", 20) # This is an instance of the Object class
obj2 = Object("Jane", 21)

obj2.last_name = "Doe" # This is an attribute of the Object class


class Book:
    def __init__(self, title, author, isbn, publication_year) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_available = True

    def get_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Isbn: {self.isbn}')
        print(f'Publication year: {self.publication_year}')
        print(f'Is available: {self.is_available}')

    def check_out(self):
        if self.is_available == True:
            check_out = input(f'Would you like to check out {self.title}? (Y or N): ')
            if check_out == 'Y':
                self.is_available = False
                print(f'You just check out {self.title}')
        else:
            print('Sorry this book is not available to check out.')

    def check_in(self):
        if self.is_available == False:
            check_in = input(f'Would you like to check in {self.title}? (Y or N): ')
            if check_in == 'Y':
                self.is_available = True
                print(f'Thank you for checking in {self.title}.')

class LibraryMember:
    def __init__(self, member_id, name, email) -> None:
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available == True:
            self.borrowed_books.append(book)
            print(f'You just borrowed {book.title}.')
            book.is_available = False
        else:
            print(f'Sorry, {book.title} is not available.')

    def return_book(self, book):
        if len(self.borrowed_books) < 1:
            print('You have no books to return')
        else:
            self.borrowed_books.remove(book)
            print(f'Thank you for returning {book.title}')

    def get_member_info(self):
        print(f'member_id: {self.member_id}')
        print(f'name: {self.name}')
        print(f'emai: {self.email}')

    def view_borrowed_books(self):
        for book in self.borrowed_books:
            print(f'You have borrowed {book.title}')

class Library:
    def __init__(self) -> None:
        self.books = dict()
        self.members = dict()
        self.name = 'The Library'

    def add_book(self, book):
        self.books[book.title] = book.author
        print(f'{book.title} was added to the library.')
        print(self.books)

book1 = Book('Harry potter', 'Billy', 189542, 2004)
# book1.get_info()
book2 = Book('Way of Kings', 'Brandon Sanderson', 5738921, 2012)
# book2.get_info()
conner = LibraryMember('myLibraryCard', 'conner', 'myemail')
conner.borrow_book(book2)
conner.view_borrowed_books()
conner.return_book(book2)
conner.view_borrowed_books()

myLibrary = Library()
myLibrary.add_book(book1)
myLibrary.add_book(book2)