import requests
from bs4 import BeautifulSoup



class Scrap:
    """return request et parsing of requests of html page"""
    
    def __init__(self, url_page):
        self.url_page = url_page
        self.reponse = self.request()
        self.soup = self.soup()
    
    def request(self):
        """get request of url"""
        reponse = requests.get(self.url_page)
        return reponse
    
    def soup(self):
        """get parsing of request of url"""
        reponse = self.request()
        soup = BeautifulSoup(reponse.content, "html.parser")
        return soup
    
    def replace_special_caractere(self, my_str):
        """replace special caractere
        Args:
            my_str (_type_): _description_
        Returns:
            _type_: _description_(without cspecial caractere)
        """
        special_caractere = "}’{!@#$%^&*'()¨^\[]};,./<>?|`~-=_+:‽"
        for element in special_caractere:
            my_str = my_str.replace(element, "_").replace(
                "é", "e").replace("è", "e").replace('"', " ")
        return my_str
        
    

