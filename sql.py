import sqlite3, pandas as pd

csv_path = ('workouts.csv')
csv_new = ('workouts(2).csv')

con = sqlite3.connect("workouts.db")
cur = con.cursor()

def CSV_Cleanup():
    # Delete unused columns from csv
    f = pd.read_csv(csv_path, usecols=[1,4,9,10])
    f.to_csv(csv_new, index=False)
    # Delete time from first column
    df = pd.read_csv(csv_new)
    df['start_time'] = df['start_time'].str[:-7]
    # Remove rows that contain 'treadmill'
    df = df[~df['exercise_title'].str.contains('Treadmill', na=False)]
    # Save new csv file
    df.to_csv(csv_new, index=False)

def Make_SQL():
    # turn the .csv into a .db
    df = pd.read_csv(csv_new)
    titles = []
    # Make a list of all exercises in sheet
    for cell in df['exercise_title']:
        if cell not in df['exercise_title']: 
            titles.append(cell)

Make_SQL()

