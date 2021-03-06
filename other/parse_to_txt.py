from cgitb import lookup
from os import listdir
from os.path import isfile, isdir, join
import search_font as search_font
import time
from bs4 import BeautifulSoup


class StartParseText():
    def __init__(self):
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
            return "????????????"
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
        if target_tmp == '??????????????????':
            # print("???====================")
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
        if target_tmp == '???????????????':
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

        # if target_tmp == '??????????????????':
        #     print("??????????????????")
        #     print(tmp_line[:index])
        # if target_tmp == '??????':
        #     print("??????")
        #     print(tmp_line[:index])
        #     print("??????")
        #     # print(origin_line)
        #     print(index)
        #     print(origin_line.find(target_tmp, count))
        #     print(origin_line.find(target_tmp, count+1))
        #     if origin_line.find(target_tmp, origin_index) != origin_line.find(target_tmp, origin_index+1):
        #         print('???????????????')
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
            # if target_tmp == '??????????????????':
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
            # if target_tmp == '??????????????????':
            #     print("second====================")
            #     print(tmp_line)
            return concate
        tmp_line = tmp_line[:index]

        return tmp_line

    def StartFindArray(self, input_path,writer):
        soup = BeautifulSoup(open(input_path, encoding="utf-8"), 'html.parser')
       
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr(
            'cellpadding') and tag.has_attr('cellpadding') and tag.has_attr('bordercolor'))
       
        all_public = []
        all_rights_scope_1 = []
        all_rights_scope_2 = []
        other = []
        buffer = ''

        for row in table.findAll('tr'):
            cells = row.findAll('td')

            if len(cells) < 2:
                continue
            
            if str(cells[0]) == '<td class="left">????????????</td>':
                
                all_public.append(cells[1].text)
                writer.write("[????????????]\n" + cells[1].text + "\n")

            if str(cells[0]) == '<td class="left">???????????????</td>':
                all_rights_scope_1.append(cells[1].text)
                all_rights_scope_2.append(cells[3].text)
                
                writer.write("[????????????]\n" + cells[1].text + "\n")
                writer.write("[??????]\n" + cells[3].text + "\n")
                
            if str(cells[0]) == '<td class="left">?????????????????????</td>':
                other.append(cells[1].text)
                writer.write("[??????????????????]\n" + cells[1].text + "\n")

            if str(cells[0]) == '<td class="left" rowspan="2" width="15%">??????????????????</td>':
                buffer = cells[2].text

            if str(cells[0]) == '<td class="left">????????????</td>':
                writer.write("[????????????]\n??????: " + buffer + '????????????: ' + cells[1].text + "\n")
                buffer = ''

            # for detail in cells:
            #     print(detail)
               
            print("-------------------------------------")
            # print(cells)


    def process_signature(self, folder_fullpath):
        # ?????????
        input_path = join(folder_fullpath, "?????????.html")
        output_path = join(folder_fullpath, "?????????.txt")
        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>#content a:link {"
        writer.write("???????????????\n")
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context_may_include_img(
                        target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(
                        target_txt, line, 3, continue_flag=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "?????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    start_index = 0

                    while 1:
                        # print(start_index)
                        house_index = line.find(target_txt, start_index)

                        tmp_line = self.find_target_context(
                            target_txt, line, 1, count=start_index)

                        if tmp_line != '????????????':
                            writer.write(
                                "[" + target_txt + "]\n" + tmp_line + "\n")
                        else:
                            pass
                            # writer.write("[" + target_txt + "]\n" + '???' + "\n")

                        if tmp_line != '????????????':

                            de_target_txt = "??????"
                            tmp_line = self.find_target_context(
                                de_target_txt, line, 1, count=start_index+60)
                            writer.write(
                                "[" + de_target_txt + "]\n" + tmp_line + "\n")
                        else:
                            pass
                            # writer.write("[" + target_txt + "]\n" + '???' + "\n")

                        if house_index == -1:
                            break

                        start_index = house_index + 1

                    # target_txt = "??????????????????"
                    # tmp_line = self.find_target_context(
                    #     target_txt, line, 1, skip_br=True)
                    # if tmp_line == "":
                    #     tmp_line = "(??????)"
                    # writer.write("[" + target_txt + "]\n" + tmp_line + "\n")
        reader.close
        self.StartFindArray(input_path,writer)
        writer.close

    def process_owner(self, folder_fullpath, index):
        # ????????????
        input_path = join(folder_fullpath, "owner_"+index+"_page.html")
        output_path = join(folder_fullpath, "owner_"+index+"_page.txt")

        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>.left{	font-size: 100%;"
        writer.write("??????????????????\n")
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_address(target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context_other_info(
                        target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

        reader.close
        writer.close

    def process_other(self, folder_fullpath, index):
        # ??????

        input_path = join(folder_fullpath, "other_"+index+"_page.html")
        output_path = join(folder_fullpath, "other_"+index+"_page.txt")

        writer = open(output_path, 'w', encoding="utf-8")
        reader = open(input_path, 'r', encoding="utf-8")
        target_txt = "<style>#content a:link {"
        writer.write("?????????????????????\n")
        for line in reader.readlines():
            line = line[:-1]
            if len(line) > len(target_txt):
                if line[:len(target_txt)] == target_txt:

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "???????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "?????????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????"
                    tmp_line = self.find_address(target_txt, line)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "???????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "?????????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "???????????????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    # print(line)
                    if tmp_line != '????????????':
                        writer.write(
                            "[" + target_txt + "]\n" + tmp_line + "\n")
                    else:
                        writer.write("[" + target_txt + "]\n" + '???' + "\n")
                    target_txt = "????????????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????(???)?????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "?????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, wholelink=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "???????????????"
                    tmp_line = self.find_target_context(target_txt, line, 1)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, continue_flag=True, debug=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, continue_flag=True)
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

                    target_txt = "??????????????????"
                    tmp_line = self.find_target_context(
                        target_txt, line, 1, skip_br=True)
                    if tmp_line == "<p>(??????)</p":
                        tmp_line = "(??????)"
                    writer.write("[" + target_txt + "]\n" + tmp_line + "\n")

        reader.close
        writer.close

    def main(self):

        folders = listdir(self.ouput_path)
        for folder in folders:
            folder_fullpath = join(self.ouput_path, folder)
            if isdir(folder_fullpath):

                files = listdir(folder_fullpath)
                print(folder_fullpath)
                for file in files:
                    file_fullpath = join(folder_fullpath, file)
                    if isfile(file_fullpath):
                        print("?????????", file)

                        if file[:3] == "?????????":
                            # print(file[3:])
                            if file[3:] == '.html':
                                self.process_signature(folder_fullpath)
                        elif file[:5] == "owner":
                            index = file.split("_")[1]
                            self.process_owner(folder_fullpath, index)
                        elif file[:5] == "other":
                            index = file.split("_")[1]
                            self.process_other(folder_fullpath, index)
