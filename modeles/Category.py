from .book import Book


class Category(list):
    """return list of books of category"""

    def __init__(self, url_category, name_of_category):
        self.url_category = url_category
        self.name_of_category = name_of_category
        self.list_url_book = []

    def append_book(self, soup, url):
        book = Book(soup, url)
        self.append(book)
