from ..controllers.scrap import Scrap
from ..controllers.base import URL_DOMAIN
from Book import Book


class Category(list):
    """return list of books of category"""

    def __init__(self, url_category, name_of_category):
        self.url_category = url_category
        self.name_of_category = name_of_category
        self.list_url_book = []
        self.list_instance_of_book = []






















    def append_book(self):
        url = self.url_category
        url_modifie = url[:-10]
        reponse = Scrap(url_modifie + "page-1.html").reponse

        if reponse.ok:
            """case of application for a request for:
            a category of several pages or the site."""
            self.list_url_book.extend(
                self.get_books_links_from_all_pages(url_modifie)
                )

        elif Scrap(url).soup.find("ol", class_="row"):
            """case of application for a request for:
            a single page category."""
            self.list_url_book.extend(
                self.get_url_books_from_a_single_page(url)
                )
            
            
    def get_url_books_from_a_single_page(self):
        """get all books links of page.
        Args:
            Parsing of html page / url page
        Returns:
            list of links of books from a page.
        """
        list_of_books_from_single_page = []
        page = Scrap(self).soup
        for i in page.find_all("h3"):
            href = i.find("a")["href"]
            book_name = href.split("/").pop(-2)
            list_of_books_from_single_page.append(
                URL_DOMAIN + book_name + "/index.html"
            )
        return list_of_books_from_single_page
    
    def instance_book(self):
        for i in self.list_url_book:
            i = Book(i)
            self.append(i)