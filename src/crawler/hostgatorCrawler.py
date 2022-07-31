from src.crawler.crawler import SimpleCrawler

class HostgatorCrawler(SimpleCrawler):
    # Constructor
    def __init__(self):
        super().__init__("https://www.hostgator.com/vps-hosting")
        self.site_structured_data = self.__get_structured_data()

    # Private methods
    def __get_all_list_items(self) -> list:
        main_component_tag = self.site_raw_data.find("section", class_="compare-table")
        head_tag = main_component_tag.find("thead").find_all("th", class_="product")
        body_tag = main_component_tag.find("tbody").find_all("tr")
        items = list()

        for element in head_tag:
            name = element.h4.string
            price = element.button.get_text()

            items.append([name, price])

        for element in body_tag:
            for index, value in enumerate(element.find_all("td")):
                if(index > 0):
                    items[index-1].append(value.get_text())

        return items

    def __get_structured_data(self) -> list:
        items = self.__get_all_list_items()
        structured_data = list()

        for i in items:
            element = dict()

            element["CPU/VCPU"] = f"{i[2]}"
            element["STORAGE"] = f"{i[4]}"
            element["MEMORY"] = f"{i[3]}"
            element["PRICE"] = f"{i[1]}"
            element["NAME"] = f"{i[0]}"
            element["NETWORK"] = f"{i[-1]}"
            element["BANDWIDTH"] = f"{'Unmetered Bandwidth' if len(i[-2])==0 else i[-2]}"

            structured_data.append(element)
        
        return structured_data