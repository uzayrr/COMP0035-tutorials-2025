def main():
    csv_df, xlsx_df1, xlsx_df2 =tutorial_202()
    tutorial_203(csv_df)

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

def tutorial_202():
    from pathlib import Path
    import pandas as pd

    #Line below goes to the parent folder of the current file
    solutions_root = Path(__file__).parent
    #Line below goes to the parent folder of the solutions folder
    solutions_root_root = Path(solutions_root).parent

    #Goes into the folder, into data folder, and then to the csv file
    csv_file = solutions_root_root.joinpath("data", "paralympics_raw.csv")
    xlsx_file = solutions_root_root.joinpath("data", "paralympics_all_raw.xlsx")

    #converts to dataframes, does it for each sheet in xlsx
    csv_df = pd.read_csv(csv_file)
    xlsx_df1 = pd.read_excel(xlsx_file, sheet_name=0)
    xlsx_df2 = pd.read_excel(xlsx_file, sheet_name=1)

    return(csv_df, xlsx_df1, xlsx_df2)

def tutorial_203(dataframe):
    '''Summary of description of function here
    
    Parameters:
    dataframe (dataframe): dataframe
    
    Returns:
    str: Description of the dataframes
    '''

    import pandas as pd

    print(dataframe.shape)
    pd.set_option("display.max_columns", None)
    print(dataframe.head)
    print(dataframe.tail)
    print(dataframe.columns)
    print(dataframe.dtypes)
    print(dataframe.info)
    print(dataframe.describe)


if __name__ == "__main__":
    main()

