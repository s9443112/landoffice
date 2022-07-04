from fpdf import FPDF
from backend_land import models
import os


class StartParsePdf():
    def __init__(self):
        self.ouput_path = "./output"
        self.fileName = ''

    def main(self):
        MarkingDepartments = models.MarkingDepartment.objects.all()

        for idx, each in enumerate(MarkingDepartments):
            pdf = FPDF()
            pdf.add_font('font', "", "kaiu.ttf", True)
            pdf.set_font("font", size=12)
            pdf.add_page()
            pdf.cell(200, 8, txt="＊＊＊　　土地標示部　　＊＊＊",
                     ln=1, align="C")
            pdf.cell(200, 8, txt=each.sheet1+" " + each.sheet2 + " " +
                     each.sheet3+"   地號 "+each.sheet4, ln=2, align="C")

            pdf.cell(200, 8, txt="登記日期:  "+each.sheet5+ "        登記原因：" + each.sheet6, ln=3, align="L")

            pdf.cell(200, 8, txt="面積:  " + each.sheet7, ln=4, align="L")
            pdf.cell(200, 8, txt="使用分區:  " + each.sheet8, ln=4, align="L")
            pdf.cell(200, 8, txt="使用地類別:  " + each.sheet9, ln=4, align="L")
            pdf.cell(200, 8, txt="公告現值年月:  " + each.sheet10, ln=4, align="L")
            pdf.cell(200, 8, txt="公告土地現值:  " + each.sheet11, ln=4, align="L")
            pdf.cell(200, 8, txt="公告地價年月:  " + each.sheet12, ln=4, align="L")
            pdf.cell(200, 8, txt="公告地價:  " + each.sheet13, ln=4, align="L")
            pdf.cell(200, 8, txt="地上建物建號:  " + each.sheet14, ln=4, align="L")
            pdf.cell(200, 8, txt="其他登記事項:  " + each.sheet15, ln=4, align="L")
            pdf.cell(200, 8, txt="地價備註事項:  " + each.sheet16, ln=4, align="L")


            OwnershipDepartments = models.OwnershipDepartment.objects.filter(markingdepartment=each)

            for idxx, eeach in enumerate(OwnershipDepartments):
                pdf.add_page()
                currentLine = 1 
                pdf.cell(200, 8, txt="＊＊＊　　土地所有權部　　＊＊＊",ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt=eeach.sheet1+" " + eeach.sheet2 + " " +
                     eeach.sheet3+"   建號 "+eeach.sheet4, ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt="登記次序:  " + eeach.sheet5, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記日期:  " + eeach.sheet6 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記原因:  " + eeach.sheet7 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="原因發生日期:  " + eeach.sheet8 , ln=currentLine, align="L")
                
                pdf.cell(200, 8, txt="所有權人姓名:  " + eeach.sheet9 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="統一編號:  " + eeach.sheet10, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="住址:  " + eeach.sheet11, ln=currentLine, align="L")

                pdf.cell(200, 8, txt="相關他項登記次序:  ", ln=currentLine, align="L")
                buildnumber = eeach.sheet12
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1
                pdf.set_font("font", size=12)
                pdf.cell(200, 8, txt="權利範圍:  " + eeach.sheet13, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權狀字號:  " + eeach.sheet14, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="當期申報地價年月:  " + eeach.sheet15, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="當期申報地價:  " + eeach.sheet16, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="其他登記事項:  ", ln=currentLine, align="L")

                buildnumber = eeach.sheet17
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1

                pdf.set_font("font", size=12)
                pdf.cell(200, 8, txt="地價備註事項:  " + eeach.sheet18, ln=currentLine, align="L")

                OwnershipDepartmentHistorys = models.OwnershipDepartmentHistory.objects.filter(ownershipdepartment=eeach)

                for idxxx, eeeach in enumerate(OwnershipDepartmentHistorys):
                    pdf.cell(200, 8, txt="年月:  " + eeeach.sheet1 ,ln=currentLine, align="L")
                    currentLine = currentLine+1
                    pdf.cell(200, 8, txt="地價:  " + eeeach.sheet2 ,ln=currentLine, align="L")
                    currentLine = currentLine+1
                    pdf.cell(200, 8, txt="歷次取得權利範圍:  " + eeeach.sheet3 ,ln=currentLine, align="L")
                    currentLine = currentLine+1




            OtherShipDepartments = models.OtherShipDepartment.objects.filter(markingdepartment=each)

            for idxx, eeach in enumerate(OtherShipDepartments):
                pdf.add_page()
                currentLine = 1 
                pdf.cell(200, 8, txt="＊＊＊　　土地他項權利部　　＊＊＊",ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt=eeach.sheet1+" " + eeach.sheet2 + " " +
                     eeach.sheet3+"   建號 "+eeach.sheet4, ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt="登記次序:  " + eeach.sheet5, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權利種類:  " + eeach.sheet6 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="收件年期:  " + eeach.sheet7 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="收件字號:  " + eeach.sheet8 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記日期:  " + eeach.sheet9 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記原因:  " + eeach.sheet10, ln=currentLine, align="L")
                
                pdf.cell(200, 8, txt="權利人姓名:  " + eeach.sheet11, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權利人統一編號:  " + eeach.sheet12, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="住址:  " + eeach.sheet13, ln=currentLine, align="L")
                
                pdf.cell(200, 8, txt="債權額比例:  " + eeach.sheet14, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="擔保債權總金額:  " + eeach.sheet15, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="擔保債權種類及範圍:  ", ln=currentLine, align="L")

                buildnumber = eeach.sheet16
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1
                    
                pdf.set_font("font", size=12)


                pdf.cell(200, 8, txt="擔保債權確定期日:  " + eeach.sheet17, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="清償日期:  " + eeach.sheet18, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="利息(率)或地租:  " + eeach.sheet19, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="遲延利息(率):  " + eeach.sheet20, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="違約金:  " + eeach.sheet21, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="其他擔保範圍約定:  ", ln=currentLine, align="L")

                buildnumber = eeach.sheet22
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1
                    
                pdf.set_font("font", size=12)

                pdf.cell(200, 8, txt="權利標的:  " + eeach.sheet23, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="標的登記次序:  " + eeach.sheet24, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="設定權利範圍:  " + eeach.sheet25, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="證明書字號:  " + eeach.sheet26, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="共同擔保地號:  " + eeach.sheet27, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="共同擔保建號:  " + eeach.sheet28, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="其他登記事項:  ", ln=currentLine, align="L")
                


                buildnumber = eeach.sheet29
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1

                pdf.set_font("font", size=12)    
                

            pdf.output(os.path.join(
                './output_land/', '{}-{}.pdf'.format(each.sheet3, each.sheet4)), 'F')
        
        