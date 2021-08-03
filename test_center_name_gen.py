import pytest
import center_name_gen

def test_initially_empty_dict():
    assert center_name_gen.name_generator({},2) == {"Center 1":0, "Center 2":0}

def test_initially_non_empty_dict():
    assert center_name_gen.name_generator({"Center 1":0},2) == {"Center 1":0, "Center 2":0, "Center 3":0}

