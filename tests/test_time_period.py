import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_time_period import get_time_period

# morning test
h1_m = 6
m1_m = 1
h7_m = 12 # boundary values
m7_m = 0 # boundary valeus

# afternoon test
h2_a = 14
m2_a = 25
h8_a = 18 # boundary values
m8_a = 0 # boundary values

# evening test
h3_e = 20
m3_e = 3
h9_e = 21 # boundary values
m9_e = 0 # boundary values

# night test
h4_n = 23
m4_n = 12
h10_n = 0 # boundary values
m10_n = 0 # boundary values

# late night test
h5_ln = 2
m5_ln = 10
h6_ln = 6 # boundary values 
m6_ln = 0 # boundary values


# regular outputs
output_m = 'Morning'
output_a = 'Afternoon'
output_e = 'Evening'
output_n = 'Night'
output_ln = 'Late Night'


# test for correct output type
def test_get_time_period_returns_str():
    result = get_time_period(h1_m, m1_m)
    assert isinstance(result, str)

# test for correct time period output for each of them, regular time 
def test_get_time_period_correct():
    assert get_time_period(h1_m, m1_m)==output_m, "'6:01' should be Morning"
    assert get_time_period(h2_a, m2_a)==output_a, "'14:25' should be Afternoon"
    assert get_time_period(h3_e, m3_e)==output_e, "'20:03' should be Evening"
    assert get_time_period(h4_n, m4_n)==output_n, "'23:12' should be Night"
    assert get_time_period(h5_ln, m5_ln)==output_ln, "'02:10' should be Late Night"

# test for correct time period output for each of them, boundary values
def test_get_time_period_boundary_values():
    assert get_time_period(h6_ln, m6_ln) == output_ln, "'6:00' should be Late Night"
    assert get_time_period(h7_m, m7_m) == output_m, "'12:00' should be Morning"
    assert get_time_period(h8_a, m8_a) == output_a, "'18:00' should be Afternoon"
    assert get_time_period(h9_e, m9_e) == output_e, "'21:00' should be Evening"
    assert get_time_period(h10_n, m10_n) == output_n, "'00:00' should be Night"
     
# test for correct error handling for incorrect type of column value     
# (not an integer) 
def test_get_time_period_type_error():
    with pytest.raises(TypeError, match=r"Both hour and minute input should be integer"):
        get_time_period(h1_m, 1.2)

        