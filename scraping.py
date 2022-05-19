import re

from bs4 import BeautifulSoup
from urllib import request


class Suumo:
    def __init__(self, url: str):
        self.url = url
        self.soup = self.scraping()

    def scraping(self):
        response = request.urlopen(self.url)
        soup = BeautifulSoup(response, 'html.parser')
        response.close()
        return soup

    def station(self):
        return [i.text for i in self.soup.select('td div.property_view_table-read')]

    def rent_fee(self):
        return self.soup.select_one(".property_view_note-emphasis").text

    def address(self):
        return self.soup.select_one("table.property_view_table td.property_view_table-body").text



