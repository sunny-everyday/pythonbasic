import csv
import os
import matplotlib.pyplot as plt
import time
from datetime import datetime


filedir =  'D:/02-progress/SD/tensar/SmartGrid_GUI_v34p0/SmartGrid_GUI_v34p0/CanAnalysis_App/SmartGrid_Host_v34p0_2021_01_28/Datalog/'
file1 = 'Node1-30m.csv'
file2 = 'Node2-30m.csv'
file3 = 'Node3-30m.csv'
file4 = 'Node4-30m.csv'
node1 = []
node1index = []
node2 = []
node2index = []
node3 = []
node3index = []
node4 = []
node4index = []

with open(filedir + file1) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
    index = 1
    for row in reader:
        substrainX = int(row[0])
        node1.append(substrainX)
        index +=1
        node1index.append(index)

with open(filedir + file2) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
    index = 1
    for row in reader:
        substrainX = int(row[0])
        node2.append(substrainX)
        index +=1
        node2index.append(index)

with open(filedir + file3) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
    index = 1
    for row in reader:
        substrainX = int(row[0])
        node3.append(substrainX)
        index +=1
        node3index.append(index)

with open(filedir + file4) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
    index = 1
    for row in reader:
        substrainX = int(row[0])
        node4.append(substrainX)
        index +=1
        node4index.append(index)

plt.subplot(411)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(node1, c='green', label='MAP')
plt.ylabel("Strain frequency")


plt.subplot(412)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(node2, c='green', label='MAP')
plt.ylabel("Strain frequency")


plt.subplot(413)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(node3, c='green', label='MAP')
plt.ylabel("Strain frequency")


plt.subplot(414)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(node4, c='green', label='MAP')
plt.ylabel("Strain frequency")
plt.show()
