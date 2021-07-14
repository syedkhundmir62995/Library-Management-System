from Book1 import Book
from BookItem1 import BookItem

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        print("Huuu")
        return b

    
    def addBookItem(self,book,isbn,rack):
        print('hello')
        b1 = Book(book.name,book.author,book.publish_date,book.pages)
        b1.addBookItem(book.name,isbn,rack)
        print('World')