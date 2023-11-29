import pytest
from Project_2.custom_date_time import CustomDateTime

# Test creating CustomDateTime with specific arguments
def test_constructor_with_arguments():
    dt = CustomDateTime(2021, 4, 3, 11, 32, 56)
    assert dt.year == 2021
    assert dt.month == 4
    assert dt.day == 3
    assert dt.hour == 11
    assert dt.minute == 32
    assert dt.second == 56

# Test creating CustomDateTime with no arguments (defaults to current date and time)
def test_constructor_defaults():
    dt = CustomDateTime()
    now = CustomDateTime.from_iso_format(CustomDateTime().to_iso_format())
    assert dt.to_iso_format().startswith(now.to_iso_format())


# Test to_iso_format method
def test_iso_format():
    dt = CustomDateTime(2021, 4, 3, 11, 32, 56)
    assert dt.to_iso_format() == "2021-04-03T11:32:56"

# Test to_human_readable_format method
def test_human_readable_format():
    dt = CustomDateTime(2021, 4, 3, 11, 32, 56)
    assert dt.to_human_readable_format() == "2021-04-03 11:32:56"

# Test validate_date class method
def test_validate_date():
    assert CustomDateTime.validate_date(2021, 4, 3) == True
    assert CustomDateTime.validate_date(2023, 2, 30) == False

# Test date_difference class method
def test_date_difference():
    dt1 = CustomDateTime(2023, 4, 3)
    dt2 = CustomDateTime(2019, 5, 10)
    assert abs(CustomDateTime.date_difference(dt1, dt2, unit='days')) == 1424


# Test date_from_string static method
def test_date_from_string():
    dt_str = "2023-10-07 12:45:36"
    dt = CustomDateTime.date_from_string(dt_str)
    assert dt.to_human_readable_format() == "2023-10-07 12:45:36"



if __name__ == "__main__":
    pytest.main()  