# tests/unit/test_prototype.py
import pytest
from rich import inspect
from llama_index.core import SimpleDirectoryReader

def test_run():
    inspect(SimpleDirectoryReader())