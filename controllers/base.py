from scrap import Scrap
import os
from views.interface import Interface

URL_WEBSITE= str("http://books.toscrape.com/catalogue/category/books_1/index.html")


Interface().user_choice_of_data

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
        


class Data_Type_Chosen_By_User:
    
    def __init__(self, user_input):
        
        self.user_input = user_input
        
    def data_type(self):
    
        if self.user_input == 1:
            
            
            
        
        elif self.user_input == 2:
            Interface().
            
            pass
        
        else:
            self.user_input == 1:
            pass
        
        
        
    



def create_folders_of_category(self):
        if not os.path.exists("Data/" + self.name_of_category):
            os.makedirs("Data/" + self.name_of_category )




     
            
        choice_of_category = category_choice(
                list_names=list_of_name_of_categories
            )
            url_of_category = url_category(
                number_of_category=choice_of_category,
                list_url=list_of_url_categories
            )

        
          
    

    
    
    
    

       
            choice_of_category = category_choice(
                list_names=list_of_name_of_categories
            )
            url_of_category = url_category(
                number_of_category=choice_of_category,
                list_url=list_of_url_categories
            )

            print("Export de la categorie: "
                + list_of_name_of_categories[choice_of_category]
                + " en cours...")
            return url_of_category


        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def get_list_categories():
    """get categories list and list of url of categories pages

    Returns:
        list of url categories and list of categories names
    """
    soup = utile.download_book_page(
        "http://books.toscrape.com/catalogue/category/books_1/index.html"
    )[0]
    categories = soup.find("ul", class_="nav").find("ul").find_all("a")
    list_of_url_categories = []
    list_of_name_of_categories = []
    for cat in categories:
        list_of_url_categories.append(cat["href"][2:])
        list_of_name_of_categories.append(cat.string.strip())
    return list_of_url_categories, list_of_name_of_categories


def category_choice(list_names):
    """return the index of category chosen by user

    Args:
        list_names (_type_): list of names of categories

    Returns:
        _type_: index of category chosen by user
    """

    list_names = list_names
    for i in list_names:
        print(i, "=", list_names.index(i), end=" ; ")

    choice_of_category = int(
        input("\nEntrer le numero de la catégorie choisie et "
              "appuyer sur Entrer :"))
    print("Vous avez choisi la categorie : " + list_names[choice_of_category])
    return choice_of_category


def url_category(number_of_category, list_url):
    """ return url of category chosen by user

    Args:
        number_of_category (_type_): _description_
        list_url (_type_): _description_

    Returns:
        _type_: url of category chosen
    """
    list_url = list_url
    URL_DOMAIN = "http://books.toscrape.com/catalogue/category"
    url_of_the_chosen_category = URL_DOMAIN + list_url[number_of_category]

    return url_of_the_chosen_category



    if choice == 1:
        """ choice of one book
        Returns:
            _type_: url of book chosen
        """
        url_livre = input("Veuillez renseigner l'url du livre et"
                          "appuyer sur Entrer :")
        print("Export du livre en cours...")
        return url_livre

    elif choice == 2:
        """choice of category

        Returns:
            _type_:return url of category chosen
        """
        choice_of_category = category_choice(
            list_names=list_of_name_of_categories
        )
        url_of_category = url_category(
            number_of_category=choice_of_category,
            list_url=list_of_url_categories
        )

        print("Export de la categorie: "
              + list_of_name_of_categories[choice_of_category]
              + " en cours...")
        return url_of_category
