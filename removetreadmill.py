import openpyxl, path

from openpyxl import Workbook, load_workbook

wb = load_workbook(path.path)
ws = wb.active

def RemoveTreadmill(wsheet,xlp):
        for row in wsheet.iter_rows(min_col=2, max_col=2):
                for cell in row:
                        if cell.value == "Treadmill":
                                ws.delete_rows(cell.row)
                                continue
                        wb.save(xlp)
                                
                                    
                        
# RemoveTreadmill(ws,path.path)
