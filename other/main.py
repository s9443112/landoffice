import pa as start_crawler
import parse_to_txt as parse_to_txt
import parse_txt_pdf as parse_txt_pdf
import parse_txt_pdf as parse_txt_pdf
import parse_txt_excel as parse_txt_excel
from tkinter import *




def pop_up_to_do():

    def pop_up():
        top.destroy()

    toper.destroy()
    parse_to_txt.StartParseText().main()
    # parse_txt_pdf.StartParsePDF().main()
    parse_txt_excel.StartParseExcel().main()
    # top = Tk()
    # top.title("爬蟲成功")
    # lbl1 = Label(top, text="已完成程式，請開啟output資料夾查看內容")
    # lbl1.pack(side=LEFT)

    # button_pop = Button(top, text="結束", command=pop_up)
    # button_pop.pack(side=RIGHT)

    # top.mainloop()
    

def pop_up_default():

    def pop_up():
        top.destroy()

    toper.destroy()
    start_crawler.StartCrawler().main()
    # parse_to_txt.StartParseText().main()
    # parse_txt_pdf.StartParsePDF().main()
    parse_txt_excel.StartParseExcel().main()
    top = Tk()
    top.title("爬蟲成功")
    lbl1 = Label(top, text="已完成程式，請開啟output資料夾查看內容")
    lbl1.pack(side=LEFT)

    button_pop = Button(top, text="結束", command=pop_up)
    button_pop.pack(side=RIGHT)

    top.mainloop()

toper = Tk()
toper.title("請選擇功能")
toper.geometry('600x480')

button_pop = Button(toper, text="完整爬蟲程式", command=pop_up_default)
button_pop.pack(side=LEFT)
button_pop = Button(toper, text="執行解析文字程式", command=pop_up_to_do)
button_pop.pack(side=RIGHT)

toper.mainloop()


# start_crawler.StartCrawler().main()



