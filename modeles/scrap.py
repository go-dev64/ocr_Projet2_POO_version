import requests
from bs4 import BeautifulSoup

class Scrap:
    """return request et parsing of requests"""
    
    def __init__(self, url_page):
        self.url_page = url_page
    
    
    def request(self):
        """get request of url"""
        reponse = requests.get(self.url_page)
        return reponse
    
    def soup(self):
        """get parsing of request of url"""
        soup = BeautifulSoup(self.request.content, "html.parser")
        return soup