import pytest
from type_test import add

def test_add():
    assert add(2, 3) == 5
    assert add("Hello, ", "World!") == "Hello, World!"
