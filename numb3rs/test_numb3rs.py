from numb3rs import validate
import pytest

def test_validate_standard():
    assert validate("1.2.3.4") == True

def test_validate_uppercorner():
    assert validate("255.1.2.3") == True

def test_validate_lowercorner():
    assert validate("0.0.0.0") == True

def test_validate_outofrange():
    assert validate("265.123.23.1") == False

def test_validate_first_byte():
    assert validate("45.432.345.346") == False
