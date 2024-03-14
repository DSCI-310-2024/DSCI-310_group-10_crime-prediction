# Predict and Classify the appearance of criminal incidents based on historical incident reports (specifically 2023)

Authors: Cassandra Zhang, Ethan Kenny, James He, Pragya Singhal

Short Summary: \
Law enforcement agencies worldwide prioritize crime prevention and public safety, traditionally relying on experience and intuition for resource allocation. However, advancements in data analysis now enable a more data-driven approach. This analysis aims to predict the appearance of criminal incidents from time period, day of the week, and police district based on data from San Francisco 2023. Understanding time-related crime patterns can inform proactive policing strategies. By associating time periods, police districts, and days of the week with the appearance of criminal incidents, this study aims to provide a forecasting tool for police patrol scheduling and resource allocation, ultimately enhancing law enforcement activities and public safety.

How to run:

1. Clone the repository to your local machine using Git:
`git clone <https://github.com/DSCI-310-2024/DSCI310-group10-project.git>`
2. Create and Activate the Conda Environment containing important dependencies:
   `conda env create -f environment.yml`
    `conda activate group10_environment`
4. Launch JupyterLab either through Git or terminal on your computer.

5. Navigate to the root of the directory where `time_period_crime.ipynb` is located.

6. Open the `time_period_crime.ipynb` file in JupyterLab to access the analysis and execute the code.


List of Dependencies: 
- **NumPy**: `pip install numpy`
- **Pandas**: `pip install pandas`
- **Matplotlib**: `pip install matplotlib`
- **Scikit-learn**: `pip install scikit-learn`
- **Altair**: `pip install altair`

Names of Licenses: \
MIT License


## Makefile

### Generating HTML Files

To generate the files in HTML format, follow these steps:

Open the terminal window, then navigate to the root directory of the project using the command.
```
cd DSCI310-group10-project
```
Once in the directory, execute the command.
```
make all
```
This will create `time_period_crime` as an HTML file. Additionally, it will generate the necessary plots and graphs.

### Cleaning Up

To remove all generated files and clean up the project directory, use the command `make clean`. This will target and remove processed data, charts, the final report, and any other generated files.


