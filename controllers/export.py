import os
import csv
from .utile import Scrap
from views.interface import Interface


class Export:
    def create_csv_file(self, category):
        """creer un fichiers csv avec les data de chaque livre."""
        en_tete = [
            "product_page_url",
            "universal_product_code",
            "title",
            "price_including_tax",
            "price_excluding_tax",
            "number_available",
            "product_description",
            "category",
            "review_rating",
            "image_url",
        ]

        with open(category.name_of_category + ".csv", "w", encoding="UTF-16LE") as f:

            writer = csv.writer(f, delimiter=",")
            writer.writerow(en_tete)

            for book in category:
                ligne_book = [
                    book["product_page_url"],
                    book["upc"],
                    book["title"],
                    book["price_including_tax"],
                    book["price_excluding_tax"],
                    book["number_available"],
                    book["product_description"],
                    book["category"],
                    book["review_rating"],
                    book["image_url"],
                ]
                writer.writerow(ligne_book)
                self.download_img(url_img=book["image_url"], titre=book["title"])

    def download_img(self, url_img, titre):
        scrap = Scrap(url_img)
        title_name = scrap.replace_special_caractere(titre)
        with open(title_name + ".jpg", "wb") as f:
            response = scrap.reponse
            f.write(response.content)
        Interface.display_download_image(self, name=title_name)

    def download_files(self, category):
        """save data in folders"""
        os.chdir("Data/" + category.name_of_category)
        self.create_csv_file(category)
        os.chdir("../../")
