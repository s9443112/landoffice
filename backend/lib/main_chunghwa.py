import backend.lib.crawler_chunghwa as start_crawler
import backend.lib.parse_text as parse_to_txt

# from tkinter import *


class NewCrawler():

    def __init__(self) -> None:
        pass
    def main_start(self):
        try:
            start_crawler.StartCrawler().main()
        except Exception as e:
            pass
        
        parse_to_txt.StartParseText().main()
