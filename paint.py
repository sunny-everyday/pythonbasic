import csv
import matplotlib.pyplot as plt
import time
from datetime import datetime

filename =  'D:/test/LoggedData_21_02_02_16_55_38_StrainData.csv'
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
    index = 1
    for row in reader:
        #datetime_obj = datetime.strptime("2021-01-01 "+row[0], "%Y-%m-%d %H:%M:%S:%f")
        #microtime = time.mktime(datetime_obj.timetuple())*1000 + datetime_obj.microsecond / 1000.0
        index += 1
        if index > 1:
            historytime.append(index - 1)
            StrainX.append(float(row[3]))
            StrainY.append(float(row[4]))
            StrainZ.append(float(row[5]))
#            StrainEX.append(float(row[6]))
#            StrainEY.append(float(row[7]))
#            StrainEZ.append(float(row[8]))

            if(StrainX[len(StrainX)-1] - StrainX[len(StrainX)-2] > 0.03):
                print(StrainX[len(StrainX)-1])
                print(row[0])

            if (StrainX[len(StrainX) - 2] - StrainX[len(StrainX) - 1] > 0.03):
                print(StrainX[len(StrainX) - 1])
                print(row[0])

        #if index > 1000:
         #   break
# 根据数据绘制图形
plt.figure(figsize=(20, 16))
plt.subplot(311)
plt.title("Strdal-strain-drawing", fontsize=24)
plt.plot(historytime, StrainX, c='red', label='MAP')
plt.ylabel("StrainX")

plt.subplot(312)
plt.plot(historytime, StrainY, c='green', label='MAP')
plt.ylabel("StrainY")

plt.subplot(313)
plt.plot(historytime, StrainZ, c='blue', label='MAP')
plt.ylabel("StrainZ")

# plt.subplot(614)
# # plt.title("Strdal-strain-drawing", fontsize=24)
# # plt.plot(historytime, StrainEX, c='red', label='MAP')
# # plt.ylabel("StrainEX")
# #
# # plt.subplot(615)
# # plt.plot(historytime, StrainEY, c='green', label='MAP')
# # plt.ylabel("StrainEY")
# #
# # plt.subplot(616)
# # plt.plot(historytime, StrainEZ, c='blue', label='MAP')
# # plt.ylabel("StrainEZ")
plt.show()
