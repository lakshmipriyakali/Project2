import sys
from os.path import abspath, dirname
import datetime

sys.path.append(abspath(dirname(dirname(__file__))))

from my_datetime.datetime import Datetime

def test_constructor_defaults():
    dt = Datetime()
    current_datetime = datetime.datetime.now()

    assert dt.date_time.year == current_datetime.year
    assert dt.date_time.month == current_datetime.month
    assert dt.date_time.day == current_datetime.day
    assert dt.date_time.hour == current_datetime.hour
    assert dt.date_time.minute == current_datetime.minute
    assert dt.date_time.second == current_datetime.second

    print(f"Actual Year: {dt.date_time.year}")
    print(f"Actual Month: {dt.date_time.month}")
    print(f"Actual Day: {dt.date_time.day}")
    print(f"Actual Hour: {dt.date_time.hour}")
    print(f"Actual Minute: {dt.date_time.minute}")
    print(f"Actual Second: {dt.date_time.second}")

def test_iso_format():
    dt = Datetime(2023, 11, 26, 19, 3, 27)
    iso_format_result = dt.iso_format()
    expected_iso_format = '2023-11-26T19:03:27'
    
    assert iso_format_result == expected_iso_format

    print(f"Actual ISO Format: {iso_format_result}")
    print(f"Expected ISO Format: {expected_iso_format}")