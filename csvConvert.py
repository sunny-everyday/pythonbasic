from io import StringIO
import csv
import pandas as pd

c_path = r"D:\02-progress\SD\测试问题汇总\tensar\测试记录\33P4版本应变及电压变化数据\LoggedData_21_01_25_09_45_02_StrainData1.csv"
x_path = r"C:\FineReport_10.0\webapps\webroot\WEB-INF\reportlets\Node"  # 路径中的xls文件在调用to_excel时会自动创建


def csv_to_xls(c_path, x_path):
    with open(c_path, 'r', encoding='gb18030', errors='ignore') as f:
        data = f.read()
    data_file = StringIO(data)
    print(data_file)
    csv_reader = csv.reader(data_file)
    list_csv = []
    index = 1
    out_path = x_path + str(index) + ".xls"
    # print(out_path)
    for row in csv_reader:
        list_csv.append(row)
        if len(list_csv) >= 65535:
            df_csv = pd.DataFrame(list_csv).applymap(str)
            '''
            这部分是不将csv装换为xls，而是过滤后再写入csv文件
            df_csv = df_csv[(df_csv[4] == '') | (df_csv[4] == 'name')]      # 过滤出第四列包含空值和name的数据
            df_csv.to_csv(csv_path, index=0, header=0, encoding='gb18030')  # 写入csv文件中
            '''
            out_path = x_path + str(index) + ".xls"
            writer = pd.ExcelWriter(out_path)
            # 写入Excel
            df_csv.to_excel(
                excel_writer=writer,
                index=False,
                header=False
            )
            writer.save()
            list_csv = []
            index +=1

    df_csv = pd.DataFrame(list_csv).applymap(str)
    '''
    这部分是不将csv装换为xls，而是过滤后再写入csv文件
    df_csv = df_csv[(df_csv[4] == '') | (df_csv[4] == 'name')]      # 过滤出第四列包含空值和name的数据
    df_csv.to_csv(csv_path, index=0, header=0, encoding='gb18030')  # 写入csv文件中
    '''
    out_path = x_path + str(index) + ".xls"
    writer = pd.ExcelWriter(out_path)
    # 写入Excel
    df_csv.to_excel(
        excel_writer=writer,
        index=False,
        header=False
    )
    writer.save()
    writer.close()
    # 删除csv文件
#os.remove(c_path)


csv_to_xls(c_path, x_path)