import backend.lib.crawler as start_crawler
import backend.lib.parse_text as parse_to_txt

# from tkinter import *


class NewCrawler():

    def __init__(self) -> None:
        pass
    def main_start(self):
        start_crawler.StartCrawler().main()
        parse_to_txt.StartParseText().main()
