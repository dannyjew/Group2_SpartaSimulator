import pytest
import trainee_generation

def test_value():
    assert trainee_generation.trainee_gen() in (range(20,31))