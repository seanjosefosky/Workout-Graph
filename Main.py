import openpyxl, path, fileconversion, products, convertreps, removetreadmill, convertweight, convertreps

from openpyxl import Workbook, load_workbook

csvpath = path.csvpath
path = path.path
wb = load_workbook(path)
ws = wb.active

def main():
    # Convert file from csv to xlsx; delete unused columns; remove times from dates
    fileconversion.FileConversion(csvpath,path)
    wb.save(path)
    # Remove treadmill from file
    removetreadmill.RemoveTreadmill(ws,path)
    wb.save(path)
    # Convert  weight from strings to floats; convert NoneTypes to 0
    convertweight.ConvertWeight(ws,path)
    wb.save(path)
    # Convert reps from strings to floats
    convertreps.ConvertReps(ws,path)
    wb.save(path)
    # Get the volume of weight per set

    # SUM volumes into one

    # Graph stuff here idk I haven't thought it through yet

if __name__ == "__main__":
    main()
