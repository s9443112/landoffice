from fpdf import FPDF
from os import listdir
from os.path import isfile, isdir, join






class StartParsePDF():
    def __init__(self):
        self.ouput_path = "./output"
        self.fileName= ""

    def find_context(self,target):
        
        target = "["+target+"]"
        f = open(self.fileName, encoding="utf-8")
        text = f.read()
        f.close
        index = text.find(target) + len(target)
        text_ = text[index:]
        index2 = text_.find("[")
        if index2 == -1:
            return text[index+1:]
        return text[index+1:index2+index-1]



    def main(self):
        folders = listdir(self.ouput_path)
        for folder in folders:
            folder_fullpath = join(self.ouput_path, folder)
            if isdir(folder_fullpath):

                pdf = FPDF()
                pdf.add_font('font',"","kaiu.ttf",True)
                pdf.set_font("font", size=12)

                files = listdir(folder_fullpath)
                for file in files:
                    file_fullpath = join(folder_fullpath, file)
                    if isfile(file_fullpath):
                        print("檔案：", file)
                        if file == "標示部.txt":

                            pdf.add_page()
                            pdf.cell(200, 10, txt="＊＊＊　　建物標示部　　＊＊＊", ln=1, align="C")
                            self.fileName = file_fullpath

                            city = self.find_context("縣市")
                            town = self.find_context("鄉鎮市區")
                            section = self.find_context("地段")
                            buildnumber = self.find_context("建號")
                            pdf.cell(200, 10, txt=city+" " + town + " " +section+"   建號 "+buildnumber, ln=2, align="C")

                            date = self.find_context("登記日期")
                            reason = self.find_context("登記原因")
                            pdf.cell(200, 10, txt="登記日期:  "+date+"     登記原因：" + reason, ln=3, align="C")

                            txt = self.find_context("建物門牌")
                            print("建物門牌")
                            print(file_fullpath)
                            print(txt)
                            pdf.cell(200, 10, txt="建物門牌:  "+txt, ln=4, align="C")

                            txt = self.find_context("建物坐落地號")
                            pdf.cell(200, 10, txt="建物坐落地號"+" "*40, ln=5, align="C")
                            pdf.cell(200, 10, txt=txt, ln=6, align="C")

                            usefor = self.find_context("主要用途")
                            element = self.find_context("主要建材")
                            pdf.cell(200, 10, txt="主要用途: "+usefor+"   主要建材: "+element, ln=7, align="C")

                            usefor = self.find_context("層數")
                            element = self.find_context("總面積")
                            pdf.cell(200, 10, txt="層數: "+usefor+"   總面積: "+element, ln=8, align="C")

                            usefor = self.find_context("層次")
                            element = self.find_context("層次面積")
                            pdf.cell(200, 10, txt="層次: "+usefor+"   層次面積: "+element, ln=9, align="C")

                            element = self.find_context("建築完成日期")
                            pdf.cell(200, 10, txt="建築完成日期: "+element, ln=10, align="C")

                            usefor = self.find_context("附屬建物用途")
                            element = self.find_context("面積")
                            pdf.cell(200, 10, txt="附屬建物用途: "+usefor+"   面積: "+element, ln=11, align="C")

                            buildnumber = self.find_context("其他登記事項")
                            pdf.cell(200, 10, txt="其他登記事項:", ln=12, align="C")

                            
                            
                        
                            currentLine = 13
                            length = len(buildnumber)//30
                            for i in range(length):
                                pdf.cell(200, 10, txt=buildnumber[:30], ln=currentLine, align="C")
                                currentLine+=1
                                buildnumber = buildnumber[30:]
                            pdf.cell(200, 10, txt=buildnumber, ln=currentLine, align="C")


                        
                        elif file[:5] == "owner" and file[-3:] == "txt":
                            
                            pdf.add_page()
                            pdf.cell(200, 10, txt="＊＊＊　　建物所有權部　　＊＊＊", ln=1, align="C")
                            # global fileName
                            self.fileName = file_fullpath

                            city = self.find_context("縣市名稱")
                            town = self.find_context("鄉鎮市區")
                            section = self.find_context("地段")
                            buildnumber = self.find_context("建號")
                            pdf.cell(200, 10, txt=city+" " + town + " " +section+"   建號 "+buildnumber, ln=2, align="C")

                            buildnumber = self.find_context("登記次序")
                            pdf.cell(200, 10, txt="登記次序:  "+buildnumber, ln=3, align="C")

                            date = self.find_context("登記日期")
                            reason = self.find_context("登記原因")
                            pdf.cell(200, 10, txt="登記日期:  "+date+"     登記原因：" + reason, ln=4, align="C")

                            buildnumber = self.find_context("原因發生日期")
                            pdf.cell(200, 10, txt="原因發生日期:  "+buildnumber, ln=5, align="C")

                            buildnumber = self.find_context("所有權人姓名")
                            pdf.cell(200, 10, txt="所有權人姓名:  "+buildnumber, ln=6, align="C")

                            buildnumber = self.find_context("統一編號")
                            pdf.cell(200, 10, txt="統一編號:  "+buildnumber, ln=7, align="C")

                            buildnumber = self.find_context("住址")
                            pdf.cell(200, 10, txt="住址:  "+buildnumber, ln=8, align="C")

                            buildnumber = self.find_context("權利範圍")
                            pdf.cell(200, 10, txt="權利範圍:  "+buildnumber, ln=9, align="C")

                            buildnumber = self.find_context("權狀字號")
                            pdf.cell(200, 10, txt="權狀字號:  "+buildnumber, ln=10, align="C")


                            buildnumber = self.find_context("其他登記事項")
                            pdf.cell(200, 10, txt="其他登記事項: ", ln=11, align="C")

                            currentLine = 12
                            length = len(buildnumber)//30
                            for i in range(length):
                                pdf.cell(200, 10, txt=buildnumber[:30], ln=currentLine, align="C")
                                currentLine+=1
                                buildnumber = buildnumber[30:]
                            pdf.cell(200, 10, txt=buildnumber, ln=currentLine, align="C")



                        elif file[:5] == "other" and file[-3:] == "txt":

                            pdf.add_page()
                            pdf.cell(200, 10, txt="＊＊＊　　建物他項權利部　　＊＊＊", ln=1, align="C")
                            # global fileName
                            self.fileName = file_fullpath

                            city = self.find_context("縣市名稱")
                            town = self.find_context("鄉鎮市區")
                            section = self.find_context("段號")
                            buildnumber = self.find_context("建號")
                            pdf.cell(200, 10, txt=city+" " + town + " " +section+"   建號 "+buildnumber, ln=2, align="C")

                            buildnumber = self.find_context("登記次序")
                            buildnumber1 = self.find_context("權利種類")
                            pdf.cell(200, 10, txt="登記次序:  "+buildnumber+"   權利種類: "+buildnumber1, ln=3, align="C")

                            date = self.find_context("收件年期")
                            reason = self.find_context("收件字號")
                            pdf.cell(200, 10, txt="收件年期:  "+date+"     收件字號：" + reason, ln=4, align="C")

                            buildnumber = self.find_context("登記日期")
                            buildnumber1 = self.find_context("登記原因")
                            pdf.cell(200, 10, txt="登記日期:  "+buildnumber+"     登記原因: "+buildnumber1, ln=5, align="C")

                            buildnumber = self.find_context("權利人姓名")
                            pdf.cell(200, 10, txt="權利人姓名:  "+buildnumber, ln=6, align="C")

                            buildnumber = self.find_context("權利人統一編號")
                            pdf.cell(200, 10, txt="權利人統一編號:  "+buildnumber, ln=7, align="C")

                            buildnumber = self.find_context("住址")
                            pdf.cell(200, 10, txt="住址:  "+buildnumber, ln=8, align="C")

                            buildnumber = self.find_context("債權額比例")
                            buildnumber1 = self.find_context("擔保債權總金額")
                            pdf.cell(200, 10, txt="債權額比例:  "+buildnumber+"     擔保債權總金額: "+buildnumber1, ln=9, align="C")


                            pdf.cell(200, 10, txt="擔保債權種類及範圍:  ", ln=10, align="C")
                            currentLine = 11
                            buildnumber = self.find_context("擔保債權種類及範圍")
                            length = len(buildnumber)//30
                            for i in range(length):
                                pdf.cell(200, 10, txt=buildnumber[:30], ln=currentLine, align="C")
                                currentLine+=1
                                buildnumber = buildnumber[30:]
                            pdf.cell(200, 10, txt=buildnumber, ln=currentLine, align="C")
                            currentLine+=1

                            buildnumber = self.find_context("擔保債權確定期日")
                            buildnumber1 = self.find_context("清償日期")
                            pdf.cell(200, 10, txt="擔保債權確定期日:  "+buildnumber+"    清償日期: "+buildnumber1, ln=currentLine, align="C")
                            currentLine+=1

                            buildnumber = self.find_context("利息(率)或地租")
                            buildnumber1 = self.find_context("違約金")
                            pdf.cell(200, 10, txt="利息(率)或地租:  "+buildnumber+"    違約金: "+buildnumber1, ln=currentLine, align="C")
                            currentLine+=1

                            element = self.find_context("其他擔保範圍約定")
                            lines = element.split("。")
                            pdf.cell(200, 10, txt="其他擔保範圍約定: ", ln=currentLine, align="C")
                            currentLine+=1
                            for index, line in enumerate(lines):
                                pdf.cell(200, 10, txt=line, ln=currentLine+index, align="C")

                pdf.output(join(folder_fullpath, '輸出_{}.pdf'.format(folder)) , 'F')