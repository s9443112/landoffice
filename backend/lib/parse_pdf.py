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
            pdf.set_font("font", size=12)
            pdf.add_page()
            pdf.cell(200, 10, txt="＊＊＊　　建物標示部　　＊＊＊",
                     ln=1, align="C")
            pdf.cell(200, 10, txt=each.sheet1+" " + each.sheet2 + " " +
                     each.sheet3+"   建號 "+each.sheet4, ln=2, align="C")
            pdf.cell(200, 10, txt="登記日期:  "+each.sheet5 +
                     "     登記原因：" + each.sheet6, ln=3, align="C")
            pdf.cell(200, 10, txt="建物門牌:  " + each.sheet7, ln=4, align="C")
            pdf.cell(200, 10, txt="主要用途:  " + each.sheet8 +
                     "     主要建材:  " + each.sheet9, ln=5, align="C")
            pdf.cell(200, 10, txt="層數:  " + each.sheet10 +
                     "     總面積:  " + each.sheet11, ln=6, align="C")
            pdf.cell(200, 10, txt="層次:  " + each.sheet12 +
                     "     層次面積:  " + each.sheet13, ln=7, align="C")
            pdf.cell(200, 10, txt="建築完成日期:  " + each.sheet14, ln=8, align="C")
            pdf.cell(200, 10, txt="其他登記事項:  ", ln=9, align="C")

            currentLine = 10
            buildnumber = each.sheet15

            while 1:
                if buildnumber == '':
                    break
                pdf.cell(
                    200, 10, txt=buildnumber[:40], ln=currentLine, align="C")
                buildnumber = buildnumber[40:]
                currentLine = currentLine + 1

            Buildings = models.MarkingDepartmentDependsBuildings.objects.filter(
                markingdepartment=each)

            currentLine = currentLine+1
            pdf.cell(200, 10, txt="附屬建物:  ", ln=currentLine, align="C")
            currentLine = currentLine+1
            for idxx, eeach in enumerate(Buildings):
                pdf.cell(200, 10, txt="附屬建物用途:  " + eeach.sheet1 +
                         "     層次面積:  " + eeach.sheet2, ln=currentLine, align="C")
                currentLine = currentLine+1
            Publics = models.MarkingDepartmentPublicPart.objects.filter(markingdepartment=each)
            
            for idxx, eeach in enumerate(Publics):
                pdf.cell(200, 10, txt="共有部分:  " + eeach.sheet1 , ln=currentLine, align="C")
                currentLine = currentLine+1
                pdf.cell(200, 10, txt="權利範圍:  " + eeach.sheet2 + "    面積:  " + eeach.sheet3, ln=currentLine, align="C")
                currentLine = currentLine+1
                pdf.cell(200, 10, txt="其他登記事項:  " , ln=currentLine, align="C")
                buildnumber = each.sheet4
                while 1:
                    if buildnumber == '':
                        break
                    pdf.cell(
                        200, 10, txt=buildnumber[:40], ln=currentLine, align="C")
                    buildnumber = buildnumber[40:]
                    currentLine = currentLine + 1
                if eeach.sheet5 != None:
                    pdf.cell(200, 10, txt="含停車位:  " + eeach.sheet5 , ln=currentLine, align="C")
                    currentLine = currentLine + 1



            # Locations = models.MarkingDepartmentDependsLocationNumber.objects.filter(markingdepartment=each)

            pdf.output(os.path.join(
                './output/', '{}-{}.pdf'.format(each.sheet3, each.sheet4)), 'F')
