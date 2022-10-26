
# OpenClassRooms_PROJET_2: Utilisez les bases de Python pour l'analyse de marché

## Scénario :

 En tant que analyste marketing chez Books Online vous devez créer un système de surveillance des prix (scraper) sur [Books to Scrape](http://books.toscrape.com/index.html), un revendeur de livres en ligne.

 Il s'agira d'une simple application exécutable à la demande visant à récupérer les prix au moment de son exécution.
***

<center>

![Logo de Books Online.](https://raw.githubusercontent.com/go-dev64/ocr_projet_2/main/image/1600779540759_Online%20bookstore-01.png "Logo de Books Online.")
# Books Online

</center>


# Projet: Application de scraping
1. [General](#Générale)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [Fonctionnement](#fonctionnement)
6. [License](#licence)


## <a id = Générale>Générale</a>
***
Cette application a pour but d'extraire les données, selon le choix de l'utilisateur, d'un livre, d'une catégorie de livre ou de tous les livres du site de revendeur de livres en lignes [Books to Scrape](http://books.toscrape.com/index.html). Les données extraites seront transformées en fichiers CSV avec en-têtes de colonnes les champs suivantes :
* product_page_url
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url

Lors de l'utilisation de l'application, celle-ci va créer un dossier _"Data"_ contenant un sous-dossier pour chaque catégorie de livre.
Dans chaque sous-dossier nous retrouverons le fichier CSV des données exportées du ou des livres de la catégorie ainsi que les images de couverture du ou des livres.


## <a id = technologies>Technologies</a>
***

Les scripts de l'application sont exclusivement écrit en **Python**  

* [Python](https://www.python.org/downloads/release/python-3107/) : Version 3.10.7


## <a id = installation>Installation</a>
***
> Installation de Python 3.10.7 requise.

Télécharger les différents modules, à partir du _"Repository"_.

Toutes les opérations suivantes seront exécutées dans ce répertoire courant.

### _**Création et activation environnement Virtuel**_


Taper dans votre terminal les commandes suivantes : 

```
python3 -m venv env
...
env\Scripts\activate
```


Votre terminal affichera la ligne de commande comme ci-dessous :

![](/image/env.png)

###  **_Installation des packages_**

Taper dans votre terminal les commandes suivantes : 
```
pip install -r requirements.txt
```

Cette commande permet l'installation de tous les packages nécessaire au fonctionnement de l'application.

Une fois l'installation terminer l'application est opérationnel.


## <a id= fonctionnement>Fonctionnement</a>
***
Le lancement de l'application s'effectue avec la commande suivante dans le terminal :
```
    pyhton main.py
```


Le terminal vous proposera un choix : 


```
    Pour exporter les données d'un livre, Taper 1
    Pour exporter les données d'une catégorie de livre, Taper 2
    Pour exporter les données du site, Taper 3
    Indiquer votre choix puis appuyer sur Entrer : 

```
Sélectionner l'export de votre choix et suivez les instructions du terminal.


### _Exemple pour l'export d'un livre._


Après avoir fait le choix d'exporter un livre, renseigner url de celui-ci et appuyer sur "Entrer".

```
    Pour exporter les données d'un livre, Taper 1
    Pour exporter les données d'une catégorie de livre, Taper 2
    Pour exporter les données du site, Taper 3
    Indiquer votre choix puis appuyer sur Entrer : 1
Veuillez renseigner l'url du livre : (adresse url du livre)
```


L'application lancera l'export des données du livre renseigné.


###  _Exemple pour l'export d'une catégorie de livre._


Après avoir fait le choix d'exporter une catégorie de livre, la liste des catégories disponibles apparait dans le terminal.


Renseigner le numéro de la catégorie souhaitée et appuyer sur "Entrer".


```
   Pour exporter les données d'un livre, Taper 1
   Pour exporter les données d'une catégorie de livre, Taper 2
   Pour exporter les données du site, Taper 3
   Indiquer votre choix: 2
Travel = 0 ; Mystery = 1 ; Historical Fiction = 2 ; Sequential Art = 3 ; Classics = 4 ; Philosophy = 5 ; Romance = 6 ; Womens Fiction = 7 ; Fiction = 8 ; Childrens = 9 ; Religion = 10 ; Nonfiction = 11 ; Music = 12 ; Default = 13 ; Science Fiction = 14 ; Sports and Games = 15 ; Add a comment = 16 ; Fantasy = 17 ; New Adult = 18 ; Young Adult = 19 ; Science = 20 ; Poetry = 21 ; Paranormal = 22 ; Art = 23 ; Psychology = 24 ; Autobiography = 25 ; Parenting = 26 ; Adult Fiction = 27 ; Humor = 28 ; Horror = 29 ; History = 30 ; Food and Drink = 31 ; Christian Fiction = 32 ; Business = 33 ; Biography = 34 ; Thriller = 35 ; Contemporary = 36 ; Spirituality = 37 ; Academic = 38 ; Self Help = 39 ; Historical = 40 ; Christian = 41 ; Suspense = 42 ; Short Stories = 43 ; Novels = 44 ; Health = 45 ; Politics = 46 ; Cultural = 47 ; Erotica = 48 ; Crime = 49 ; 
Entrer le numéro de la catégorie choisie : 
```

Par exemple taper 4 et appuyer sur "Entrer" pour exporter la catégorie _"Classics"_.


L'application lancera l'export des données de chaque livre de la catégorie. 


### _Exemple pour l'export de tous les livres du site_


En sélectionnant l'optioin 3, l'application lancera l'export de chaque livre du site.


## <a id = licence>Licence</a>


* [Licence ouverte](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf) : Version 2.0
***
