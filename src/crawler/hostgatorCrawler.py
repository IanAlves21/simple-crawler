from src.crawler.crawler import SimpleCrawler

class HostgatorCrawler(SimpleCrawler):
    # Constructor
    def __init__(self):
        super().__init__("https://www.hostgator.com/vps-hosting")
        self.site_structured_data = self.__get_structured_data()

    # Private methods
    def __get_all_list_items(self) -> list:
        items = list()

        return items

    def __get_structured_data(self) -> list:
        items = self.__get_all_list_items()
        structured_data = list()
        
        return structured_data