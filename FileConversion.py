import csv, openpyxl, path

csvpath = path.csvpath
path = path.path
wb = openpyxl.Workbook()
ws = wb.active


def FileConversion(cvp,xlp):
    with open(cvp) as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    wb.save(xlp)
    ws.delete_cols(1)
    ws.delete_cols(2,2)
    ws.delete_cols(3,2)
    ws.delete_cols(5,2)

    ws.delete_rows(1)

    wb.save(xlp)

    for cell in ws['A']:
        cell.value = cell.value[:-7]
        wb.save(xlp)

# FileConversion(csvpath,path)