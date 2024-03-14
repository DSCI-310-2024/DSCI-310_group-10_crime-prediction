import pandas as pd
import altair as alt
import click

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def create_visualizations(input_path, output_path):
    # Read data from the input path
    data = pd.read_csv(input_path)
    
    # Perform data cleaning and preprocessing
    visualizations = getVisualizations(data)

    # Save visualizations to figures
    for i in range(len(visualizations)):
        visualizations[i].save(f'{output_path}/chart{i + 1}.png')

def getVisualizations(data):

    visualizations = []
    
    # visualize the distribution of incidents records based on time period
    time_period_dist = alt.Chart(data).mark_bar().encode(
        x = alt.X('time_period', title = 'Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
        ).configure_axisX(
        labelAngle=45
        ).properties(title='Chart 1: The distribution of Time Period')

    visualizations.append(time_period_dist)

    # visualize the incident records based on the time period and day of the week
    day_time = alt.Chart(data).mark_point().encode(
        x = alt.X('time_period',title='Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
        ).properties(height = 150).facet(
        facet = alt.Facet('incident_day_of_week',title=None,
        ),
        title = 'Chart 2: Incidents Records by Time Period & Day'
        )

    visualizations.append(day_time)

    return visualizations


if __name__ == '__main__':
    create_visualizations()