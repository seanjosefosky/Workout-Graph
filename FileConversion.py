import csv, openpyxl
from pandas.io.parsers import read_csv

# CSV - remove empty columns
path = 'C:/Users/xsoup/Downloads/workouts.csv'
data = read_csv(path)
filtered_data = data.dropna(axis='columns', how='all')
path = filtered_data.to_csv('workouts.csv', index=False)


# Convert CSV file to XLSX
wb = openpyxl.Workbook()
ws = wb.active

with open('workouts.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        ws.append(row)

wb.save('workouts.xlsx')