import pandas as pd
import altair as alt
import click
import os

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def create_visualization(input_path, output_path):
    # Read data from the input path
    data = pd.read_csv(input_path)
    
    # Save Visualization
    saveVisualization(data, output_path)

def saveVisualization(data, output_path):
    
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('coefficients:Q', title='Coefficient'),
        y=alt.Y('features:N', sort='-x', title='Feature'),
        color=alt.condition(
            alt.datum.coefficients > 0,
            alt.value("steelblue"),  # The positive color
            alt.value("orange")  # The negative color
        )
    ).properties(
        title={
            "text": ["Coefficients of Logistic Regression Model"], 
            "subtitle": ["Predicting the Likelihood of Criminal Incidents in San Francisco",
                     "Intercept: 0.8484733214216308"]
        },
        width=600,
        height=600
    )

    chart.save(output_path + '/coefficients_of_lr_model_plot.png')


if __name__ == '__main__':
    create_visualization()