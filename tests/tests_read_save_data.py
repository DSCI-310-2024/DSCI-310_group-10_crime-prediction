import pandas as pd
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_read_save_data import read_save_data

# valid url and output path test
valid_input_path_1 = '../data/raw/raw_data.csv'
valid_output_path_1 = '../data/raw/test_1_raw_data.csv'

# invalid url and output path test
invalid_path_1 = ''

# test for valid input and outputs
def test_read_save_data_correct():
    read_save_data(valid_input_path_1, valid_output_path_1)
    assert os.path.exists(valid_output_path_1)

    original_data = pd.read_csv(valid_input_path_1)
    new_data = pd.read_csv(valid_output_path_1)

    assert new_data.equals(original_data)

# test for correct path error handling
def test_read_save_data_path_error():
    with pytest.raises(FileNotFoundError):
        read_save_data(invalid_path_1, valid_output_path_1)
    with pytest.raises(FileNotFoundError):
        read_save_data(valid_input_path_1, invalid_path_1)
    with pytest.raises(FileNotFoundError):
        read_save_data(invalid_path_1, invalid_path_1)
     
# test for correct type error handling
def test_read_save_data_type_error():
    with pytest.raises(TypeError, match=r'both input_path and output_path should be strings'):
        read_save_data(1, valid_output_path_1)
    with pytest.raises(TypeError, match=r'both input_path and output_path should be strings'):
        read_save_data(valid_input_path_1, 2)
    with pytest.raises(TypeError, match=r'both input_path and output_path should be strings'):
        read_save_data(3, 4)