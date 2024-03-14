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
        )#.properties(title='The distribution of Time Period')

    time_period_dist.save(output_path + '/time_period_plot.png')

    # visualize the incident records based on the time period and day of the week
    day_time = alt.Chart(data).mark_point().encode(
        x = alt.X('time_period',title='Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
        ).properties(height = 150).facet(
        facet = alt.Facet('incident_day_of_week',title=None,
        )#,
        #title = 'Incidents Records by Time Period & Day'
        #)

    day_time.save(output_path + '/records_by_time_and_day_plot.png')


if __name__ == '__main__':
    create_visualizations()