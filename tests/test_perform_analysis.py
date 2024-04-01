import pandas as pd
import pytest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_perform_analysis import perform_analysis  

# Test data
iris_data = load_iris(return_X_y=True)
X_train, _, y_train, _ = train_test_split(iris_data[0], iris_data[1], test_size=0.3, random_state=123)

# Test for correct return type
def test_perform_analysis_returns_correct_type():
    result = perform_analysis(pd.DataFrame(X_train), pd.Series(y_train))
    assert isinstance(result, tuple), "Output should be a tuple"

    lr, dummy_results, cv_results_lr, viz_df = result
    assert isinstance(lr, LogisticRegression), "Logistic Regression model should be returned"
    assert isinstance(dummy_results, pd.DataFrame), "Dummy Classifier results should be a DataFrame"
    assert isinstance(cv_results_lr, pd.DataFrame), "Logistic Regression results should be a DataFrame"
    assert isinstance(viz_df, pd.DataFrame), "Visualization DataFrame should be a DataFrame"

# Test for correct output shape
def test_perform_analysis_output_shapes():
    result = perform_analysis(pd.DataFrame(X_train), pd.Series(y_train))
    lr, dummy_results, cv_results_lr, viz_df = result

    assert dummy_results.shape == (1, 4), "Dummy Classifier results DataFrame shape should be (1, 4)"
    assert cv_results_lr.shape == (1, 4), "Logistic Regression results DataFrame shape should be (1, 4)"
    assert viz_df.shape[1] == 2, "Visualization DataFrame should have 2 columns"

# Test for handling incorrect input types
def test_perform_analysis_handles_incorrect_input_types():
    with pytest.raises(TypeError):
        perform_analysis(X_train.tolist(), y_train)  # Passing list instead of DataFrame

    with pytest.raises(TypeError):
        perform_analysis(pd.DataFrame(X_train), y_train.tolist())  # Passing list instead of Series

    with pytest.raises(TypeError):
        perform_analysis(X_train, y_train)  # Passing numpy array instead of DataFrame and Series
