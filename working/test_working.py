import pytest
from working import convert

def test_convert_wrong_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")

def test_convert_right_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:15 AM to 5:15 PM") == "09:15 to 17:15"

def test_convert_PM_AM():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"