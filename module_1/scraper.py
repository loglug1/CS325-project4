# SOLID IMPLEMENTATION: Interface segregation principle

# This module contains a Scraper interface that is implemented by CNNScraper, it takes
# the url as a parameter on the constructor and has two methods to retrieve infromation about the article: get_title and get_article

import requests
from pyquery import PyQuery
from abc import ABC, abstractmethod

#returns html source of page or None if response is not 200 OK
#helper function for Scraper implementations
def get_source(url: str) -> str | None:
    try:
        page = requests.get(url, timeout=5)
        if page.ok:
            return page.text
    except requests.exceptions.Timeout:
        print("Timed Out")
    except requests.exceptions.MissingSchema:
        print("Invalid URL Schema, try adding http:// or https://")
    except requests.exceptions.RequestException:
        print(f"Error while fetching {url} source")

# returns text inside HTML element selected by selector. For example: '.article__content' would select an element with the 
# class 'article__content' and '#title' would select the element with the id 'title'. For more examples, research jQuery selectors
# helper function for Scraper implementations
def get_inner_html(page_src: str, jQuery_selector: str) -> str:
    doc = PyQuery(page_src)
    res = doc(jQuery_selector)
    return res.text()

#Scraper interface
class Scraper(ABC):
    # when implemented this should fetch the source code from the url
    @abstractmethod
    def __init__(self, url: str):
        pass

    # returns article contents from page source
    @abstractmethod
    def get_article(self):
        pass

    # returns article contents from page source
    @abstractmethod
    def get_title(self):
        pass

#CNN Implementation of Scraper Interface
class CNNScraper(Scraper):
    def __init__(self, url: str):
        self.url = url
        self.source = get_source(self.url)

    # returns article contents from cnn page source
    def get_article(self):
        return get_inner_html(self.source, ".article__content")
    
    # returns article contents from cnn page source
    def get_title(self):
        return get_inner_html(self.source, ".headline__text")

def main():
    print("This is the scraper module. It should be used in addition to another source code file.")

if __name__=="__main__":
    main()