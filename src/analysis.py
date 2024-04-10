# author: Group 10
# date: 2024-04-09

"""This script is used for performing analysis and outputting data used for analysis visualization. It contains two functions: perform_analysis function creates the model, and analysis function saves the analyzed results.

Usage: src/analysis.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>      Local file path to a cleaned and preprocessed data
--output_path=<output_path>    Local file path where the file wants to be saved
"""

from sklearn.model_selection import train_test_split, cross_validate
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
import pandas as pd
import click


@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def analysis(input_path, output_path):
    # Read data from the input path
    data = pd.read_csv(input_path)

    X = data.drop(columns=['if_crime'])
    y = data['if_crime']

    lr, dummy_results, cv_results_lr = perform_analysis(X, y)

    # Save results
    dummy_results.to_csv(output_path + '/dummy_results.csv', index=False)
    cv_results_lr.to_csv(output_path + '/cross_validation_results.csv', index=False)

    # Save coefficients
    viz_df = saveCoefficients(X, lr, output_path)
    viz_df.to_csv(output_path + '/crime_coefficients.csv', index=False)


def perform_analysis(X, y):

    # Perform one-hot encoding with sparse representation
    X_encoded = pd.get_dummies(X, sparse=True)
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=123)  
    
    # Initialize classifiers
    dummy = DummyClassifier()
    lr = LogisticRegression()
    
    # Fit the classifiers
    dummy.fit(X_train, y_train)
    lr.fit(X_train, y_train)
    
    # Evaluate the classifier
    
    dummy_results = pd.DataFrame(cross_validate(dummy, X_train, y_train, return_train_score=True)).mean().to_frame().T
    dummy_results.columns = ['Fit Time', 'Score Time', 'Test Score', 'Train Score']

    cv_results_lr = pd.DataFrame(cross_validate(lr, X_train, y_train, return_train_score=True)).mean().to_frame().T
    cv_results_lr.columns = ['Fit Time', 'Score Time', 'Test Score', 'Train Score']
    
    viz_df = pd.DataFrame({"features": X_train.columns, "coefficients": lr.coef_[0]})


    return lr, dummy_results, cv_results_lr, viz_df



if __name__ == '__main__':
    analysis()