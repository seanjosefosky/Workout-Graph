import openpyxl, path

from openpyxl import Workbook, load_workbook

wb = load_workbook(path.path)
ws = wb.active
wb2 = Workbook()
ws2 = wb2.active

for row in ws.iter_rows(min_col=2, max_col=2):
    for cell in row:
        if cell.value == "Treadmill":
            ws.delete_rows(row)
            wb.save(path.path)