import pandas as pd
from datetime import datetime

def CSV_Cleanup(csv_path, csv_new):
    # Read CSV file and use specific columns
    df = pd.read_csv(csv_path, usecols=[1, 4, 9, 10])

    # Delete times from the 'start_time' column (leave dates)
    df['start_time'] = df['start_time'].str[:-7]

    # Remove rows that contain 'Treadmill'
    df = df[~df['exercise_title'].str.contains('Treadmill', na=False)]

    # Remove data prior to 2025
    df = df[~df['start_time'].str.contains('2024', na=False)]
    
    # Make new column for set volume
    df['set_volume'] = df['weight_lbs'] * df['reps']

    # Delete unused columns (weight_lbs, reps)
    df = df.drop("weight_lbs", axis='columns')
    df = df.drop("reps", axis='columns')

    # Convert start_time to DateTime
    df = df.rename(columns={"start_time": "date"})
    
    df['date'] = pd.to_datetime(df['date'], format='%d %b %Y')
    
    # Consolidate workouts per date (3 sets of x volume equals 1 day of y total volume)
    consolidated_df = df.groupby(['date', 'exercise_title']).agg({'set_volume': 'sum'}).reset_index()

    # Save the new CSV file
    consolidated_df.to_csv(csv_new, index=False)
