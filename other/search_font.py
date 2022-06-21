from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *
from tkinter import messagebox
from selenium.webdriver.support.ui import Select
import msvcrt
from selenium.webdriver.common.action_chains import ActionChains
import os
from datetime import datetime
from openpyxl import load_workbook
from tkinter import filedialog
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchFont(object):
    def __init__(self,font: str,):
        self.output_path = "./output"
        self.font= font



    def write_log(self,txt):
        with open('log.txt', 'a', encoding="utf-8") as f:
            now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(now_time+" ")
            f.write(txt + '\n')

    def find_element_by_name(self,str):
        try:
            element = self.chrome.find_element_by_name(str)
            return element
        except NoSuchElementException:
            return []

    def find_element_by_class(self,str):
        try:
            element = self.chrome.find_elements_by_class_name(str)
            return element
        except NoSuchElementException:
            return []



    def create_chrome(self):

        
        # chromedriver_autoinstaller.install()
        

        options = Options()
        
        options.add_argument("--disable-notifications")
        self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        # self.chrome = webdriver.Chrome(chrome_options=options)
        # for 10 sec
        self.chrome.implicitly_wait(10)
        return self.chrome
        # return False
        # time.sleep(20)
    def main(self):
        self.chrome = self.create_chrome()
        self.chrome.get("https://www.cns11643.gov.tw/searchQ.jsp?SN={}".format(self.font))
        self.write_log("Start search font {}.".format(self.font))
        el = self.chrome.find_element_by_tag_name('body')
        el.screenshot("{}/{}.jpg".format(self.output_path,self.font))
        result = self.chrome.find_element_by_xpath("//meta[@property='og:description']").get_attribute("content")
        print(result)
        return result[6]