from .category import Category


class Website(list):
    def __init__(self, url, name, list_url_categories, list_of_name_of_category):

        self.url = url
        self.name = name
        self.list_of_url_categories = list_url_categories
        self.list_of_name = list_of_name_of_category

    def append_category(self):

        for category, url in zip(self.list_of_name, self.list_of_url_categories):
            category = category.lower()
            category = Category(url_category=url, name_of_category=category)
            self.append(category)


