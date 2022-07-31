import requests
import csv
import json

from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import datetime


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

        columns = list(self.site_structured_data[0].keys())
        file_name = str(datetime.now().timestamp()).replace(".", "") + ".csv"

        try:
            with open(file_name, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=columns)
                writer.writeheader()

                for data in self.site_structured_data:
                    writer.writerow(data)

        except IOError:
            print("I/O error")

    def save_json(self) -> None:
        print("save_json")

        file_name = str(datetime.now().timestamp()).replace(".", "") + ".json"

        try:
            with open(file_name, "w") as json_file:
                json.dump(self.site_structured_data, json_file, indent=4)
                
        except IOError:
            print("I/O error")

    # Private methods
    def __request_data(self) -> BeautifulSoup:
        print("request_for_data")

        html = requests.get(self.url)
        soup_element = BeautifulSoup(html.content, 'html.parser')

        return soup_element
