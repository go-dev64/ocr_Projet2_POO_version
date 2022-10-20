
from controllers.scrap import Scrap


class Interface:
    """user interface , return his choice
    
    
    """
    
    def __init__(self, name_of_categories, list_of_url_categories):
        
        self.list_of_name_of_categories = name_of_categories
        self.list_of_url_categories = list_of_url_categories
        
    def user_choice_of_data(self):
        """return user choice of data to expotr

        Returns:
            _type_: int (1 = book, 2= category or 3 = site)
        """
        
        choice_of_data = int(
            input(
                "    Pour exporter les données d'un livre, Taper 1\n\
        Pour exporter les données d'une catégorie de livre, Taper 2\n\
        Pour exporter les données du site, Taper 3\n\
        Indiquer votre choix: "
            )
        )
        
        return choice_of_data


    def user_choice_is_book(self):
        """ choice of one book
            Returns:
                _type_: url of book chosen
            """
        url_livre = input("Veuillez renseigner l'url du livre et"
                            "appuyer sur Entrer :")
        print("Export du livre en cours...")
        return url_livre
        
    
    def user_choice_is_category(self):
        """return the number of category chosen
            Returns:
                _type_:number of category
            """
        for i in self.list_of_name_of_categories:
            print(i, "=", self.list_of_name_of_categories.index(i), end=" ; ")

        choice_of_category = int(
            input("\nEntrer le numero de la catégorie choisie et "
                "appuyer sur Entrer :"))
        print("Vous avez choisi la categorie : " 
              + self.list_of_name_of_categories[choice_of_category]
              )
        print("Export de la categorie: "
                + self.list_of_name_of_categories[choice_of_category]
                + " en cours..."
                )
        return choice_of_category
                
    
    def user_choice_is_site(self):
        
        print("Export du site en cours...")
      
            
            
            
            
            
       