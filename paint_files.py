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
            StrainX.append(float(row[3]))
            StrainY.append(float(row[4]))
            StrainZ.append(float(row[5]))
            StrainEX.append(float(row[6]))
            StrainEY.append(float(row[7]))
            StrainEZ.append(float(row[8]))

            #datetime_obj = datetime.strptime("2021-01-01 "+row[0], "%Y-%m-%d %H:%M:%S:%f")
            #microtime = time.mktime(datetime_obj.timetuple())*1000 + datetime_obj.microsecond / 1000.0
            historytime.append(index)
            index += 1
    # 根据数据绘制图形
    plt.figure(figsize=(16, 16))
    plt.subplot(611)
    plt.title("strain-drawing", fontsize=24)
    plt.plot(historytime, StrainX, c='red', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainX")
    plt.subplot(612)
    plt.plot(historytime, StrainY, c='green', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainY")
    plt.subplot(613)
    plt.plot(historytime, StrainZ, c='blue', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainZ")
    photoname = filename.replace('.csv', 'E.png')

    plt.subplot(614)
    plt.plot(historytime, StrainEX, c='red', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainEX")
    plt.subplot(615)
    plt.plot(historytime, StrainEY, c='green', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainEY")
    plt.subplot(616)
    plt.plot(historytime, StrainEZ, c='blue', label='MAP')
    plt.xlabel('historytime')
    plt.ylabel("StrainEZ")
    photoname = filename.replace('.csv', 'E.png')
    print(photoname)
    plt.savefig(photoname)

    plt.show()

filedir =  'LoggedData_21_02_02_09_22_54_StrainData.csv'
def getpaints():
    for i in range(2):
        filename = "D:/" + "test_" + str(i) + filedir
        opensmallfileforpaint(filename)

getpaints()
#filename = 'D:/test/LoggedData_21_01_29_16_49_09_StrainData.csv'
#opensmallfileforpaint(filename)
