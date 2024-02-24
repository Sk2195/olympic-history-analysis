import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_athlete_file(cur, filepath):
    # Process the athlete file and insert data into the athlete table
    df = pd.read_csv(filepath)
    
    # Extract year from the 'Games' column if it exists, otherwise assume it's in a 'Year' column
    if 'Games' in df.columns:
        df['Year'] = df['Games'].str.extract('(\d{4})').astype(int)
        df.drop(columns=['Games'], inplace=True)  # Drop the 'Games' column
    
    for index, row in df.iterrows():
        athlete_data = (row['ID'], row['Name'], row['Sex'], row['Age'],
                        row['Height'], row['Weight'], row['Team'], row['NOC'],
                        row['Year'], row['Season'], row['City'],
                        row['Sport'], row['Event'], row['Medal'])
        cur.execute(athlete_table_insert, athlete_data)

def process_noc_file(cur, filepath):
    # Process the noc file and insert data into the noc_regions table
    df = pd.read_csv(filepath)
    
    for index, row in df.iterrows():
        noc_data = (row['NOC'], row['region'], row['notes'])
        cur.execute(noc_regions_table_insert, noc_data)

def process_data(cur, conn, filepath, process_func):
    """
    Walks through all files nested under filepath, and processes all files found.
    Parameters:
        cur (psycopg2.cursor()): Cursor of the olympics database
        filepath (str): Filepath parent of the logs to be analyzed
        process_func (python function): Function to be used to process each file
    Returns:
        Name of files processed
    """
    
    # Get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.csv'))  
        for f in files:
            all_files.append(os.path.abspath(f))
    
    # Get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    
    # Iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        process_func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
    
    return all_files
    
def main():
    """
    Main ETL process
    """
    conn = psycopg2.connect('host=localhost port=5433 dbname=olympicsdb user=postgres password=123456')
    cur = conn.cursor()

    # Define your file paths
    athlete_data_path = r'C:\Users\chimi\Desktop\Data Engineering\olympics_dataset\data\athlete'
    noc_data_path = r'C:\Users\chimi\Desktop\Data Engineering\olympics_dataset\data\noc_regions'

    # Process each file with the appropriate function
    process_data(cur, conn, athlete_data_path, process_athlete_file)
    process_data(cur, conn, noc_data_path, process_noc_file)

    conn.close()

if __name__ == '__main__':
    main()


