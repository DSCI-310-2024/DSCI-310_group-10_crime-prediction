# author: Group 10
# date: 2024-04-09

"""
This script is used for processing the data. It removes unused features and columns with missing data from the dataset. 
It prepares the dataset for analysis and EDA visualizations.
The processed data is saved as a CSV file.

Usage: src/script_processed.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>      Local file path to the raw data
--output_path=<output_path>    Local file path where the processed data will be saved
"""


import pandas as pd
import click

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def clean_and_process_data(input_path, output_path):
    # Read data from the input path
    raw_data = pd.read_csv(input_path)
    
    # Perform data cleaning and preprocessing
    processed_data = preprocess_data(raw_data)
    
    # Save the cleaned data to the output path
    processed_data.to_csv(output_path, index=False)


def get_time_period(hour, minute):
    if 0 < hour < 6 or (hour == 6 and minute == 0):
        return 'Late Night'
    elif 6 < hour < 12 or (hour == 6 and minute > 0) or (hour == 12 and minute == 0):
        return 'Morning'
    elif 12 < hour < 18 or (hour == 12 and minute > 0) or (hour == 18 and minute == 0):
        return 'Afternoon'
    elif 18 < hour < 21 or (hour == 18 and minute > 0) or (hour == 21 and minute == 0):
        return 'Evening'
    else:
        return 'Night'
    

def preprocess_data(data):
    data['incident_datetime'] = pd.to_datetime(data['incident_datetime'], errors='coerce')
    # Isolate necessary features
    data = data[['incident_datetime', 'incident_time', 'incident_day_of_week',
                 'incident_category', 'incident_subcategory', 'police_district']]
    


    # Add hour and minute features
    data = data.assign(hour=data['incident_datetime'].dt.hour,
                       minute=data['incident_datetime'].dt.minute)
    
    # Add feature identifying time period
    data = data.assign(time_period=data.apply(lambda row: get_time_period(row['hour'], row['minute']), axis=1))
    
    # Add feature to classify criminal incidents
    data = add_if_crime_feature(data)
    
    # Isolate necessary features for modeling
    data = data[['incident_day_of_week', 'police_district', 'time_period', 'if_crime']]
    
    return data

def add_if_crime_feature(data):
    criminal_incident = ["Larceny - From Vehicle", "Vandalism", "Larceny Theft - Other", "Motor Vehicle Theft",             
                        "Simple Assault", "Drug Violation", "Aggravated Assault", "Fraud", "Theft From Vehicle",                  
                        "Burglary - Other", "Weapons Offense", "Intimidation", "Warrant", "Larceny - Auto Parts",                
                        "Other Offenses", "Larceny Theft - From Building", "Larceny Theft - Shoplifting",         
                        "Robbery - Other", "Burglary - Residential", "Robbery - Street",                    
                        "Traffic Violation Arrest", "Robbery - Commercial", "Larceny Theft - Pickpocket", "Forgery And Counterfeiting",           
                        "Motor Vehicle Theft (Attempted)", "Burglary - Hot Prowl", "Prostitution",                         
                        "Burglary - Commercial", "Disorderly Conduct", "Arson",                                
                        "Larceny Theft - Bicycle", "Embezzlement",                         
                        "Extortion-Blackmail", "Sex Offense"] 
    
    data['if_crime'] = data['incident_subcategory'].apply(lambda x: 1 if x in criminal_incident else 0)
    return data

if __name__ == '__main__':
    clean_and_process_data()
