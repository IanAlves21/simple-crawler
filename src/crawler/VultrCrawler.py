from src.crawler.SimpleCrawler import SimpleCrawler

class VultrCrawler(SimpleCrawler):
    def __init__(self):
        super().__init__("https://www.vultr.com/products/bare-metal/#pricing")