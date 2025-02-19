import random, path
import pandas as pd
import matplotlib.pyplot as plt

def Graph():
    # Data
    csv = path.csv_new
    df = pd.read_csv(csv)

    date = df['date']
    exercise = df['exercise_title']
    volume = df['set_volume']

    # Graphing
    # # Sort data by date
    df = df.sort_values(by='date')
                        
    # Group data by exercise_title
    grouped = df.groupby('exercise_title')

    # Create a plot
    fig, ax = plt.subplots()

    # Plot each exercise's data
    for name, group in grouped:
        ax.plot(group['date'], group['set_volume'], marker='o', linestyle='-', label=name)
        # print(group)

    # Graph UI
    ax.legend()

    ax.set_title('Workout Progression')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume (lbs)')

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
    