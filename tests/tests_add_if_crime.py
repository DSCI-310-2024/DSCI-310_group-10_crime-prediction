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
    "incident_subcategory": ["Robbery - Commercial"]
})



# Expected outputs
case1_output = pd.DataFrame({
    "incident_subcategory": ["Vandalism", "Fraud", "Robbery - Street"],
    "if_crime": [1, 1, 1]
})
case2_output = pd.DataFrame({
    "incident_subcategory": ["Theft", "Assault"],
    "if_crime": [0, 0]
})
boundary_output = pd.DataFrame({
    "incident_subcategory": ["Robbery - Commercial"],
    "if_crime": [1]
})




# test for correct return type
def test_add_if_crime_returns_dataFrame():
    result = add_if_crime_feature(test_data1)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame"

# test for correct output for different cases
# case1: incident_subcategory value is in the list of criminal_incident
# case2: incident_subcategory value is not in the list of criminal_incident
def test_add_if_crime_output():
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data1), case1_output)
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data2), case2_output)

# Test for correcting handling for dataFrame with missing crime_incident column
def test_add_if_crime_contains_incident_subcategory():
    with pytest.raises(KeyError):
        add_if_crime_feature(test_data3)

# Test function for boundary values
def test_add_if_crime_boundary():
    pd.testing.assert_frame_equal(add_if_crime_feature(test_data_boundary), boundary_output)


# Test for correct error handling for incorrect object type 
# (not a pandas data frame)
def test_non_dataframe_input_handling():
    with pytest.raises(TypeError, match="Input data should be a pandas DataFrame"):
        add_if_crime_feature(test_not_dataFrame)
