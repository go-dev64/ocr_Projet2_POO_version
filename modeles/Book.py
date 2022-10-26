# from utile import Scrap


class Book(dict):
    """return dictionnary of data of book

    Args:
        dict (_type_): _description_
    """

    def __init__(self, soup, url):
        self.soup = soup
        self["product_page_url"] = url
        self["upc"] = self.data_of_table()["UPC"]
        self["title"] = soup.h1.string
        self["price_including_tax"] = self.data_of_table()["Price (incl. tax)"].replace(
            "Â", ""
        )
        self["price_excluding_tax"] = self.data_of_table()["Price (excl. tax)"].replace(
            "Â", ""
        )
        self["number_available"] = int(
            "".join(
                [str(i) for i in self.data_of_table()["Availability"] if i.isnumeric()]
            )
        )
        self["product_description"] = soup.h2.find_next("p").text
        self["category"] = soup.find("ul", class_="breadcrumb").find_all("a")[2].string
        self["review_rating"] = soup.find_all("p", class_="star-rating")[0]["class"][1]
        self["image_url"] = self.img()

    def img(self):
        image = str(self.soup.find("div", class_="item active").find("img")["src"])[6:]
        url_absolu = "http://books.toscrape.com/" + str(image)
        return url_absolu

    def data_of_table(self):
        key_of_obj = []
        value_of_obj = []
        for element in self.soup.find("table", class_="table table-striped").find_all(
            "th"
        ):
            key_of_obj.append(element.string)
        for element in self.soup.find("table", class_="table table-striped").find_all(
            "td"
        ):
            value_of_obj.append(element.string)
        result = {x: y for x, y in zip(key_of_obj, value_of_obj)}
        return result
