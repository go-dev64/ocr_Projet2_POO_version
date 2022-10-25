#from controllers.base import URL_WEBSITE


class Interface:
    """user interface , return his choice"""

    def __init__(self, name_of_categories, list_of_url_categories):

        self.list_of_name_of_categories = name_of_categories
        self.list_of_url_categories = list_of_url_categories
        
    def first_choice(self):
        choice_of_data = int(
            input(
                "    Pour exporter les données d'un livre, Taper 1\n\
        Pour exporter les données d'une catégorie de livre, Taper 2\n\
        Pour exporter les données du site, Taper 3\n\
        Indiquer votre choix et appuyer sur Entrer: "
            )
        )
        return choice_of_data
                

    def user_choice_of_data(self):
        choice_of_data = self.first_choice()

        match choice_of_data:

            case 1:
                """return  url for 1 book"""
                url_livre = input(
                    "Veuillez renseigner l'url du livre et"
                    "appuyer sur Entrer :"
                )
                print("Export du livre en cours...")
                return url_livre

            case 2:
                """return url of 1 category"""
                for i in self.list_of_name_of_categories:
                    print(i,
                          "=",
                          self.list_of_name_of_categories.index(i), end=" ; "
                          )

                choice_of_category = int(
                    input(
                        "\nEntrer le numero de la catégorie choisie et "
                        "appuyer sur Entrer :"
                    )
                )
                print(
                    "Vous avez choisi la categorie : "
                    + self.list_of_name_of_categories[choice_of_category]
                )
                print(
                    "Export de la categorie: "
                    + self.list_of_name_of_categories[choice_of_category]
                    + " en cours..."
                )
                return choice_of_category

            case 3:
                """return url of site"""
                print("Export du site en cours...")
                return "URL_WEBSITE"


    def display_download_book(self, books):
        print(len(books), ":livres traités")
        
    def display_download_category(self, category):
        print("Categorie: ",category,"traitée" )

    def display_download_image(self, name):
        print("Telechargement de l'image du livre: " + name)

    def display_end_of_process(self, category):
        print(
            "Creation du fichier: "
            + category
            + ".csv dans le dossier: Data/ "
            + category
        )
