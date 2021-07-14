from BookItem1 import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self,book,isbn,rack):
        b = BookItem1(self,book,isbn,rack)
        self.book_item.append(b)
        self.total_count +=1