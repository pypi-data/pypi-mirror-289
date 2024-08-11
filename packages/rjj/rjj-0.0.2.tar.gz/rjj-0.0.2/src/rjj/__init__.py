# !/usr/bin/env python3

__version__="0.0.2"

import argparse, os
import pandas as pd

def jointer():
    csv_files = [f for f in os.listdir() if f.endswith('.csv') and f != 'output.csv']
    dataframes = []

    for file in csv_files:
        file_name = os.path.splitext(file)[0]
        df = pd.read_csv(file)
        df['File'] = file_name
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df[['File'] + [col for col in combined_df.columns if col != 'File']]
    combined_df.to_csv('output.csv', index=False)

    print("Combined CSV file saved as output.csv")

def spliter():
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]

    if csv_files:
        print("CSV file(s) available. Select which one to split:")
        
        for index, file_name in enumerate(csv_files, start=1):
            print(f"{index}. {file_name}")

        choice = input(f"Enter your choice (1 to {len(csv_files)}): ")
        
        try:
            choice_index=int(choice)-1
            selected_file=csv_files[choice_index]
            print(f"File: {selected_file} is selected!")
            df = pd.read_csv(selected_file)
            reference_field = df.columns[0]
            groups = df.groupby(reference_field)

            for file_id, group in groups:
                group = group.drop(columns=[reference_field]) 
                output_file = f'{file_id}.csv'
                group.to_csv(output_file, index=False)

            print("CSV files have been split and saved successfully.")

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
    else:
        print("No CSV files are available in the current directory.")
        input("--- Press ENTER To Exit ---")

def __init__():
    parser = argparse.ArgumentParser(description="rjj will execute different functions based on command-line arguments")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="choose a subcommand:")
    subparsers.add_parser('j', help='joint csv(s) together')
    subparsers.add_parser('s', help='split csv to piece(s)')

    args = parser.parse_args()
    if args.subcommand == 'j':
        jointer()
    elif args.subcommand == 's':
        spliter()
