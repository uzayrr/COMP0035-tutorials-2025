def main():
    tutorial_201()

def tutorial_201():
    from pathlib import Path

    #Line below goes to the parent folder of the current file
    solutions_root = Path(__file__).parent
    #Line below goes to the parent folder of the solutions folder
    solutions_root_root = Path(solutions_root).parent

    #Goes into the folder, into data folder, and then to the csv file
    csv_file = solutions_root_root.joinpath("data", "paralympics_raw.csv")

    #Checks if the file exists, if so, it prints 'CSV file found' and the path
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")

if __name__ == "__main__":
    main()

