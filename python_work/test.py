import pandas as pd
import sys
from numpy.distutils.fcompiler import none
len_arg = len(sys.argv)
input_path = 'C:\\Users\\anran\\Desktop\\test.xlsx'
output_path = 'C:\\Users\\anran\\Desktop\\file\\'
default_sheet_name = "Sheet1"
columns_index = 0

if len_arg == 5:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    default_sheet_name = sys.argv[3]
    columns_index = int(sys.argv[4])

file = pd.read_excel(input_path, sheet_name=default_sheet_name)
menu = file.iloc[:, columns_index].drop_duplicates()
city = file.columns.T[columns_index]
for name in menu:
    df1 = file[file[city] == name]
    out_file = output_path + str(name) + ".xlsx"
    df1.to_excel(out_file, index=None)
