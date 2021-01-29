import csv
import matplotlib.pyplot as plt
import time
from datetime import datetime

filename =  'D:/test/LoggedData_21_01_27_17_23_35_StrainData1000.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用了next()一次，因此得到的是文件的第一行
    print(header_row)

    historytime = []
    StrainX = []
    StrainY = []
    StrainZ = []
    #extract = [1, 100000, 200000, 300000, 400000, 500000, 600000]
    extract = [1, 100000]
    index = 1
    for row in reader:
        #datetime_obj = datetime.strptime("2021-01-01 "+row[0], "%Y-%m-%d %H:%M:%S:%f")
        #microtime = time.mktime(datetime_obj.timetuple())*1000 + datetime_obj.microsecond / 1000.0
        if index > 10000:
            StrainX.append(float(row[6]))
            StrainY.append(float(row[7]))
            StrainZ.append(float(row[8]))
            historytime.append(index)
        if index > 11000:
            break
        index += 1

# 根据数据绘制图形
plt.figure(figsize=(16,8))
plt.subplot(111)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(StrainX, c='red', label='MAP')
plt.xticks(range(len(historytime)), historytime, rotation=30)
plt.xlabel('historytime')
plt.ylabel("StrainX")
photoname = filename.replace('csv', 'png')
print(photoname)
plt.savefig(photoname)
plt.show()
