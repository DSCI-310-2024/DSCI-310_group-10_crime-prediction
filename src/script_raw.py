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

# Example usage:
# input_path = "url link"
# output_path = "../data/raw"
# script_raw(input_path, output_path)
