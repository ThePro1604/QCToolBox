import os.path
from xlsx2csv import Xlsx2csv
from io import StringIO
import pandas as pd


def read_excel(path: str, sheet_name: str) -> pd.DataFrame:
    buffer = StringIO()
    Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer)
    buffer.seek(0)
    df = pd.read_csv(buffer)
    return df


manual_remarks = []
notes = []
header_row = []

file_path = 'N:/Images/Shahaf/Instinct.csv'
file_name = file_path[file_path.rfind("/") + 1:file_path.rfind(".xlsx")]
folder_path = file_path[:file_path.rfind("/")]
csv = os.path.join(folder_path, "Instinct.csv")

if '.xlsx' in file_path:
    df = read_excel(file_path, file_name)
else:
    df = pd.read_csv(file_path)

# for i in range(len(df.columns)):
#     header_row.append(list(df[df.columns[i]].values)[0])
header_row = df.columns.values.tolist()
if 'Manual Remarks' not in header_row:
    df['Manual Remarks'] = pd.Series([], dtype=pd.StringDtype())
    df = df.fillna(" ")
    print("test")
if 'Notes' not in header_row:
    df['Notes'] = pd.Series([], dtype=pd.StringDtype())
    df = df.fillna(" ")
    print("test")

# print(df.lookup(df[df['Douments count'] == 78].index, ['Notes']))
# # print(df.locas(df[df['Douments count'] == 78].index, ['Notes']))
# df.to_csv(csv, index=False, encoding='utf-8')
# # print(df.loc(df[df['Douments count']==78].index))
# print(df[df['Douments count'] == 78].index.values)
# print(df[df['Douments count'] == 78].index)
# print(df[df['Douments count'] == 78].index[0])
# df.iloc[df[df['Douments count'] == 78].index[0], df.columns.get_loc('Notes')] = "aaa"
# print(df.iloc[df[df['Douments count'] == 78].index[0], df.columns.get_loc('Notes')])
# df.to_csv(csv, index=False, encoding='utf-8')

