from .utile import Scrap


class Link:
    
    def __init__(self, url_chosen, url_domain):
        
        self.url_chosen = url_chosen
        self.url_domain = url_domain

    
    def get_links_books(self):
        """selects the application case according to the url entered
        by the user.
        Args:
            url of category or site or book.
        Returns:
            list of links of books (one book,category or site).
        """
        url = self.url_chosen
        list_of_links = []
        url_modifie = url[:-10]
        reponse = Scrap(url_modifie + "page-1.html").reponse

        if reponse.ok:
            """case of application for a request for:
            a category of several pages or the site."""
            list_of_links.extend(
                self.get_books_links_from_all_pages(url_modifie)
                )

        elif Scrap(url).soup.find("ol", class_="row"):
            """case of application for a request for:
            a single page category."""
            list_of_links.extend(
                self.get_url_books_from_a_single_page(url)
                )

        else:
            """case of application for a request for a book."""
            list_of_links.append(url)
            
        return list_of_links

    def get_url_books_from_a_single_page(self, url_page):
        """get all books links of page.
        Args:
            Parsing of html page / url page
        Returns:
            list of links of books from a page.
        """
        url_domain = self.url_domain[:36]
        list_of_books_from_single_page = []
        page = Scrap(url_page).soup
        for i in page.find_all("h3"):
            href = i.find("a")["href"]
            book_name = href.split("/").pop(-2)
            list_of_books_from_single_page.append(
                url_domain + book_name + "/index.html"
            )
        return list_of_books_from_single_page

    def get_books_links_from_all_pages(self, url):
        """loop through all pages for a category or site and
        return all available books.
        Args:
            url of category or site .
            response : response (requests).
        Returns:
            list of links of books from a category or site.
        """
        list_of_all_links_of_books = []
        reponse = Scrap(url).reponse
        x = 0
        while reponse.ok:
            x += 1
            url_var = url + "page-" + str(x) + ".html"
            reponse = Scrap(url_var).reponse
            list_of_all_links_of_books.extend(
                self.get_url_books_from_a_single_page(url_var)
            )
        return list_of_all_links_of_books