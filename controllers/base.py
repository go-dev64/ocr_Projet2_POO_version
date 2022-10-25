from .utile import Scrap
from .control_link_page import Link
from .export import Export
import os
from views.interface import Interface
from modeles.website import Website
from 

URL_WEBSITE = "http://books.toscrape.com/catalogue/category/books_1/index.html"
URL_DOMAIN = "http://books.toscrape.com/catalogue/category"


class Controller:
    def __init__(self):
        self.list_of_category = self.list_of_category_of_name()
        self.list_url_of_category = self.list_of_url_of_category()
        self.interface = interface

    def list_of_category_of_name(self):
        """return list of name of category

        Returns:
            _type_: _description_
        """
        list_of_category = []
        site_soup = Scrap(url_page=URL_WEBSITE).soup
        for category in site_soup.find("ul",
                                       class_="nav").find("ul").find_all("a"):
            list_of_category.append(category.string.strip().replace(" ", "_"))
        return list_of_category

    def list_of_url_of_category(self):
        """return list of url of category

        Returns:
            _type_: _description_
        """
        list_of_url = []
        soup = Scrap(URL_WEBSITE).soup
        for category in soup.find("ul", class_="nav").find("ul").find_all("a"):
            list_of_url.append(URL_DOMAIN + category["href"][2:])
        return list_of_url

    def create_instance_webside(self):

        site = Website(
            url=URL_WEBSITE,
            name="book_to_scrap",
            list_url_categories=self.list_url_of_category,
            list_of_name_of_category=self.list_of_category,
        )

        site.append_category()
        return site

    def user_choice(self):
        """function of user choice

        Returns:
            _type_:
        """
        user_choice = self.interface.user_choice_of_data()
        return user_choice

    def url_chosen(self):
        url_chosen = self.application_of_user_choice()
        return url_chosen

    def create_instance_of_book(self, category):
        """create a Instance of Book

        Args:
            category (_type_): _description_
        """
        link = Link(url_chosen=category.url_category, url_domain=URL_DOMAIN)

        category.list_url_book = link.get_links_books()
        for url_book in category.list_url_book:
            soup = Scrap(url_book).soup
            category.append_book(soup, url_book)
            self.interface.display_download_book(category)

    def application_of_user_choice(self, user_choice, website):
        """geneate instance of Book for 1 Book ,
        all books of category or all book of site
        """
        if user_choice == "URL_WEBSITE":
            """generate all Books for all categories"""
            for category in website:
                self.create_instance_of_book(category=category)
                self.interface.display_download_category(category)
                
        elif isinstance(user_choice, int):
            """Gerate all Books for 1 category"""
            self.create_instance_of_book(website[user_choice])
            self.interface.display_download_category(
                website[user_choice].name_of_category
            )            

        else:
            """Generate 1 Book"""
            category_of_book = self.get_category_of_book(
                user_choice).replace(" ", "_")
            for i in website:
                if i.name_of_category == category_of_book.lower():
                    instance_of_category = i
            instance_of_category.list_url_book = user_choice
            soup = Scrap(user_choice).soup
            instance_of_category.append_book(soup, user_choice)
            



    def create_folders_of_category(self, name):
        if not os.path.exists("Data/" + name):
            os.makedirs("Data/" + name)
                

    def get_category_of_book(self, url):
        """return category of chosen book

        Args:
            url (_type_): url of chosen book

        Returns:
            _type_: name of category of book
        """
        category_of_book = (
            Scrap(url).soup.find("ul",
                                 class_="breadcrumb").find_all("a")[2].string
        )
        return category_of_book



    def run(self):
        site = self.create_instance_webside()
        export = Export()
        self.interface = Interface(
            name_of_categories=self.list_of_category,
            list_of_url_categories=self.list_url_of_category,
        )
        user_choice = self.user_choice()
        self.application_of_user_choice(user_choice, website=site)
        for category in site:
            self.create_folders_of_category(category.name_of_category)
            export.download_files(category=category)
            self.interface.display_end_of_process(category=category)
                
        print(site)
