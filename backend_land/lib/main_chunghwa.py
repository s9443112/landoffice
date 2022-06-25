import backend_land.lib.crawler_chunghwa as start_crawler
import backend_land.lib.parse_text_land as parse_to_txt

# from tkinter import *


class NewCrawler():

    def __init__(self) -> None:
        pass
    def main_start(self):
        try:
            start_crawler.StartLandCrawler().main()
        except Exception as e:
            pass
        
        parse_to_txt.StartParseText().main()
