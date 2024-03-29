# test_add_if_crime.py

import pandas as pd
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_add_if_crime import add_if_crime_feature

# Test data
test_data1 = pd.DataFrame({
    "incident_subcategory": ["Vandalism", "Fraud", "Robbery - Street"]
})
test_data2 = pd.DataFrame({
    "incident_subcategory": ["Theft", "Assault"]
})
test_data3 = pd.DataFrame({
    "no_subcategory": ["Vandalism", "Fraud"]
})
test_data_boundary = pd.DataFrame({
    "incident_subcategory": ["Robbery - Commercial", "Simple Assault", "Burglary - Residential", "Theft From Vehicle", "Traffic Violation Arrest"]
})
test_not_string = pd.DataFrame({
    "incident_subcategory": [1, 2]  # non-string values
})
test_not_dataFrame = "This is not a DataFrame"

# Expected outputs
case1_output = pd.DataFrame({
    "incident_subcategory": ["Vandalism", "Fraud", "Robbery - Street"],
    "if_crime": [1, 1, 1]
})
case2_output = pd.DataFrame({
    "incident_subcategory": ["Theft", "Assault"],
    "if_crime": [0, 0]
})
case3_output = "Please insert correct datatype with incident category"
boundary_output = pd.DataFrame({
    "incident_subcategory": ["Robbery - Commercial", "Simple Assault", "Burglary - Residential", "Theft From Vehicle", "Traffic Violation Arrest"],
    "if_crime": [1, 1, 1, 1, 0]
})


# test for correct return type
def test_add_if_crime_returns_dataFrame():
    result = add_if_crime_feature(test_data1)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame"

# test for correct output for different cases
# case1: crime_subcategory is in incident_category
# case2: crime_subcategory is not in criminal_incident
def test_add_if_crime_output():
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data1), case1_output)
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data2), case2_output)

# Test for correcting handling for dataFrame with missing crime_incident column
def test_add_if_crime_contains_incident_subcategory():
    assert add_if_crime_feature(test_data3) == case3_output, "Expected error message when incident_category column is missing"

# Test function for boundary values
def test_add_if_crime_boundary():
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data_boundary), boundary_output)

# Test for correct error handling for incorrect type of column value 
# (not a string)
def test_add_if_crime_not_string():
    with pytest.raises(TypeError):
        add_if_crime_feature(test_not_string)

# Test for correct error handling for incorrect object type 
# (not a pandas data frame)
def test_non_dataframe_input_handling():
    with pytest.raises(AttributeError):
        add_if_crime_feature(test_not_dataFrame)