from Book1 import Book
from Catalog1 import Catalog
# from User import Member, Librarian

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015','312')
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '123hg','H1B4')
catalog.addBookItem(b, '123hg','H1B5')