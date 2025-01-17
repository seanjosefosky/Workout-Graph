import openpyxl, path

from openpyxl import Workbook, load_workbook

path = path.path
wb = load_workbook(path)
ws = wb.active


def Products(ws):
    for row in ws.iter_rows():
        weight = 0
        reps = 0
        for cell in row:
            match cell.column_letter:
                case 'C': weight = cell.value
                case 'D': reps = cell.value
        ws['E'] = weight*reps
        wb.save(path)
        break
