
from cgitb import lookup
from os import listdir
from os.path import isfile, isdir, join
import time
from bs4 import BeautifulSoup
from backend import models
from django.forms.models import model_to_dict
from datetime import datetime


class StartParseText():
    def __init__(self,):
        self.ouput_path = "./output"

        # -*- coding: utf-8 -*-
    def lookup(self, target):
        f = open('bi5_table.txt', encoding="utf-8")
        for line in f.readlines():
            if line.find(target) != -1:
                return line[5: len(line)-1]
        f.close
        return None

    def find_address(self, target_tmp, line):
        address = ""
        index = line.find(target_tmp)
        tmp_line = line[index+len(target_tmp):]

        index = tmp_line.find("<img")
        tmp_line = tmp_line[index:]

        index = tmp_line.find("</td></tr><tr>")
        tmp_line = tmp_line[:index-6]

        tmp_line = tmp_line.split(".png")
        # print(tmp_line)
        for tmp in tmp_line:
            # print(tmp)
            number = tmp[-4:]
            # print(number)
            if number[0] == "1":
                number = "B"+number[1:]
            elif number[0] == "2":
                number = "A"+number[1:]
            elif number[0] == "4":
                number = "C"+number[1:]

            char = self.lookup(number)

            if char != None:
                address = address+char
            else:
                # print(number)
                # new_font = search_font.SearchFont(font=number).main()
                # print(new_font)
                address = address + "'{}'".format(number)
                # f = open('bi5_table.txt','a', encoding="utf-8")
                # f.write("{} LOST\n".format(number))
                # f.close()
            # print(address)
        return address

    def find_target_context_may_include_img(self, target_tmp, line):
        target_tmp2 = ">"
        target_tmp3 = "<"
        index = line.find(target_tmp)
        while line[index-1] != ">":
            line = line[index+len(target_tmp):]
            index = line.find(target_tmp)

        result = ""
        tmp_line = line[index+len(target_tmp)+5:]
        end_index = tmp_line.find("/td>")
        tmp_line = tmp_line[:end_index]
        first_time = True
        while len(tmp_line) > 1:
            start_index = tmp_line.find(">")
            tmp_line = tmp_line[start_index+1:]
            end_index = tmp_line.find("<")

            ex_start_index = tmp_line.find("<img")
            ex_tmp_line = tmp_line[ex_start_index:]
            ex_end_index = ex_tmp_line.find(">")
            ex_tmp_line = ex_tmp_line[:ex_end_index+1]

            ex_start_index_word = tmp_line.find("<img")
            ex_tmp_line_word = tmp_line[ex_start_index_word+57:]
            ex_end_index_word = ex_tmp_line_word.find(">")
            ex_tmp_line_word = ex_tmp_line_word[:ex_end_index_word-5]
            # ex_tmp_line = ex_tmp_line.split(".gif")
            # print(tmp_line)
            if ex_tmp_line != '':
                print(ex_tmp_line)
                print(ex_tmp_line_word)

                if ex_tmp_line_word[0] == "1":
                    ex_tmp_line_word = "B"+ex_tmp_line_word[1:]
                elif ex_tmp_line_word[0] == "2":
                    ex_tmp_line_word = "A"+ex_tmp_line_word[1:]
                elif ex_tmp_line_word[0] == "4":
                    ex_tmp_line_word = "C"+ex_tmp_line_word[1:]

                char = self.lookup(ex_tmp_line_word)
                # print(char)
                if char != None:
                    print(tmp_line)
                    tmp_line = tmp_line.replace(ex_tmp_line, "{}".format(char))
                    print(tmp_line)
                    continue
                    # result = result + char
                else:
                    tmp_line = tmp_line.replace(
                        ex_tmp_line, "''{}'".format(ex_tmp_line_word))
                    # f = open('bi5_table.txt', 'a',encoding="utf-8")
                    # f.write("{} LOST\n".format(ex_tmp_line_word))
                    # f.close()
            # print(tmp_line)
            # if not first_time:
            #     print('not')
            #     result = result + "?"
            first_time = False
            result = result + tmp_line[:end_index]
            tmp_line = tmp_line[end_index+1:]
            # print(result)

        return result

    def find_target_context_other_info(self, target_tmp, line):
        target_tmp2 = ">"
        target_tmp3 = "<"
        index = line.find(target_tmp)
        while line[index-1] != ">":
            line = line[index+len(target_tmp):]
            index = line.find(target_tmp)

        result = ""
        tmp_line = line[index+len(target_tmp)+5:]
        index = tmp_line.find(">")+1
        tmp_line = tmp_line[index:]

        index = tmp_line.find("</td>")
        tmp_line = tmp_line[:index]
        result = ""
        while len(tmp_line) > 1:
            start_flag = "<p>"
            end_flag = "</p>"
            start_index = tmp_line.find(start_flag)
            # tmp_line = tmp_line[start_index+len(start_flag)+1:]
            end_index = tmp_line.find(end_flag)
            tmp = tmp_line[start_index+len(start_flag):end_index]

            while tmp.find("<") != -1:
                tmp_index = tmp.find("<")
                result = result + tmp[:tmp_index]+"?"
                tmp = tmp[tmp_index:]
                tmp_index = tmp.find(">")+1
                tmp = tmp[tmp_index:]
                # pass

            result = result + tmp
            tmp_line = tmp_line[end_index+len(end_flag):]

        #     result = result + tmp_line[:end_index]
        #     tmp_line = tmp_line[end_index+1:]

        return result

    def find_target_context(self, target_tmp, line, number, continue_flag=False, skip_br=False, wholelink=False, debug=False, count=0):

        origin_line = line

        target_tmp2 = ">"
        target_tmp3 = "<"
        # print(count)
        index = line.find(target_tmp, count)

        origin_index = index

        # print(line)
        # print(target_tmp)
        # print(line[index:])
        if index == -1:
            return "★錯誤★"
        while line[index-1] != ">":
            line = line[index+len(target_tmp):]
            index = line.find(target_tmp)

        tmp_line = line[index+len(target_tmp):]

        for i in range(number):
            index = tmp_line.find(target_tmp2)
            tmp_line = tmp_line[index+len(target_tmp2):]
            index = tmp_line.find(target_tmp2)
            tmp_line = tmp_line[index+len(target_tmp2):]

        if wholelink:
            index = tmp_line.find(target_tmp2)
            tmp_line = tmp_line[index+len(target_tmp2):]

        index = tmp_line.find(target_tmp3)
        if target_tmp == '所有權人姓名':
            # print("找====================")
            if index == 0:
                index_start = tmp_line.find('.gif">')
                index_end = tmp_line.find('</td></tr><tr>')
                last_two_word = tmp_line[index_start+6:index_end]
                first_word = tmp_line[74:index_start]
                # print(first_word)

                char = self.lookup(first_word)

                if char != None:
                    return char + last_two_word
                else:
                    return first_word + last_two_word
        if target_tmp == '權利人姓名':
            if index == 0:
                index_start = tmp_line.find('.gif">')
                index_end = tmp_line.find('</td></tr><tr>')
                last_two_word = tmp_line[index_start+6:index_end]
                first_word = tmp_line[74:index_start]
                # print(last_two_word)
                char = self.lookup(first_word)
                if char != None:
                    return char + last_two_word
                else:
                    return first_word + last_two_word

        # if target_tmp == '附屬建物用途':
        #     print("附屬建物用途")
        #     print(tmp_line[:index])
        # if target_tmp == '面積':
        #     print("面積")
        #     print(tmp_line[:index])
        #     print("近來")
        #     # print(origin_line)
        #     print(index)
        #     print(origin_line.find(target_tmp, count))
        #     print(origin_line.find(target_tmp, count+1))
        #     if origin_line.find(target_tmp, origin_index) != origin_line.find(target_tmp, origin_index+1):
        #         print('給老子回去')
        #         new_result = self.find_target_context(target_tmp, origin_line, 1, count=origin_index+1)
        #         print()
        #         return tmp_line[:index] +'\n'+  new_result
        #     else:
        #         return tmp_line[:index]

        append = ""
        if continue_flag:

            tmp_index = tmp_line.find(target_tmp2)
            tmp_tmp_line = tmp_line[tmp_index+1:]
            tmp_index = tmp_tmp_line.find(target_tmp3)
            append = tmp_tmp_line[:tmp_index]
            tmp_line = tmp_line[:index]
            # if target_tmp == '所有權人姓名':
            #     print("first====================")
            #     print(tmp_line)

            return tmp_line + " "+append

        if skip_br:
            tmp_line = tmp_line.split("</td>")[0]
            tmp_line = tmp_line.split("<br>")
            concate = ""
            for txt in tmp_line:
                concate = concate + txt + "\n"
            concate = concate[:-2]
            # if target_tmp == '所有權人姓名':
            #     print("second====================")
            #     print(tmp_line)
            return concate
        tmp_line = tmp_line[:index]

        return tmp_line

    def StartFindOwn(self, input_path, writer):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
        table = soup.findAll(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('width'))
        # print(table[3])
        # input()
        result = ''
        for row in table[3].findAll('tr'):
            cells = row.findAll('td')
            print(cells)
            if len(cells) < 1:
                continue
            if str(cells[0]) == '<td class="left" width="30%">相關他項登記次序</td>':
                result = cells[1].text
                break
            print("-------///////--------------")
        return result

    def StartFindHouse(self, input_path, writer, result, check):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('bordercolor'))

        data = {}
        if result == '':
            models.MarkingDepartmentDependsBuildings.objects.filter(
                markingdepartment=check).delete()

        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) < 1:
                continue
            if str(cells[0]) == '<td class="left">附屬建物用途</td>':
                data["sheet1"] = cells[1].text
                data["sheet2"] = cells[3].text

            if "sheet1" in data and "sheet2" in data:
                if result != '':
                    models.MarkingDepartmentDependsBuildings.objects.create(
                        markingdepartment=result,
                        sheet1=data["sheet1"],
                        sheet2=data["sheet2"],
                    )
                else:
                    models.MarkingDepartmentDependsBuildings.objects.create(
                        markingdepartment=check,
                        sheet1=data["sheet1"],
                        sheet2=data["sheet2"],
                    )
                data = {}
    
    def StartFindHouseNumber(self, input_path,writer,result,check):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('bordercolor'))
        
        data = {}
        if result == '':
            models.MarkingDepartmentDependsLocationNumber.objects.filter(markingdepartment=check).delete()
        for x,row in enumerate(table.findAll('tr')):
            cells = row.findAll('td')
            if len(cells) < 1:
                continue
            if str(cells[0]) == '<td class="bar" colspan="4">建物坐落地號</td>':
                
                ed_cells = table.findAll('tr')[x+1].findAll('td')
                # print(ed_cells)
                data["sheet1"] = ed_cells[1].text
                # print(cells[1].text)
                # input()

            if "sheet1" in data :
                if result != '':

                    models.MarkingDepartmentDependsLocationNumber.objects.create(
                        markingdepartment = result,
                        sheet1 = data["sheet1"],
                    )
                else:
                     models.MarkingDepartmentDependsLocationNumber.objects.create(
                        markingdepartment = check,
                        sheet1 = data["sheet1"],
                    )
                data = {}
         

    def StartFindOther(self, input_path,writer):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('bordercolor'))
        result = ''
        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) < 1:
                continue

            if str(cells[0]) == '<td class="left">其他登記事項</td>':
                result = cells[1].text
                break
        
        # print(result)
        return result
        # input()

    def StartFindArray(self, input_path,writer,result,check):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
       
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('bordercolor'))
        if result == '':
            models.MarkingDepartmentPublicPart.objects.filter(markingdepartment=check).delete()

        all_public = []
        all_rights_scope_1 = []
        all_rights_scope_2 = []
        other = []
        buffer = ''
        data={}

        for row in table.findAll('tr'):
            cells = row.findAll('td')

            if len(cells) < 2:
                continue
            
            if str(cells[0]) == '<td class="left">共有部分</td>':
                
                all_public.append(cells[1].text)
                writer.write("[共有部分]\n" + cells[1].text + "\n")
                data["sheet1"] = cells[1].text

            if str(cells[0]) == '<td class="left">　權利範圍</td>':
                all_rights_scope_1.append(cells[1].text)
                all_rights_scope_2.append(cells[3].text)
                
                writer.write("[權利範圍]\n" + cells[1].text + "\n")
                writer.write("[面積]\n" + cells[3].text + "\n")
                data["sheet2"] = cells[1].text
                data["sheet3"] = cells[3].text
                
            if str(cells[0]) == '<td class="left">　其他登記事項</td>':
                other.append(cells[1].text)
                writer.write("[其他登記事項]\n" + cells[1].text + "\n")
                data["sheet4"] = cells[1].text

            if str(cells[0]) == '<td class="left" rowspan="2" width="15%">　　含停車位</td>':
                buffer = cells[2].text

            if str(cells[0]) == '<td class="left">權利範圍</td>':
                writer.write("[含停車位]\n編號: " + buffer + '權利範圍: ' + cells[1].text + "\n")
                
                data["sheet5"] = "編號: " + buffer + '權利範圍: ' + cells[1].text 
                buffer = ''

            # for detail in cells:
            #     print(detail)
            # print(data)
            
            # print("-------------------------------------")
            # print(cells)


        if "sheet1" in data and "sheet2" in data and "sheet3" in data and "sheet4" in data and "sheet5" in data :
            if result != '':
                models.MarkingDepartmentPublicPart.objects.create(
                    markingdepartment = result,
                    sheet1 = data["sheet1"],
                    sheet2 = data["sheet2"],
                    sheet3 = data["sheet3"],
                    sheet4 = data["sheet4"],
                    sheet5 = data["sheet5"]
                )
            else:
                models.MarkingDepartmentPublicPart.objects.create(
                    markingdepartment = check,
                    sheet1 = data["sheet1"],
                    sheet2 = data["sheet2"],
                    sheet3 = data["sheet3"],
                    sheet4 = data["sheet4"],
                    sheet5 = data["sheet5"]
                )
            data = {}
                
    def process_signature(self, folder_fullpath):
        # 標示部
        input_path = join(folder_fullpath, "標示部.html")
        output_path = join(folder_fullpath, "標示部.txt")
        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>#content a:link {"
        writer.write("建物標示部\n")
        data = {}
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "縣市"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet1"] = tmp_line

                    target_txt = "鄉鎮市區"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet2"] = tmp_line

                    target_txt = "地段"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet3"] = tmp_line

                    target_txt = "建號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet4"] = tmp_line

                    target_txt = "登記日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet5"] = tmp_line

                    target_txt = "登記原因"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet6"] = tmp_line

                    target_txt = "建物門牌"
                    tmp_line = self.find_target_context_may_include_img(
                        target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet7"] = tmp_line

                    # target_txt = "建物坐落地號"
                    # tmp_line = self.find_target_context(
                    #     target_txt, line, 3, continue_flag=True)
                    # writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    

                    target_txt = "主要用途"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet8"] = tmp_line

                    target_txt = "主要建材"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet9"] = tmp_line

                    target_txt = "總面積"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet11"] = tmp_line

                    target_txt = "層次面積"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet13"] = tmp_line

                    target_txt = "層數"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet10"] = tmp_line

                    target_txt = "層次"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet12"] = tmp_line

                    target_txt = "建築完成日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet14"] = tmp_line

                    target_txt = "附屬建物用途"
                    start_index = 0

                    while 1:
                        # print(start_index)
                        house_index = line.find(target_txt, start_index)

                        tmp_line = self.find_target_context(
                            target_txt, line, 1, count=start_index)

                        if tmp_line != '★錯誤★':
                            writer.write(
                                "[" + target_txt + "]\n" + tmp_line + "\n")
                        else:
                            pass
                            # writer.write("[" + target_txt + "]\n" + '無' + "\n")

                        if tmp_line != '★錯誤★':

                            de_target_txt = "面積"
                            tmp_line = self.find_target_context(
                                de_target_txt, line, 1, count=start_index+60)
                            writer.write(
                                "[" + de_target_txt + "]\n" + tmp_line + "\n")
                        else:
                            pass
                            # writer.write("[" + target_txt + "]\n" + '無' + "\n")

                        if house_index == -1:
                            break

                        start_index = house_index + 1
                    
                    data["sheet15"] = self.StartFindOther(input_path,writer)
                    
                    # target_txt = "其他登記事項"
                    # tmp_line = self.find_target_context(
                    #     target_txt, line, 1, skip_br=True)
                    # if tmp_line == "":
                    #     tmp_line = "(空白)"
                    # writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
        reader.close
        result = ''
        check = models.MarkingDepartment.objects.filter(sheet3=data["sheet3"], sheet4=data["sheet4"])
        if len(check) == 0:
       
            result = models.MarkingDepartment.objects.create(
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"])
        else:
            
            check.update(
                update_time=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"])
            check = models.MarkingDepartment.objects.get(sheet3=data["sheet3"], sheet4=data["sheet4"])

        self.StartFindArray(input_path,writer,result,check)
        self.StartFindHouse(input_path,writer,result,check)
        self.StartFindHouseNumber(input_path,writer,result,check)
        writer.close

    def process_owner(self, folder_fullpath, index):
        # 所有權部
        input_path = join(folder_fullpath, "owner_"+index+"_page.html")
        output_path = join(folder_fullpath, "owner_"+index+"_page.txt")

        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>.left{	font-size: 100%;"
        writer.write("建物所有權部\n")
        data = {}
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "縣市名稱"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet1"] = tmp_line

                    target_txt = "鄉鎮市區"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet2"] = tmp_line

                    target_txt = "地段"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet3"] = tmp_line

                    target_txt = "建號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet4"] = tmp_line

                    target_txt = "登記次序"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet5"] = tmp_line

                    target_txt = "登記日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet6"] = tmp_line

                    target_txt = "登記原因"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet7"] = tmp_line

                    target_txt = "原因發生日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet8"] = tmp_line

                    target_txt = "所有權人姓名"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet9"] = tmp_line

                    target_txt = "統一編號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet10"] = tmp_line

                    target_txt = "住址"
                    tmp_line = self.find_address(target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet11"] = tmp_line

                    target_txt = "權利範圍"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet12"] = tmp_line

                    target_txt = "權狀字號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet13"] = tmp_line

                    # target_txt = "相關他項登記次序"
                    # tmp_line = self.find_target_context(
                    #     target_txt, line,1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    # print("相關他項登記次序")
                    # print(tmp_line)
                    data["sheet14"] = self.StartFindOwn(input_path,writer)

                    target_txt = "其他登記事項"
                    tmp_line = self.find_target_context_other_info(
                        target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet15"] = tmp_line
        result = ''
        check = models.OwnershipDepartment.objects.filter(sheet3=data["sheet3"], sheet4=data["sheet4"])
        if len(check) == 0:
            models.OwnershipDepartment.objects.create(
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"])
        else:
            
            check.update(
                update_time=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"])
        reader.close
        writer.close

    def process_other(self, folder_fullpath, index):
        # 他項

        input_path = join(folder_fullpath, "other_"+index+"_page.html")
        output_path = join(folder_fullpath, "other_"+index+"_page.txt")

        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>#content a:link {"
        writer.write("建物他項權利部\n")
        data = {}
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "縣市名稱"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet1"] = tmp_line

                    target_txt = "鄉鎮市區"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet2"] = tmp_line

                    target_txt = "段號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet3"] = tmp_line

                    target_txt = "建號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet4"] = tmp_line

                    target_txt = "登記次序"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet5"] = tmp_line

                    target_txt = "權利種類"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet6"] = tmp_line

                    target_txt = "收件年期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet7"] = tmp_line

                    target_txt = "收件字號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet8"] = tmp_line

                    target_txt = "登記日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet9"] = tmp_line

                    target_txt = "登記原因"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet10"] = tmp_line

                    target_txt = "權利人姓名"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet11"] = tmp_line

                    target_txt = "權利人統一編號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet12"] = tmp_line

                    target_txt = "住址"
                    tmp_line = self.find_address(target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet13"] = tmp_line

                    target_txt = "債權額比例"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet14"] = tmp_line

                    target_txt = "擔保債權總金額"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet15"] = tmp_line

                    target_txt = "擔保債權種類及範圍"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    # print(line)
                    if tmp_line != '★錯誤★':
                        writer.write(
                            "[" + target_txt + "]\n" + tmp_line + "\n")
                        data["sheet29"] = tmp_line
                    else:
                        writer.write("[" + target_txt + "]\n" + '無' + "\n")
                        data["sheet29"] = '無'

                    target_txt = "擔保債權確定期日"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet16"] = tmp_line

                    target_txt = "存續期間"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    
                    if tmp_line != '★錯誤★':
                        writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                        data["sheet17"] = tmp_line
                    else:
                        writer.write("[" + target_txt + "]\n" + '無' + "\n")
                        data["sheet17"] = '無'

                    target_txt = "清償日期"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet18"] = tmp_line

                    target_txt = "利息(率)或地租"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet19"] = tmp_line

                    target_txt = "遲延利息(率)"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet20"] = tmp_line

                    target_txt = "違約金"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet21"] = tmp_line

                    target_txt = "其他擔保範圍約定"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "權利標的"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet22"] = tmp_line

                    target_txt = "標的登記次序"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, wholelink=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet23"] = tmp_line

                    target_txt = "設定權利範圍"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet24"] = tmp_line

                    target_txt = "證明書字號"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet25"] = tmp_line

                    target_txt = "共同擔保地號"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, continue_flag=True, debug=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet26"] = tmp_line

                    target_txt = "共同擔保建號"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, continue_flag=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet27"] = tmp_line

                    target_txt = "其他登記事項"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, skip_br=True)
                    if tmp_line == "<p>(空白)</p":
                        tmp_line = "(空白)"
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
                    data["sheet28"] = tmp_line
        result = ''
        check = models.OtherShipDepartment.objects.filter(sheet3=data["sheet3"], sheet4=data["sheet4"])
        if len(check) == 0:
                    
            models.OtherShipDepartment.objects.create(
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"],
                sheet16=data["sheet16"],
                sheet17=data["sheet17"],
                sheet18=data["sheet18"],
                sheet19=data["sheet19"],
                sheet20=data["sheet20"],
                sheet21=data["sheet21"],
                sheet22=data["sheet22"],
                sheet23=data["sheet23"],
                sheet24=data["sheet24"],
                sheet25=data["sheet25"],
                sheet26=data["sheet26"],
                sheet27=data["sheet27"],
                sheet28=data["sheet28"],
                sheet29=data["sheet29"],
                )
        else:
            
            check.update(
                update_time=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                sheet1=data["sheet1"],
                sheet2=data["sheet2"],
                sheet3=data["sheet3"],
                sheet4=data["sheet4"],
                sheet5=data["sheet5"],
                sheet6=data["sheet6"],
                sheet7=data["sheet7"],
                sheet8=data["sheet8"],
                sheet9=data["sheet9"],
                sheet10=data["sheet10"],
                sheet11=data["sheet11"],
                sheet12=data["sheet12"],
                sheet13=data["sheet13"],
                sheet14=data["sheet14"],
                sheet15=data["sheet15"],
                sheet16=data["sheet16"],
                sheet17=data["sheet17"],
                sheet18=data["sheet18"],
                sheet19=data["sheet19"],
                sheet20=data["sheet20"],
                sheet21=data["sheet21"],
                sheet22=data["sheet22"],
                sheet23=data["sheet23"],
                sheet24=data["sheet24"],
                sheet25=data["sheet25"],
                sheet26=data["sheet26"],
                sheet27=data["sheet27"],
                sheet28=data["sheet28"],
                sheet29=data["sheet29"],
            )
        reader.close
        writer.close

    def main(self):
        # print(self.ouput_path)
        folders = listdir(self.ouput_path)
        for folder in folders:
            folder_fullpath = join(self.ouput_path, folder)
            if isdir(folder_fullpath):

                files = listdir(folder_fullpath)
                print(folder_fullpath)
                for file in files:
                    file_fullpath = join(folder_fullpath, file)
                    if isfile(file_fullpath):
                        print("檔案：", file)
                        
                        if file[:3] == "標示部":
                            # print(file[3:])
                            if file[3:] == '.html':
                                self.process_signature(folder_fullpath)
                        elif file[:5] == "owner":
                            index = file.split("_")[1]
                            if file[12:] == '.html':
                                self.process_owner(folder_fullpath, index)
                        elif file[:5] == "other":
                            index = file.split("_")[1]
                            print(file[12:])
                            if file[12:] == '.html':
                                self.process_other(folder_fullpath, index)



   