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

    index = 1
    for row in reader:
        #datetime_obj = datetime.strptime("2021-01-01 "+row[0], "%Y-%m-%d %H:%M:%S:%f")
        #microtime = time.mktime(datetime_obj.timetuple())*1000 + datetime_obj.microsecond / 1000.0
        historytime.append(index)
        StrainX.append(float(row[6]))
        StrainY.append(float(row[7]))
        StrainZ.append(float(row[8]))
        index += 1
        if index > 1000:
            break
# 根据数据绘制图形
plt.subplot(111)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(historytime, StrainX, c='red', label='MAP')
plt.xlabel('historytime')
plt.ylabel("StrainX")
plt.show()
