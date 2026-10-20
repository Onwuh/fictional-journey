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

# key error bei leerem dict. Weil der input immer vollständig sein soll und ein leeres dict auf einen fehler in der basis hinweist
def test_empty_dict():
    with pytest.raises(KeyError):
        count_by([{}, {"typ": "b"}, {"typ": "a"}],"typ")

def test_different_key():
    with pytest.raises(KeyError):
            count_by([{"blah": "a"}, {"typ": "b"}, {"typ": "a"}],"typ")