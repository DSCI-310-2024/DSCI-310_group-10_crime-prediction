# Predict the appearance of criminal incidents based on historical incident reports (specifically 2023)

Authors: Cassandra Zhang, Ethan Kenny, James He, Pragya Singhal

## About

Law enforcement agencies worldwide prioritize crime prevention and public safety, traditionally relying on experience and intuition for resource allocation. However, advancements in data analysis now enable a more data-driven approach. We will use [San Francisco 2023 data](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783/about_data) to understand time-related crime patterns that would potentially inform proactive policing strategies. As a group, we attempt to use logistical regression to predict whether it would be a crime occurring, or not. We will use explanatory variables such as incident_day_of_week (Monday - Sunday), police_district, and time_period. And predict on target if_crime (0 there will not be crime, 1 there will be crime). Our final logistic regression model predicts a test accuracy score of 0.8. Using the dummy classifier as a sanity check, we obtained a test accuracy score of 0.58. In our findings, the predictions indicate that Sundays have a lower likelihood of criminal incidents, with a significant negative coefficient. Police districts between Mission and Park have the highest likelihood of criminal incidents. Additionally, crime occurs most frequently during late-night time periods.

The dataset used in this project is filed by officers or by self-reported by members of the public using [SFPD's Online Reporting System](https://www.sanfranciscopolice.org/get-service/police-reports), and published by the San Francisco Police Department. It was reviewed and approved by a supervising Sergeant or Lieutenant. The dataset is sourced from [here](https://www.sanfranciscopolice.org/), which is licensed under [Open Data Commons](https://opendatacommons.org/licenses/pddl/1-0/). The columns category, incident date is the date and time when the incident occurred, incident time is the time of the incident occurred. More information on the column variables can be found in this [link](https://datasf.gitbook.io/datasf-dataset-explainers/sfpd-incident-report-2018-to-present#field-definitions). Each row in the dataset corresponds to a specific incident ID or incident number. Not all incident numbers are associated with a crime; for example, incidents that do not occur in the incident_category column, we do not consider that as a crime in this report (e.g., if a missing child is found).

## Report
The final report can be found [here](https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction/blob/main/reports/quarto_reports.qmd).

## Usage

1. Clone the repository to your local machine using Git:
`git clone https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction.git`

2. Open terminal and navigate to DSCI-310_group-10_crime-prediction directory.

Note: Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running in the background

3. Run `docker-compose build`, this will create a docker image.

4. Run `docker-compose up` and copy and paste the last link to your browser to open JupyterLab (or the command used to pull the docker image `docker pull ekenny02/dsci310-group10-project`)

5. Necessary files found within the `work` directory.

6. To shut down and exit the container use `Crtl + c`.

7. Removing volumes, images, containers, open another window in terminal and run `docker-compose down --rmi all --volumes --remove-orphans`, or run it in the existing terminal after step 6 `Ctrl + c`.

### Makefile (for creating HTML and PDF Files)

To generate the files in HTML and PDF format, follow these steps:

Once you have started JupyterLab using `docker-compose up` and accessed it through the provided link, open a new terminal window in JupyterLab, navigate to the root of the project directory `cd work` where makefile is located and run the following command:
```
make all
```
This will create __quarto_reports__ as an HTML and PDF file. Additionally, it will generate the necessary plots and graphs.

### Cleaning Up

To remove all generated files and clean up the project directory, navigate to the root of the project directory where makefile is located and run `make clean`. This will target and remove processed data, charts, the final report, and any other generated files.

### Running tests for functions in data analysis

To run tests for functions in data analysis using pytest, follow these steps:

1. Open a new terminal in Jupyter Lab after building the Docker container ([instructions](https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction/blob/main/reports/quarto_reports.qmd) on "Usage" include steps to accessing Jupyter Lab).
2. Navigate to the root directory of the project, `cd work`, where the tests directory is located.

Note: The functions will be in the [src](https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction/tree/main/src) directory e.g. __function_time_period.py__, the tests will be in [tests]([https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction/tree/main/tests) directory e.g. __test_time_period.py__.

3. Run the following command:
    ```bash
    pytest tests/*
    ```
    This command tells pytest to run all tests in the `tests` directory and its subdirectories.
   
4. After executing the command, pytest will run all test files (`test_*.py`) within the specified directory.
5. This will output any passed or failed tests.


## Dependencies

| Package           | Version   |
|-------------------|-----------|
| altair            | 5.2.0     |
| altair_saver      | 0.1.0     |
| click             | 8.1.7     |
| numpy             | 1.26.4    |
| pandas            | 2.2.1     |
| scikit-learn      | 1.4.1.post1 |
| pytest            | 8.1.1     |
| vl-convert-python | 1.3.0     |
| tabulate          | 0.9.0     |

If this information is outdated, please visit [Dockerfile](https://github.com/DSCI-310-2024/DSCI-310_group-10_crime-prediction/blob/main/Dockerfile) for the most current dependencies.


## License
The Time Period Crime materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References
San Francisco Police Department. "Police Department Incident Reports: 2018 to Present." San Francisco Governmnet, DataSF: Public-Safety. https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783/about_data.

San Francisco Police Department. "SFPD Incident Report: 2018 to present." San Francisco GOvernment, DataSF: datasf-dataset-explainers. https://datasf.gitbook.io/datasf-dataset-explainers.



