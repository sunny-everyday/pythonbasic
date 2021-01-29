import matplotlib.pyplot as plt
from datetime import datetime

filedir =  'D:/02-progress/SD/tensar/SmartGrid_GUI_v34p0/SmartGrid_GUI_v34p0/CanAnalysis_App/SmartGrid_Host_v34p0_2021_01_28/Datalog/'
file1 = 'Node1-30m.txt'
file2 = 'Node2-30m.txt'
file3 = 'Node3-30m.txt'
file4 = 'Node4-30m.txt'
node1 = []
node2 = []
node3 = []
node4 = []
f1 = open(filedir + file1 , "r")  # 设置文件对象
node1 = f1.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
f1.close()  # 关闭文件

f2 = open(filedir + file2 , "r")  # 设置文件对象
node2 = f2.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
f2.close()  # 关闭文件

f3 = open(filedir + file3 , "r")  # 设置文件对象
node3 = f3.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
f3.close()  # 关闭文件

f4 = open(filedir + file4 , "r")  # 设置文件对象
node4 = f4.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
f4.close()  # 关闭文件


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