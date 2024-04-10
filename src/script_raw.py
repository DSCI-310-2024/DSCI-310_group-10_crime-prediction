# author: Group 10
# date: 2024-04-09

"""Downloads data csv data from the web to a local filepath as a csv file.

Usage: src/script_raw.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>      URL link of the dataset from the web or local file path
--output_path=<output_path>    Local file path where the file wants to be saved
"""

import pandas as pd
import click

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def main(input_path, output_path):
    # Read data from the input path
    raw_data = pd.read_csv(input_path, parse_dates=['incident_datetime'])
    
    # Save the data to the output path
    raw_data.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()
