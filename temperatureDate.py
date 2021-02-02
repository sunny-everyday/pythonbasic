import csv
import matplotlib.pyplot as plt
import numpy as np

filename =  'D:/test/temperature-COM3-2021_2_1_16-07-10.DAT'
with open(filename) as f:
    reader = csv.reader(f)
    timegroup = []

    for row in reader:
        if row == []:
            continue

        cf, cv = str(row).split('+')
  #      print(cv)
        sf, sv = cv.split('\'')
        #(sf)
        timegroup.append(float(sf))
    x = np.arange(0, len(timegroup))
    fig=plt.figure(num=1,figsize=(6,4))
    ax=fig.add_subplot(111)
    ax.plot(x,timegroup)

    plt.show()