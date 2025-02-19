import path, data, graph

def main():
    # Clean the original csv file
    data.CSV_Cleanup(path.csv_path, path.csv_new)

    # Plot the new csv data
    graph.Graph()

if __name__ == "__main__":
    main()
