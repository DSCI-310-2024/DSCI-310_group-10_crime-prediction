# author: Group 10
# date: 2024-04-09

"""
This script is used for creating visualizations of the initial dataset.
Two plots are created: a scatterplot and a bar plot.
The visualizations are saved as PNG files.

Usage: src/eda_visualizations.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>      Local file path to the processed data
--output_path=<output_path>    Local file path where the files are to be saved
"""


import pandas as pd
import altair as alt
import click
import os

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def create_visualizations(input_path, output_path):
    # Read data from the input path
    data = pd.read_csv(input_path)
    
    # Save Visualizations
    saveVisualizations(data, output_path)

def saveVisualizations(data, output_path):
    
    # visualize the distribution of incidents records based on time period
    time_period_dist = alt.Chart(data).mark_bar().encode(
        x = alt.X('time_period', title = 'Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
        ).configure_axisX(
        labelAngle=45
        ).properties(height = 150)

    time_period_dist.save(output_path + '/time_period_plot.png')

    # visualize the incident records based on the time period and day of the week
    day_time = alt.Chart(data).mark_point().encode(
        x = alt.X('time_period',title='Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
        ).properties(height = 150).facet(
        facet = alt.Facet('incident_day_of_week',title=None,
        ))#,
        #title = 'Incidents Records by Time Period & Day')

    day_time.save(output_path + '/records_by_time_and_day_plot.png')


if __name__ == '__main__':
    create_visualizations()