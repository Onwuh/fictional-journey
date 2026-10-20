import pytest
from main import count_by

def test_key_error():
    liste = [{" ": "a"}, {"typ": "b"}, {"typ": "a"}]
    
    with pytest.raises(KeyError):
        count_by(liste, "typ")

def test_empty_input():
    liste = []

    with pytest.raises(ValueError):
        count_by(liste,"typ")

