from fpdf import FPDF
from backend import models
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
            pdf.set_text_color(0,0,255)
            pdf.set_font("font", size=12)
            pdf.add_page()
            pdf.cell(200, 8, txt="＊＊＊　　建物標示部　　＊＊＊",
                     ln=1, align="C")
            pdf.cell(200, 8, txt=each.sheet1+" " + each.sheet2 + " " +
                     each.sheet3+"   建號 "+each.sheet4, ln=2, align="C")

            pdf.cell(200, 8, txt="登記日期:  "+each.sheet5+ "        登記原因：" + each.sheet6, ln=3, align="L")

            pdf.cell(200, 8, txt="建物門牌:  " + each.sheet7, ln=4, align="L")

            currentLine = 5
            Locations = models.MarkingDepartmentDependsLocationNumber.objects.filter(markingdepartment=each)
            for idxx, eeach in enumerate(Locations):
                pdf.cell(200, 8, txt="建物坐落地號:  " + eeach.sheet1 ,ln=currentLine, align="L")
                currentLine = currentLine+1

            pdf.cell(200, 8, txt="主要用途:  " + each.sheet8 + "    主要建材:  " + each.sheet9 , ln=currentLine, align="L")
           
            currentLine = currentLine+1

            pdf.cell(200, 8, txt="層數:  " + each.sheet10+ "       總面積:  " + each.sheet11,ln=currentLine, align="L")
            currentLine = currentLine+1

            new_floor = each.sheet12.split(',')
            new_floor2 = each.sheet13.split(',')
            for idxx, eeach in enumerate(new_floor):
                pdf.cell(200, 8, txt="層次:  " + new_floor[idxx] + "     層次面積:  " + new_floor2[idxx], ln=currentLine, align="L")


            # pdf.cell(200, 8, txt="層次:  " + each.sheet12 + "     層次面積:  " + each.sheet13, ln=currentLine, align="L")
            currentLine = currentLine+1
            pdf.cell(200, 8, txt="建築完成日期:  " + each.sheet14, ln=currentLine, align="L")
            currentLine = currentLine+1
            Buildings = models.MarkingDepartmentDependsBuildings.objects.filter(
                markingdepartment=each)

            for idxx, eeach in enumerate(Buildings):
                pdf.cell(200, 8, txt="附屬建物用途:  " + eeach.sheet1 +
                         "     層次面積:  " + eeach.sheet2, ln=currentLine, align="L")
                currentLine = currentLine+1

            Publics = models.MarkingDepartmentPublicPart.objects.filter(markingdepartment=each)
            
            for idxx, eeach in enumerate(Publics):
                pdf.set_font("font", size=10)
                pdf.cell(120, 7, txt="共有部分:  " + eeach.sheet1 , ln=currentLine, align="L",border=1)
                currentLine = currentLine+1
                pdf.cell(200, 5, txt="權利範圍:  " + eeach.sheet2 + "    面積:  " + eeach.sheet3, ln=currentLine, align="L")
                currentLine = currentLine+1
                pdf.cell(200, 5, txt="其他登記事項:  " , ln=currentLine, align="L")
                buildnumber = eeach.sheet4
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(
                        0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1
                if eeach.sheet5 != None:
                    pdf.cell(200, 5, txt="含停車位:  " + eeach.sheet5 , ln=currentLine, align="L")
                    currentLine = currentLine + 1

            pdf.set_font("font", size=12)
            pdf.cell(200, 8, txt="其他登記事項:  ", ln=9, align="L")

            currentLine = currentLine+1
            buildnumber = each.sheet15
            pdf.set_font("font", size=10)

            while 1:
                if buildnumber == '':
                    break
                pdf.cell(
                    120, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                buildnumber = buildnumber[55:]
                currentLine = currentLine + 1


            pdf.add_font('font', "", "kaiu.ttf", True)
            pdf.set_font("font", size=12)
            
            
           
            
            OwnershipDepartments = models.OwnershipDepartment.objects.filter(markingdepartment=each)

            for idxx, eeach in enumerate(OwnershipDepartments):
                pdf.add_page()
                currentLine = 1 
                pdf.cell(200, 8, txt="＊＊＊　　建物所有權部　　＊＊＊",ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt=eeach.sheet1+" " + eeach.sheet2 + " " +
                     eeach.sheet3+"   建號 "+eeach.sheet4, ln=currentLine, align="C")
                
                pdf.cell(200, 8, txt="登記次序:  " + eeach.sheet5, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記日期:  " + eeach.sheet6 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="登記原因:  " + eeach.sheet7 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="原因發生日期:  " + eeach.sheet8 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="所有權人姓名:  " + eeach.sheet9 , ln=currentLine, align="L")
                pdf.cell(200, 8, txt="統一編號:  " + eeach.sheet10, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="住址:  " + eeach.sheet11, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權利範圍:  " + eeach.sheet12, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權狀字號:  " + eeach.sheet13, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="相關他項登記次序:  " + eeach.sheet14, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="其他登記事項:  " + eeach.sheet15, ln=currentLine, align="L")

               


            OtherShipDepartments = models.OtherShipDepartment.objects.filter(markingdepartment=each)

            for idxx, eeach in enumerate(OtherShipDepartments):
                pdf.add_page()
                currentLine = 1 
                pdf.cell(200, 8, txt="＊＊＊　　建物他項權利部　　＊＊＊",ln=currentLine, align="C")
                
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
                pdf.cell(200, 8, txt="擔保債權確定期日:  " + eeach.sheet16, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="存續期間:  " + eeach.sheet17, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="清償日期:  " + eeach.sheet18, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="利息(率)或地租:  " + eeach.sheet19, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="遲延利息(率):  " + eeach.sheet20, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="違約金:  " + eeach.sheet21, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="權利標的:  " + eeach.sheet22, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="標的登記次序:  " + eeach.sheet23, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="設定權利範圍:  " + eeach.sheet24, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="證明書字號:  " + eeach.sheet25, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="共同擔保地號:  " + eeach.sheet26, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="共同擔保建號:  " + eeach.sheet27, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="其他登記事項:  " + eeach.sheet28, ln=currentLine, align="L")
                pdf.cell(200, 8, txt="擔保債權種類及範圍:  " , ln=currentLine, align="L")


                buildnumber = eeach.sheet29
                pdf.set_font("font", size=10)
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(0, 5, txt=buildnumber[:55], ln=currentLine, align="L")
                    buildnumber = buildnumber[55:]
                    currentLine = currentLine + 1
                

            pdf.output(os.path.join(
                './output/', '{}-{}.pdf'.format(each.sheet3, each.sheet4)), 'F')
        
        