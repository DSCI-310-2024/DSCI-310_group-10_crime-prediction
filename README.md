# Predict and Classify the appearance of criminal incidents based on historical incident reports (specifically 2023)

Authors: Cassandra Zhang, Ethan Kenny, James He, Pragya Singhal

Short Summary: \
Law enforcement agencies worldwide prioritize crime prevention and public safety, traditionally relying on experience and intuition for resource allocation. However, advancements in data analysis now enable a more data-driven approach. This analysis aims to predict the appearance of criminal incidents from time period, day of the week, and police district based on data from [San Francisco 2023]( https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783/about_data). Understanding time-related crime patterns can inform proactive policing strategies. By associating time periods, police districts, and days of the week with the appearance of criminal incidents, this study aims to provide a forecasting tool for police patrol scheduling and resource allocation, ultimately enhancing law enforcement activities and public safety.

## How to run (Virtual Environment):

1. Clone the repository to your local machine using Git:
`git clone <https://github.com/DSCI-310-2024/DSCI310-group10-project.git>`
2. Create and Activate the Conda Environment containing important dependencies:
   `conda env create -f environment.yml`
    `conda activate group10_environment`
4. Launch JupyterLab either through Git or terminal on your computer.

5. Navigate to the root of the directory where `time_period_crime.ipynb` is located.

6. Open the `time_period_crime.ipynb` file in JupyterLab to access the analysis and execute the code.

## How to run (Docker Container):

1. Clone the repository to your local machine using Git:
`git clone <https://github.com/DSCI-310-2024/DSCI310-group10-project.git>`

2. Open terminal and navigate to DSCI310-group10-project directory

Note: Make sure Docker Desktop is installed and running in the background

4. Run `docker-compose build`, this will create a docker image

5. Run `docker-compose up` and click the last link provided to open Jupyter Lab (or the command used to pull the docker image `docker pull ekenny02/dsci310-group10-project`)

6. Necessary files found withing the `work` directory

7. To shut down and exit container use `Crtl + c`

8. Removing volumes, images, containers, open another window in terminal and run `docker-compose down --rmi all --volumes --remove-orphans`

Makefile (for creating HTML and PDF Files)

To generate the files in HTML and PDF format, follow these steps:

Once you have started Jupyter Lab using docker-compose up and accessed it through the provided link, open a new terminal window in Jupyter Notebook and run the following command:
```
make all
```
This will create `time_period_crime` as an HTML and PDF file. Additionally, it will generate the necessary plots and graphs.

Cleaning Up

To remove all generated files and clean up the project directory, use the command `make clean`. This will target and remove processed data, charts, the final report, and any other generated files.

## Running tests for functions in data analysis

To run tests for functions in data analysis using pytest, follow these steps:

- Open terminal
- Navigate to the root directory of your project where the `tests` directory is located.
- Run the following command:
    ```bash
    pytest tests/*
    ```
    This command tells pytest to run all tests in the `tests` directory and its subdirectories.
- After executing the command, pytest will run all test files (`test_*.py`) within the specified directory.
- This will output any passed or failed tests.



## List of Dependencies: 
- **NumPy**: `pip install numpy`
- **Pandas**: `pip install pandas`
- **Matplotlib**: `pip install matplotlib`
- **Scikit-learn**: `pip install scikit-learn`
- **Altair**: `pip install altair`
- **Altair Saver**: `pip install altair_saver`
- **Click**: `pip install click`
- **Pytest**: `pip install pytest`
- **Vl Convert**: `pip install vl-convert-python`
- **Tabulate**: `pip install tabulate`

## Names of Licenses:
MIT License


