import os

class Category:

    list_of_book = []

    def __init__(self,
                 url_category,
                 name_of_category):
        self.url_category = url_category
        self.name_of_category = name_of_category

    def create_folders_of_category(self):
        if not os.path.exists("Data/" + self.name_of_category):
            os.makedirs("Data/" + self.name_of_category )
            

