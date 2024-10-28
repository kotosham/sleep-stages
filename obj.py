import pandas as pd
import glob
import os

script_name = 'obj.py'

current_directory = os.path.dirname(os.path.abspath(script_name))
path = os.path.join(current_directory, '*.xlsx')
excel_files = glob.glob(path)

dataframes = []

for file in excel_files:
    df = pd.read_excel(file)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)
combined_df.to_csv('data.csv', index=False)

print("создан файл data.csv")
