import csv, openpyxl

path = 'C:/Users/xsoup/Downloads/workouts.csv'
wb = openpyxl.Workbook()
ws = wb.active


with open(path) as f:
    reader = csv.reader(f)

    for row in reader:
        ws.append(row)

wb.save('workouts.xlsx')