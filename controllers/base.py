from scrap import Scrap
import os
import views.interface
from modeles.Category import Category
from modeles.Book import Book

URL_WEBSITE = "http://books.toscrape.com/catalogue/category/books_1/index.html"
URL_DOMAIN = "http://books.toscrape.com/catalogue/category"


class List_Of_Categories:
    """return list of categories and list url of categories
    Args:
        list (_type_): _description_
    """

    def __init__(self):
        self.soup = Scrap(url_page=URL_WEBSITE).soup
        self.list_of_category_name = self.list_of_category_name()
        self.list_url_of_category = self.list_of_url_of_category()

    def list_of_category_name(self):
        list_of_category = []
        for category in self.soup.find(
                        "ul", class_="nav").find("ul").find_all("a"):
            list_of_category.append(category.string.strip())
        return list_of_category

    def list_of_url_of_category(self):
        list_of_url = []
        for category in self.soup.find(
                        "ul", class_="nav").find("ul").find_all("a"):
            list_of_url.append(category["href"][2:])
        return list_of_url


class Controller:
    def __init__(self):
        self.list_of_category = List_Of_Categories().list_of_category_name
        self.list_url_of_category = List_Of_Categories().list_url_of_category
        self.user_choice = Interface(
            name_of_categories=self.list_of_category
        ).user_choice_of_data
        self.url_chosen = self.application_of_user_choice()

    def application_of_user_choice(self):
        """return url chosen by user( url of book,
        url of category or url of website)

        Returns:
            _type_: _description_ : url
        """
        if self.user_choice == URL_WEBSITE:
            for category in self.list_of_category:
                self.create_folders_of_category(category)

            return URL_WEBSITE

        elif self.user_choice == int:

            self.create_folders_of_category(
                self.list_of_category[self.user_choice]
                )
            url_of_the_chosen_category = URL_DOMAIN
            +self.list_url_of_category[self.user_choice]
            
            self.list_of_category[self.user_choice] = Category(
                url_category=url_of_the_chosen_category,
                name_of_category=self.list_of_category[self.user_choice],
                list=self.select_case_of_application(
                    url_of_the_chosen_category
                    )
            )

        else:
            category_of_book = self.get_category_of_book(
                self.user.choice)
            url_of_category = self.list_url_of_category[
            self.list_of_category.find(category_of_book)
            ]
    
            self.create_folders_of_category(category_of_book)
            
            
            

    def select_case_of_application(self):
        """selects the application case according to the url entered
        by the user.
        Args:
            url of category or site or book.
        Returns:
            list of links of books (one book,category or site).
        """
        url = self
        list_of_links = []
        url_modifie = url[:-10]
        reponse = Scrap(url_modifie + "page-1.html").reponse

        if reponse.ok:
            """case of application for a request for:
            a category of several pages or the site."""
            list_of_links.extend(
                self.get_books_links_from_all_pages(url_modifie)
                )

        elif Scrap(url).soup.find("ol", class_="row"):
            """case of application for a request for:
            a single page category."""
            list_of_links.extend(
                self.get_url_books_from_a_single_page(url)
                )

        else:
            """case of application for a request for a book."""
            list_of_links.append(url)
        return list_of_links

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

    def get_books_links_from_all_pages(self):
        """loop through all pages for a category or site and
        return all available books.
        Args:
            url of category or site .
            response : response (requests).
        Returns:
            list of links of books from a category or site.
        """
        list_of_all_links_of_books = []
        reponse = Scrap(self).reponse
        x = 0
        while reponse.ok:
            x += 1
            url_var = self + "page-" + str(x) + ".html"
            reponse = Scrap(url_var).reponse
            list_of_all_links_of_books.extend(
                self.get_url_books_from_a_single_page(url_var)
            )
        return list_of_all_links_of_books

    def create_folders_of_category(self):
        if not os.path.exists("Data/" + self):
            os.makedirs("Data/" + self)

    def get_category_of_book(self):

        category_of_book = (
            Scrap(self).soup.find(
                "ul", class_="breadcrumb").find_all("a")[2].string
        )
        return category_of_book
