# -*- coding:utf-8 -*-
import xlrd
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as  mpl

infos=[]
info_file=xlrd.open_workbook('E:/selfInfo/econemy/9831_20210101_20210129.xlsx')#打开excel文件
info_sheet=info_file.sheets()[0]#通过索引顺序获取工作表
row_count=info_sheet.nrows#获取行数，列数ncols
category = []

for row in range(8,row_count):
    time_string=info_sheet.cell(row,3).value
    if( ''!= time_string):
        category.append(info_sheet.cell(row,6).value)
#print(category)
set_category=set(category)
print(set_category)
print(len(set_category))
category = list(set_category)

categoryvalue = [[0 for i in range(2)] for j in range(len(set_category))]

for index in range(len(set_category)):
    categoryvalue[index][0] = category[index]

for row in range(8,row_count):
    time_string=info_sheet.cell(row,3).value
    if( ''!= time_string):
        value = int(time_string)
        for index in range(len(set_category)):
            if info_sheet.cell(row,6).value == category[index]:
                categoryvalue[index][1] += value
#print(categoryvalue)
categoryvalue.sort(key=lambda x:x[1])
#print(categoryvalue)
#将list元素转存为CSV文件 https://blog.csdn.net/qq_38409301/article/details/89818632
name=['category','number']
test=pd.DataFrame(columns=name,data=categoryvalue)#数据有三列，列名分别为one,two,three
test.to_csv('E:/selfInfo/econemy/classandsort.csv',encoding='gbk',index=False)

fig = plt.figure()
value = []
for index in range(len(set_category)):
    value.append(categoryvalue[index][1])

classname = []
for index in range(len(set_category)):
    classname.append(categoryvalue[index][0])

p = plt.pie(value, labels=classname,autopct='%1.1f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
for front in p[1]:
    front.set_fontproperties(mpl.font_manager.FontProperties(
        fname='C:/Windows/WinSxS/amd64_microsoft-windows-font-truetype-simfang_31bf3856ad364e35_10.0.18362.1_none_5a7f93f39ed619f0/simfang.ttf'))
plt.title("Pie chart")

plt.show()
#plt.savefig("PieChart.jpg")
