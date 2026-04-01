# tests/conftest.py
import pytest
from rich import inspect

@pytest.fixture
def hello():
    inspect("Hello World!")