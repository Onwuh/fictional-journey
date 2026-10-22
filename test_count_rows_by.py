import pytest
from main import count_rows_by

def test_normal_output():
    data = [{"name":"john","area": "New York City, Downtown", "desc":"long brown hair, short, 80 kg"},
            {"name":"Jason","area": "New York City, Uptown", "desc":"short brown hair, short, 120 kg"},
            {"name":"Jared","area": "New York City, Downtown, Downtown", "desc":"long blue hair, big, 70 kg"},
            {"name":"Johanna","area": "New York City, Bronx", "desc":"short purple hair, tall, 60 kg"}
            ]
    assert count_rows_by(data,"area","Downtown") == 2

def test_missing_key():
    data = [{"name":"john","area": "New York City, Downtown", "desc":"long brown hair, short, 80 kg"},
                {"name":"Jason","area": "New York City, Uptown", "desc":"short brown hair, short, 120 kg"},
                {"name":"Jared","area": "New York City, Downtown", "desc":"long blue hair, big, 70 kg"},
                {"name":"Johanna","area": "New York City, Bronx", "desc":"short purple hair, tall, 60 kg"}
                ]
    with pytest.raises(ValueError):
        count_rows_by(data,"area","   ")

def test_lower_higher():
    data = [{"name":"john","area": "New York City, Downtown", "desc":"long brown hair, short, 80 kg"},
                {"name":"Jason","area": "New York City, Uptown", "desc":"short brown hair, short, 120 kg"},
                {"name":"Jared","area": "New York City, downtown", "desc":"long blue hair, big, 70 kg"},
                {"name":"Johanna","area": "New York City, Bronx", "desc":"short purple hair, tall, 60 kg"}
                ]
    assert count_rows_by(data,"area","Downtown") == 2

def test_key_is_part_of_word():
    data = [{"name":"john","area": "New York City, Downtown", "desc":"long brown hair, short, 80 kg"},
                {"name":"Jason","area": "New York City, Uptown", "desc":"short brown hair, short, 120 kg"},
                {"name":"Jared","area": "New York City, Downtown", "desc":"long blue hair, big, 70 kg"},
                {"name":"Johanna","area": "New York City, Bronx", "desc":"short purple hair, tall, 60 kg"}
                ]
    assert count_rows_by(data,"area","Down") == 2

def test_key_is_none():
    data = [{"name":"john","area": "New York City, Downtown", "desc":"long brown hair, short, 80 kg"},
                    {"name":"Jason","area": "New York City, Uptown", "desc":"short brown hair, short, 120 kg"},
                    {"name":"Jared","area": "New York City, Downtown", "desc":"long blue hair, big, 70 kg"},
                    {"name":"Johanna","area": "New York City, Bronx", "desc":"short purple hair, tall, 60 kg"}
                    ]
    with pytest.raises(ValueError):
        count_rows_by(data,"area",None)  # type: ignore