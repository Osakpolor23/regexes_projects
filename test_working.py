import pytest
from working import convert


def test_convert():
    assert convert("9am to 5pm") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("9am to 15:30") == "09:00 to 15:30"

    # Ensure ValueError is raised for invalid inputs
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
        
    with pytest.raises(ValueError):
        convert("9:00 AM   5:00 PM")