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
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException,TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller
import base64
import requests


class StartCrawler(object):
    def __init__(self):
        self.user_acount = "AAN14928"
        self.user_passwd = "Z1X2C3V4"
        self.output_path = "./output"
        self.user_code = ""
        if not os.path.isdir(self.output_path):
            os.mkdir(self.output_path)

        
    def get_user_acount(self):
        def pop_up(x):
            # global user_acount
            # user_acount = ent1.get()
            # global user_passwd
            # user_passwd = ent2.get()

            self.user_code = ent3.get()
            # messagebox.showinfo("Pop up", ent1.get()+", "+ent2.get()+", "+ent3.get()+", "+str(len(ent3.get())))
            top.destroy()

        def gg():
            self.user_code = ent3.get()
            top.destroy()
            
        top = Tk()
        top.title("會員登入輔助工具")
        top.bind('<Return>', pop_up)

        lbl1 = Label(top, text="Enter acount:")
        ent1 = Entry(top, bd=5)
        ent1.insert(END, self.user_acount)
        lbl1.pack(side=LEFT)
        ent1.pack(side=LEFT)

        lbl2 = Label(top, text="Enter password:")
        ent2 = Entry(top, bd=5, show='*')
        ent2.insert(END, self.user_passwd)
        lbl2.pack(side=LEFT)
        ent2.pack(side=LEFT)

        lbl3 = Label(top, text="Enter code:")
        ent3 = Entry(top, bd=5)
        lbl3.pack(side=LEFT)
        ent3.pack(side=LEFT)

        
        button_pop = Button(top, text="登入", command=gg)
        button_pop.pack(side=RIGHT)
        top.mainloop()

    def click_popup_window(self):
        try:
            alert = self.chrome.switch_to.alert
            alert.accept()
            return True
        except NoAlertPresentException:
            
            print("沒有彈跳視窗")
            return False

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

        
        chromedriver_autoinstaller.install()
    
        options = Options()
        options.add_argument("--disable-notifications")
        # self.chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.chrome = webdriver.Chrome(chrome_options=options)
        # for 10 sec
        self.chrome.implicitly_wait(10)
        return self.chrome
        # return False
        # time.sleep(20)

    

    def main(self):
        if not os.path.isdir(self.output_path):
            os.mkdir(self.output_path)
        
        try:
            root = Tk()
            root.withdraw()
            excel_path = filedialog.askopenfilename()
            print(excel_path)
            root.destroy()

            wb = load_workbook(excel_path)
            sheet = wb['工作表1']
            col = 2

        except Exception as e:
            return 'break'
        


        self.chrome = self.create_chrome()

        


        self.chrome.maximize_window()
        self.chrome.execute_script("javascript:document.body.style.zoom='80%'")
        # self.chrome.execute_script("window.resizeTo(2560,1440)")

        self.chrome.get("https://ttt.land.net.tw/APTCLN/Home.htm")
        self.write_log("Start.")
        # time.sleep(3)
        email = self.chrome.find_element_by_name("username")
        password = self.chrome.find_element_by_name("password")
        inputCode = self.chrome.find_element_by_name("validateCode")
        self.chrome.execute_script("javascript:document.body.style.zoom='80%'")
        self.get_user_acount()

        self.write_log("Got user acount.")

        email.send_keys(self.user_acount)
        password.send_keys(self.user_passwd)
        inputCode.send_keys(self.user_code)

        
        inputCode.submit()
        self.write_log("Send user acount.")

        self.click_popup_window()

        self.click_popup_window()

        
        while True:
            # chrome.refresh()
            self.chrome.get("http://ttt.land.net.tw/APTCLN/Login.htm?service=https://tradevan.land.net.tw/NEW_PTT_WEB/TTTLogin.servlet")
            colQ = sheet['Q'+str(col)]
            time.sleep(3)
            if colQ.value == None:
                break
             
            txts = colQ.value.split("\n")
            landNumber_txt = txts[3][:5]
             
            index = 0
            for i in range(len(txts[1])):
                if txts[1][i].isdigit():
                    index = i
                    break

            landSection_txt = txts[1][index:index+4]
             
            col+=1

            output_path_tmp = os.path.join(self.output_path, landSection_txt+"_"+landNumber_txt)
            if not os.path.isdir(output_path_tmp):
                os.mkdir(output_path_tmp)
            self.write_log("Create output folder.")


            def Start_Search():

                try:
                
                    while True:
                        landSection = self.find_element_by_name("sectioncode")

                        if landSection != []:
                            landSection.send_keys('')
                            # print(landSection_txt)
                            landSection.send_keys(landSection_txt)
                            self.write_log("送地段["+landSection_txt+"].")
                            break
                        else:
                            time.sleep(1)
                    
                    
                    #get radio buttom
                    self.chrome.find_element_by_css_selector("input#RBUILD").click()

                    select = self.find_element_by_name("projectB")
                    if select != []:
                        select = Select(select)
                        select.select_by_index(0)

                    while True:
                    
                        landNumber = self.find_element_by_name("search2")
                        if landNumber != []:
                            landNumber.send_keys(Keys.CONTROL + "a")
                            time.sleep(0.5)
                            landNumber.send_keys(Keys.DELETE)
                            time.sleep(0.5)
                            landNumber.send_keys(landNumber_txt)
                            self.write_log("送建號["+landNumber_txt+"].")
                            break
                        else:
                            time.sleep(1)
                    
                    self.chrome.execute_script("javascript:landQuery()")
                    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'right'))
                    WebDriverWait(self.chrome, 10).until(element_present)

                except Exception as e:
                    print(e)
                    print("系統壞掉 開始執行.... 等待5秒鐘再次執行")
                    self.write_log("系統壞掉 開始執行.... 等待5秒鐘再次執行")
                    
                    time.sleep(5)
                    Start_Search()


            Start_Search()


             
            self.write_log("執行查詢.")

            # time.sleep(5)

            owners = self.find_element_by_class("owner_folder")
             
            while owners == []:
                self.write_log("所有權部找不到人，從新搜尋.")
                owners = self.find_element_by_class("owner_folder")
                # if owners != None:
                #     write_log("所有權部有[" + str(len(owners)-1) + "]人." )
                #     time.sleep(3)

            self.write_log("所有權部有[" + str(len(owners)-1) + "]人." )

            # print("owner number:" + str(len(owners)-1))
            self.querys = []
            def SaveOwn():
                # global querys
                try:
                    
                    for index, owner in enumerate(owners):
                        if index == 0:
                            self.write_log("儲存標示部網頁.")

                            #get window size
                            s = self.chrome.get_window_size()
                            #obtain browser height and width
                            w = self.chrome.execute_script('return document.body.parentNode.scrollWidth')
                            h = self.chrome.execute_script('return document.body.parentNode.scrollHeight')
                            #set to new window size
                            self.chrome.set_window_size(w, h)
                            
                            
                            
                            el = self.chrome.find_element_by_tag_name('body')
                            self.chrome.execute_script("javascript:document.body.style.zoom='80%'")
                            time.sleep(1)
                            el.screenshot("{}/標示部.jpg".format(output_path_tmp))
                            self.chrome.set_window_size(s['width'], s['height'])

                            

                            with open( os.path.join(output_path_tmp, '標示部.html') , 'w', encoding="utf-8") as f:
                                f.write(self.chrome.page_source)
                            # time.sleep(2)
                            continue
                        
                        innerHTMLTxt = owner.get_attribute("innerHTML")
                        self.write_log("調閱所有權部人element.")
                        txt_start = innerHTMLTxt.find("\"") + 1
                        txt_end = innerHTMLTxt[txt_start+1:].find("\"") + txt_start + 1
                        
                        queryTxt = innerHTMLTxt[txt_start:txt_end]
                        self.querys.append(queryTxt)
                except Exception as e:
                    print(e)
                    print("系統壞掉 標示部.... 等待5秒鐘再次執行")
                    self.write_log("系統壞掉 標示部.... 等待5秒鐘再次執行")
                    self.querys = []
                    time.sleep(5)
                    SaveOwn()

            SaveOwn()
             
            print("========")
            print(self.querys)
            print("========")
            for index, query in enumerate(self.querys):
                self.write_log("執行所有權部人之query.")
                if query == "":
                    break

                def Start_Owner():

                    try:
                    
                        self.chrome.refresh()
                        print("========")
                        print(query)
                        print(len(query))
                        print("========")
                        self.chrome.execute_script("javascript:"+query)
                        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'right'))
                        WebDriverWait(self.chrome, 10).until(element_present)

                    except Exception as e:
                        print("系統壞掉 所有權部.... 等待5秒鐘再次執行")
                        self.write_log("系統壞掉 所有權部.... 等待5秒鐘再次執行")
                        time.sleep(5)
                        Start_Owner()

                Start_Owner()

                self.write_log("儲存所有權部人網頁.")
                #get window size
                s = self.chrome.get_window_size()
                #obtain browser height and width
                w = self.chrome.execute_script('return document.body.parentNode.scrollWidth')
                h = self.chrome.execute_script('return document.body.parentNode.scrollHeight')
                #set to new window size
                self.chrome.set_window_size(w, h)
                el = self.chrome.find_element_by_tag_name('body')
                self.chrome.execute_script("javascript:document.body.style.zoom='80%'")
                time.sleep(1)
                # el.screenshot("{}/owner_{}_page.jpg".format(output_path_tmp,str(index+1)))
                el.screenshot("{}/所有權部_{}.jpg".format(output_path_tmp,str(index+1)))
                self.chrome.set_window_size(s['width'], s['height'])
                with open( os.path.join(output_path_tmp, "owner_"+str(index+1)+'_page.html') , 'w', encoding="utf-8") as f:
                    f.write(self.chrome.page_source)




            # time.sleep(3)
            self.write_log("搜尋他項權利部.")
             
             
            owners = self.find_element_by_class("other_folder")

            # print("other number:" + str(len(owners)-1))
            self.write_log("他項權利部[" + str(len(owners)-1) +"]人")
             
            self.querys = []
            for index, owner in enumerate(owners):
                if index == 0:
                    continue
                self.write_log("搜尋他項權利部query.")
                innerHTMLTxt = owner.get_attribute("innerHTML")
                txt_start = innerHTMLTxt.find("\"") + 1
                txt_end = innerHTMLTxt[txt_start+1:].find("\"") + txt_start + 1
                
                queryTxt = innerHTMLTxt[txt_start:txt_end]
                self.querys.append(queryTxt)

            for index, query in enumerate(self.querys):
                self.write_log("執行他項權利部query.")
                
                if query == "":
                    break

                def Start_Other():
                    try:
    
                        self.chrome.refresh()
                        self.chrome.execute_script("javascript:"+query)
                        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'right'))
                        WebDriverWait(self.chrome, 10).until(element_present)

                    except Exception as e:
                        print("系統壞掉 他項權利部.... 等待5秒鐘再次執行")
                        self.write_log("系統壞掉 他項權利部.... 等待5秒鐘再次執行")
                        time.sleep(5)
                        Start_Other()
                Start_Other()


                # clicked = click_popup_window()


                self.write_log("儲存他項權利部網頁.")
                # time.sleep(5)
                #get window size
                s = self.chrome.get_window_size()
                #obtain browser height and width
                w = self.chrome.execute_script('return document.body.parentNode.scrollWidth')
                h = self.chrome.execute_script('return document.body.parentNode.scrollHeight')
                #set to new window size
                self.chrome.set_window_size(w, h)

                el = self.chrome.find_element_by_tag_name('body')
                self.chrome.execute_script("javascript:document.body.style.zoom='80%'")
                time.sleep(1)
                # el.screenshot("{}/other_{}_page.jpg".format(output_path_tmp,str(index+1)))
                el.screenshot("{}/權力部_{}.jpg".format(output_path_tmp,str(index+1)))
                self.chrome.set_window_size(s['width'], s['height'])
                with open( os.path.join(output_path_tmp, "other_"+str(index+1)+'_page.html') , 'w', encoding="utf-8") as f:
                    f.write(self.chrome.page_source)

        return True