

class book:

    def __init__(self, product_page_url,
                 universal_product_code,
                 title,
                 price_including_tax,
                 price_excluding_tax,
                 number_available,
                 product_description,
                 category,
                 review_rating,
                 image_url):
        self.product_page_url = product_page_url
        self.universal_product_code = universal_product_code
        self.title = title
        self.price_including_tax = price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.review_rating = review_rating
        self.image_ur = image_url
