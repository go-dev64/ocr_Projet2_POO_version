import requests
from bs4 import BeautifulSoup


class Scrap:
    """return request et parsing of requests"""
    
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
    
    



