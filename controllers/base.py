from scrap import Scrap

URL_WEBSITE= str("http://books.toscrape.com/catalogue/category/books_1/index.html")


class List_Of_Categories(list):
    """return list of categories

    Args:
        list (_type_): _description_
    """
    def __init__(self):
        soup = Scrap(url_page=URL_WEBSITE).soup
        for category in soup.find("ul",
                        class_="nav").find("ul").find_all("a"):
            self.append(category.string.strip())
        


