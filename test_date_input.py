import pytest
import datetime
import date_input

def test_for_datetime_object():
    assert date_input.date(8) isinstance(datetime)
def test_date_for_4_months():
    assert date_input.date(4) == datetime.date(2021,12,3)
