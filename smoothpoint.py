import csv
import os
import matplotlib.pyplot as plt
import time
from datetime import datetime


def opensmallfileforpaint(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
        print(header_row)

        historytime = []
        StrainX = []
        StrainY = []
        StrainZ = []
        StrainEX = []
        StrainEY = []
        StrainEZ = []
        SubStrainX = []
        strainX = strainY = strainZ = strainEX = strainEY = strainEZ = 0.0
        index = 1
        for row in reader:
            for i in range(200):
                strainX += float(row[3])
                strainY += float(row[4])
                strainZ += float(row[5])
                strainEX += float(row[6])
                strainEY += float(row[7])
                strainEZ += float(row[8])
            strainX = strainX / 200
            strainY = strainY / 200
            strainZ = strainZ / 200
            strainEX = strainEX / 200
            strainEY = strainEY / 200
            strainEZ = strainEZ / 200
            substrainX = float(row[3])

            #datetime_obj = datetime.strptime("2021-01-01 "+row[0], "%Y-%m-%d %H:%M:%S:%f")
            #microtime = time.mktime(datetime_obj.timetuple())*1000 + datetime_obj.microsecond / 1000.0

            historytime.append(index)
            StrainX.append(strainX)
            StrainY.append(strainY)
            StrainZ.append(strainZ)
            StrainEX.append(strainEX)
            StrainEY.append(strainEY)
            StrainEZ.append(strainEZ)
            SubStrainX.append(substrainX)
            index += 1
    # 根据数据绘制图形
    plt.subplot(311)
    plt.title("Strdal-strain-drawing", fontsize=24)
    #plt.plot(historytime, StrainX, c='red', label='MAP')
    plt.plot(historytime, StrainX, c='red', label='MAP')
    #plt.plot(historytime, StrainY, c='green', label='MAP')
    #plt.plot(historytime, StrainZ, c='blue', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainX")
    plt.subplot(312)
    plt.plot(historytime, StrainY, c='green', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainY")
    plt.subplot(313)
    plt.plot(historytime, StrainZ, c='blue', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainZ")
    photoname = filename.replace('.csv', 'E.png')
    print(photoname)
    plt.savefig(photoname)
    plt.show()

filedir =  'LoggedData_21_01_27_09_38_14_StrainData5.csv'
def getpaints():
    for i in range(10):
        filename = "D:/" + "test_" + str(i) + filedir
        opensmallfileforpaint(filename)

#getpaints()
filename = 'D:/test/LoggedData_21_01_27_09_38_14_StrainData5.csv'
opensmallfileforpaint(filename)
