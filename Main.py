import openpyxl, path, FileConversion, products, convertreps
import removetreadmill, convertweight, consolidate

from openpyxl import Workbook, load_workbook

csvpath = path.csvpath
path = path.path
wb = load_workbook(path)
ws = wb.active




def main():
    
    
    # Convert file from csv to xlsx; delete unused columns; remove times from dates
    FileConversion.FileConversion(csvpath,path)
    print("File Conversion Done")
    wb.save(path)

    # Remove treadmill from file
    removetreadmill.RemoveTreadmill(ws,path)
    print("Treadmills Removed", flush=True)
    wb.save(path)

    # Convert  weight from strings to floats; convert NoneTypes to 0
    convertweight.ConvertWeight(ws,path)
    print("Weights Ready", flush=True)
    wb.save(path)

    # Convert reps from strings to floats
    convertreps.ConvertReps(ws,path)
    print("Reps Ready", flush=True)
    wb.save(path)

    # Get the volume of weight per set
    products.Products(ws,path)
    print("Set Volumes Calculated", flush=True)
    wb.save(path)

    # Consolidate
    consolidate.Consolidate(ws,path)
    print("Set Volumes Consolidated")

    # Exercises with the same title need to be graphed as the same color
    
    # Graph stuff here idk I haven't thought it through yet

if __name__ == "__main__":
    main()
