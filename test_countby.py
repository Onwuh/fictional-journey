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

def test_normal_input():
    assert count_by([{"typ": "a"}, {"typ": "b"}, {"typ": "a"}],"typ") == {'a': 2, 'b': 1}

def test_diff_case():
    liste = [{"typ": "A"}, {"typ": "b"}, {"typ": "a"}]
    assert count_by(liste,"typ") == {"A":1,"b":1,"a":1}

