# Predict and Classify the appearance of criminal incidents based on historical incident reports (specifically 2023)

Authors: Cassandra Zhang, Ethan Kenny, James He, Pragya Singhal

## Short Summary:
Law enforcement agencies worldwide prioritize crime prevention and public safety, traditionally relying on experience and intuition for resource allocation. However, advancements in data analysis now enable a more data-driven approach. This analysis aims to predict the appearance of criminal incidents from time period, day of the week, and police district based on data from [San Francisco 2023]( https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783/about_data). Understanding time-related crime patterns can inform proactive policing strategies. By associating time periods, police districts, and days of the week with the appearance of criminal incidents, this study aims to provide a forecasting tool for police patrol scheduling and resource allocation, ultimately enhancing law enforcement activities and public safety.

## How to run (Virtual Environment):

1. Clone the repository to your local machine using Git:
`git clone <https://github.com/DSCI-310-2024/DSCI310-group10-project.git>`
2. Create and Activate the Conda Environment containing important dependencies:
   `conda env create -f environment.yml`
    `conda activate group10_environment`
4. Launch JupyterLab either through Git or terminal on your computer `jupyter lab`.

5. Navigate to the root of the directory where __time_period_crime.ipynb__ is located.

6. Open the __time_period_crime.ipynb__ file in JupyterLab to access the analysis and execute the code.

## How to run (Docker Container):

1. Clone the repository to your local machine using Git:
`git clone <https://github.com/DSCI-310-2024/DSCI310-group10-project.git>`

2. Open terminal and navigate to DSCI310-group10-project directory.

Note: Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running in the background

3. Run `docker-compose build`, this will create a docker image.

4. Run `docker-compose up` and copy and paste the last link to your browser to open JupyterLab (or the command used to pull the docker image `docker pull ekenny02/dsci310-group10-project`)

5. Necessary files found within the `work` directory.

6. To shut down and exit the container use `Crtl + c`.

7. Removing volumes, images, containers, open another window in terminal and run `docker-compose down --rmi all --volumes --remove-orphans`, or run it in the existing terminal after step 6 `Ctrl + c`.

### Makefile (for creating HTML and PDF Files)

To generate the files in HTML and PDF format, follow these steps:

Once you have started JupyterLab using `docker-compose up` and accessed it through the provided link, open a new terminal window in Jupyter Notebook, navigate to the root of the project directory `cd work` where makefile is located and run the following command:
```
make all
```
This will create __quarto_reports__ as an HTML and PDF file. Additionally, it will generate the necessary plots and graphs.

### Cleaning Up

To remove all generated files and clean up the project directory, navigate to the root of the projecr directory where makefile is located and run `make clean`. This will target and remove processed data, charts, the final report, and any other generated files.

### Running tests for functions in data analysis

To run tests for functions in data analysis using pytest, follow these steps:

1. Open a new terminal in Jupyter Lab after building the Docker container (instructions on "how to run Docker container" include steps to accessing Jupyter Lab).
2. Navigate to the root directory of the project, `cd work`, where the tests directory is located.

Note: The functions will be in the [src](https://github.com/DSCI-310-2024/DSCI310-group10-project/tree/main/src) directory e.g. __function_time_period.py__, the tests will be in [tests](https://github.com/DSCI-310-2024/DSCI310-group10-project/tree/main/tests) directory e.g. __test_time_period.py__.

3. Run the following command:
    ```bash
    pytest tests/*
    ```
    This command tells pytest to run all tests in the `tests` directory and its subdirectories.
   
4. After executing the command, pytest will run all test files (`test_*.py`) within the specified directory.
5. This will output any passed or failed tests.



## List of Dependencies: 
Specific denependencies and versions can be found inside [Dockerfile](https://github.com/DSCI-310-2024/DSCI310-group10-project/blob/main/Dockerfile).

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


