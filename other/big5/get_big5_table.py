#!/usr/bin/env python3
# -*- coding: utf-8 -*-

path = 'bi5_table.txt'
writer = open(path, 'w', encoding="utf-8")

f = open('ori_table.txt', encoding="utf-8")
for line in f.readlines():
    line = line[:-1]

    if line!="" and line[:4]!="code" and line[:4]!="====":
        encode_number = line[:3]
        # encode_txt = line[6:].split(" ")
        line = line[6:]
        encode_txt = []
        while len(encode_txt)!=16:
            if line[0]!=" ":
                encode_txt.append(line[0])
                line = line[2:]
            else:
                encode_txt.append(line[0])
                line = line[3:]
        # print(encode_txt)
        # input()
        # print(line)
        # print(encode_txt)
        # print(len(encode_txt))
        # input("----------")
        for index, char in enumerate(["0", "1", "2", "3","4","5", "6","7", "8", "9", "A", "B", "C", "D","E", "F"]):
            writer.write(encode_number+char+" "+encode_txt[index]+"\n")

f.close
writer.close