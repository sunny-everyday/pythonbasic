import csv
import os
import matplotlib.pyplot as plt
import time
from datetime import datetime


filedir =  'D:/LoggedData_21_02_02_16_41_58'
file1 = '_AccelData.csv'
file2 = '_EulerAngles.csv'
file3 = '_StrainData.csv'
file4 = '_StressData.csv'
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
plt.plot(node2, c='green', label='MAP')
plt.ylabel("Strain frequency")

plt.subplot(413)
plt.plot(node3, c='green', label='MAP')
plt.ylabel("Strain frequency")

plt.subplot(414)
plt.plot(node4, c='green', label='MAP')
plt.ylabel("Strain frequency")

photoname = filedir + 'Node4'
print(photoname)
plt.savefig(photoname)
plt.show()
