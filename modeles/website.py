from category import Category


class Website(list):
    
    def __init__ (self, url, name, list_url_categories):
        
        self.url = url
        self.name = name
        self.list_of_url_categories = list_url_categories
        
    def append_category(self, list_of_categories):
        
        for category, url in list_of_categories , self.list_of_url_categories:
            category = category.lower()
            
            self.append(Category(url_category= url, name_of_category=category, ))
            
            
toto = ["http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"]

book_to_scrap = Website(url="http://books.toscrape.com/catalogue/category/books_1/index.html",
                        name="book_to_scrap",
                         list_url_categories=toto
                         )
book_to_scrap.append_category(toto)

print(book_to_scrap)