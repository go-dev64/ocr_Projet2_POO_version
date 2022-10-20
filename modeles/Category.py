import os

list1 = [1,2,3,4,5,6,9,8,7,8,5,6,49,55,9,5,9]

class Category:
    """return list of books of category
    """

    def __init__(self,
                 url_category,
                 name_of_category
                 ):
        self.url_category = url_category
        self.name_of_category = name_of_category
        self.list = list
        

    
            

    def append_element_to_list_of_links_of_book(self):
        
        for link in self.list:
            self.list_of_links_of_book.append(link)
        
        
        
        

toto = Category(url_category="xxx", name_of_category="toto", list=list1)
toto.append_element_to_list_of_links_of_book()
print (toto.name_of_category)
print(toto.list_of_links_of_book)