#from controllers.utile import Scrap
from book import Book
#from views.interface import Interface


class Category(list):
    """return list of books of category"""

    def __init__(self, url_category, name_of_category, list_of_url_of_books = None):
        self.url_category = url_category
        self.name_of_category = name_of_category
        self.list_url_book = list_of_url_of_books

    def append_book(self, book):
        for book in self.list_url_book:
            self.append(book)
            #Interface(self).display_download_book(self)

