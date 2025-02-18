import openpyxl, path, fileconversion, products, integerconversions, removetreadmill, consolidate

from openpyxl import Workbook, load_workbook

csvpath = path.csvpath
path = path.path



def main():
    
    # Convert file from csv to xlsx; delete unused columns; remove times from dates
    fileconversion.FileConversion(csvpath,path)
    print("File Conversion Done")

    wb = load_workbook(path)
    ws = wb.active

    # Remove treadmill from file
    removetreadmill.RemoveTreadmill(ws,path)
    print("Treadmills Removed", flush=True)
    wb.save(path)

    # Converts data from strings to floats; convert NoneTypes to 0
    integerconversions.ConvertToInt(ws,path)
    print("Integers converted", flush=True)
    wb.save(path)
    
    # Get the volume of weight per set
    products.Products(ws,path)
    print("Set Volumes Calculated", flush=True)
    wb.save(path)

    # TODO: Consolidate might need a different data structure.

    # Consolidate
    consolidate.Consolidate(ws)
    print("Set Volumes Consolidated")

    # Exercises with the same title need to be graphed as the same color
    
    # Graph stuff here idk I haven't thought it through yet

if __name__ == "__main__":
    main()
