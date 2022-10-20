
from controllers.scrap import Scrap


class Interface:
    
    def user_choice():
        """user choice interface

        Returns:
            _type_: url chosen by user(book, category or site)
        """
        list_of_url_categories = get_list_categories()[0]
        list_of_name_of_categories = get_list_categories()[1]
        choice = int(
            input(
                "    Pour exporter les données d'un livre, Taper 1\n\
        Pour exporter les données d'une catégorie de livre, Taper 2\n\
        Pour exporter les données du site, Taper 3\n\
        Indiquer votre choix: "
            )
        )

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

        else:
            """choice of site
            return l url of site
            """
            URL_SITE = ("http://books.toscrape.com/"
                        "catalogue/category/books_1/index.html"
                        )
            print("Export du site en cours...")
            return URL_SITE

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

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


def user_choice():
    """user choice interface

    Returns:
        _type_: url chosen by user(book, category or site)
    """
    list_of_url_categories = get_list_categories()[0]
    list_of_name_of_categories = get_list_categories()[1]
    choice = int(
        input(
            "    Pour exporter les données d'un livre, Taper 1\n\
    Pour exporter les données d'une catégorie de livre, Taper 2\n\
    Pour exporter les données du site, Taper 3\n\
    Indiquer votre choix: "
        )
    )

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

    else:
        """choice of site
        return l url of site
        """
        URL_SITE = ("http://books.toscrape.com/"
                    "catalogue/category/books_1/index.html"
                    )
        print("Export du site en cours...")
        return URL_SITE
