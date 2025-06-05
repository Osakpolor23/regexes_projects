import pytest
from numb3rs import validate

# define a function to test for the valid size of each octet in an IPv4 address
def test_validate_ip_size():
    assert validate("2.5.6.0") == True
    assert validate("256.5.6.0") == False
    assert validate("2.5.6.256") == False
    assert validate("2.5.6.0") == True
    assert validate("255.255.255.0") == True
    assert validate("255.255.255.256") == False
    assert validate("0.1.5.3") == True
    assert validate("0.1.5.300") == False

# define a function to test for the valid format of an IPv4 address
def test_validate_ip_format():
    assert validate("2.255.156") == False
    assert validate("4.158.188_4") == False
    assert validate("cat") == False
    assert validate("my ip is 158.4.3.225") == False
    assert validate("#.#.#.#") == False