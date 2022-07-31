import re

from src.crawler.crawler import SimpleCrawler

class VultrCrawler(SimpleCrawler):
    # Constructor
    def __init__(self):
        super().__init__("https://www.vultr.com/products/bare-metal/#pricing")
        self.site_structured_data = self.__get_structured_data()

    # Private methods
    def __get_all_list_items(self) -> list:
        list_items = self.site_raw_data.find_all("div", class_="col-lg-3")
        items = list()

        for element in list_items:
            s = re.sub(r'[^a-zA-Z0-9\-\n\.\s\/]', '', element.get_text())
            s = s.replace('\t', '')
            t = s.split(s[0])
            x = filter(lambda x: len(x) > 0, t)
            items.append(list(x))

        items.pop()

        return items

    def __get_structured_data(self) -> list:
        items = self.__get_all_list_items()
        structured_data = list()

        for i in items:
            element = dict()

            element["CPU/VCPU"] = f"{''.join(i[5:-3]) if 'nvme' in i[4].lower() else ''.join(i[4:-3])}"
            element["STORAGE"] = f"{i[3]} {i[4] if 'nvme' in i[4].lower() else ''}"
            element["MEMORY"] = f"{i[-3]}"
            element["PRICE"] = f"{i[1]}"
            element["NAME"] = f"{i[0]}"
            element["NETWORK"] = f"{i[-1]}"
            element["BANDWIDTH"] = f"{i[-2]}"

            structured_data.append(element)
        
        return structured_data