import pandas as pd
import altair as alt
import click

@click.command()
@click.argument('data_file', type=click.Path(exists=True))
@click.argument('output_prefix', type=str)
def main(data_file, output_prefix):
    """Generate exploratory data visualizations."""
    # Load data
    data = pd.read_csv(data_file)

    # Generate summary
    print("Data Cardinality Summary:")
    data_cardinality(data)

    # Generate visualizations
    generate_visualizations(data, output_prefix)


def generate_visualizations(data, output_prefix):

    # Visualization 1
    time_period_dist = alt.Chart(data).mark_bar().encode(
        x = alt.X('time_period', title = 'Time Period', sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
    ).configure_axisX(
        labelAngle=45
    ).properties(title='Chart 1: The distribution of Time Period')

    chart1_file = output_prefix + '_chart1.png'
    time_period_dist.save(chart1_file)

    # Visualization 2
    day_time = alt.Chart(data).mark_point().encode(
        x = alt.X('time_period',title='Time Period',sort=['Morning', 'Afternoon','Evening','Night','Late Night']),
        y = alt.Y('count()', title = 'Count of Records')
    ).properties(height = 150).facet(
        facet = alt.Facet('incident_day_of_week',title=None),
        title = 'Chart 2: Incidents Records by Time Period & Day'
    )

    chart2_file = output_prefix + '_chart2.png'
    day_time.save(chart2_file)


def data_cardinality(data):
    for field in data.columns:
        print(field, '', data[field].nunique())
        if data[field].nunique() > 0:
            print(data[field].value_counts())
        print('********\n')


if __name__ == "__main__":
    main()
