import os
import csv
import datetime
import pandas as pd

#import matplotlib.pyplot as plt
import time

def read_csv(filename):

    reader = csv.reader(open(filePath + filename,'r'))
    dlastS = datetime.datetime.strptime('0:0:0:0', "%H:%M:%S:%f")
    thissecondrequency = 0
    totalrequency = 0
    secondtime = 0
    frequencylist = []
    for line in reader: #这里的line就是读取的csv中的一行信息，是一个列表，直接可以根据下标来取第几列#  #我这里是把这个路径的图片展示出来，不用管下面的信息，只要知道line的类型就可以了
        if line[0] == 'Hr:Min:Sec:MSec':
            continue
        #print('new second')

        dd = datetime.datetime.strptime(line[0], "%H:%M:%S:%f")
        if dlastS.hour == 0:
            dlastS = dd
            continue
        if (dlastS.hour == dd.hour and dlastS.minute == dd.minute and dlastS.second == dd.second ):
            thissecondrequency +=1
        else:
            #print(thissecondrequency)
            frequencylist.append(thissecondrequency)

            #if thissecondrequency < 110:
                #print(dlastS)
                #print(thissecondrequency)
            dlastS = dd
            secondtime += 1
            totalrequency += thissecondrequency
                #print(totalrequency)
            thissecondrequency = 0
    print(int(totalrequency/(secondtime)))
    name = ['frequency']
    test = pd.DataFrame(columns=name, data=frequencylist)  # 数据有一列
    #print(test)
    test.to_csv('D:/'+filename,encoding='utf-8',index=False)

if __name__ == '__main__':
    # generate_excel()
    filePath = 'D://02-progress//SD//tensar//SmartGrid_GUI_v34p0//SmartGrid_GUI_v34p0//ZLG_App//SmartGrid_Host_v34p0_2021_01_21//Datalog//Node4//'
    os.listdir(filePath)
    for _, Nodes, fnames in os.walk(filePath):
        print(Nodes)
    for filename in fnames:
        print(filename)
        read_csv(filename)

    #read_csv(filePath +'/' + filename)