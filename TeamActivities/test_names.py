"""
Team 1B Activity # 5

test_names.py
"""
from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])