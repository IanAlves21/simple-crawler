import requests

from bs4 import BeautifulSoup


class SimpleCrawler:
    # Constructor
    def __init__(self, url: str):
        print("initializing")
        self.url = url
        self.site_raw_data = self.__request_data()
        self.site_structured_data = dict()

    # Public methods
    def print(self) -> None:
        print("print")
        print(self.site_structured_data)

    def save_csv(self) -> None:
        print("save_csv")

    def save_json(self) -> None:
        print("save_json")

    # Private methods
    def __request_data(self) -> BeautifulSoup:
        print("request_for_data")
        html = requests.get(self.url)
        soup_element = BeautifulSoup(html.content, 'html.parser')

        return soup_element