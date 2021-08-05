import unittest.mock as mock
import pytest
import sys
import month_input
from center_name_gen import name_generator
import datetime
import date_input
from num_full_centers import num_full
from opening_new_centre import monthly_centre
from stu_assignment import student_assignment
from trainee_generation import trainee_gen


# Tests month_input functions
@pytest.fixture
def fake_input():
    with mock.patch('month_input.my_input') as m:
        yield m


def test_valid_month_input(fake_input):
    fake_input.return_value = 3
    assert month_input.time_frame() == 3


def test_invalid_month_input(fake_input):
    fake_input.return_value = "randomstring"
    with pytest.raises(ValueError):
        month_input.time_frame()


# Tests center_name_gen functions
def test_initially_empty_dict():
    assert name_generator({},2) == {"Center 1":0, "Center 2":0}


def test_initially_non_empty_dict():
    assert name_generator({"Center 1":0},2) == {"Center 1":0, "Center 2":0, "Center 3":0}


# Tests date_input functions
def test_date_for_4_months():
    assert date_input.date(4) == datetime.date(2021,12,4)


# Tests num_full_centers functions
def test_three_full_centres():
    assert num_full({"Center 1": 100, "Center 2": 100, "Center 3": 75, "Center 4": 100, "Center 5": 0}) == 3


# Tests opening_new_centre functions
def test_opening_one_new_centre():
    assert monthly_centre({"Center 1":0}) == {"Center 1":0, "Center 2":0}


# Tests stu_assignment functions
def test_student_assignment_for_zero_waiting():
    assert student_assignment({"Center 1": 50,"Center 2": 85,"Center 3": 75}, 0, 0) == ({"Center 1": 50,"Center 2": 85, "Center 3": 75}, 0)


def test_student_assignment_for_intake_and_waiting():
    test_centre_list, test_waiting = student_assignment({"Center 1": 50, "Center 2": 80, "Center 3": 75}, 50, 20)
    assert test_centre_list["Center 1"] in range(50,71)
    assert test_centre_list["Center 2"] in range(80, 101)
    assert test_centre_list["Center 3"] in range(75, 96)
    assert test_waiting in range(10, 71)


# Tests trainee_generation functions
def test_value():
    assert trainee_gen() in (range(20,31))

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))