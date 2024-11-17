import pytest
from src.main import ExampleClass

def test_example_class():
    example = ExampleClass(42)
    assert example.get_value() == 42
