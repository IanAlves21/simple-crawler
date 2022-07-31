import requests

from bs4 import BeautifulSoup
from prettytable import PrettyTable


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

        formated_table = PrettyTable()
        formated_table.field_names = list(self.site_structured_data[0].keys())

        for data_element in self.site_structured_data:
            row = list()

            for data_key in formated_table.field_names:
                row.append(data_element[data_key])
            
            formated_table.add_row(row)

        print(formated_table)

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