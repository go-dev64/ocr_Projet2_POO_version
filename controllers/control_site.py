from utile  import Scrap
from modeles.website import Website
from controllers.base import URL_WEBSITE, URL_DOMAIN



class Site:


    def list_of_category_of_name(self):
            list_of_category = []
            site_soup  = Scrap(url_page=URL_WEBSITE).soup
            for category in site_soup.find(
                            "ul", class_="nav").find("ul").find_all("a"):
                list_of_category.append(category.string.strip().replace(" ", "_"))
            return list_of_category


    def list_of_url_of_category(self):
            list_of_url = []
            for category in self.soup.find(
                            "ul", class_="nav").find("ul").find_all("a"):
                list_of_url.append(URL_DOMAIN + category["href"][2:])
            return list_of_url
        
    book_to_scrap = Website(url=URL_WEBSITE, list_url_categories=list_of_url_of_category)
    book_to_scrap.append_category(list_of_categories=list_of_category_of_name)