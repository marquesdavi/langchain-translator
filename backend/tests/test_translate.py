import pytest
from fastapi.testclient import TestClient
from api.settings import app

client = TestClient(app)

def test_translate_success():
    response = client.post("/translate", json={"sentence": "Hello"})
    assert response.status_code == 200
    assert "output" in response.json()
    assert isinstance(response.json()["output"], str)

def test_translate_empty_sentence():
    response = client.post("/translate", json={"sentence": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "The sentence cannot be empty."}

def test_translate_short_sentence():
    response = client.post("/translate", json={"sentence": "Hi"})
    assert response.status_code == 400
    assert response.json() == {"detail": "The sentence is too short."}

def test_translate_long_sentence():
    long_sentence = "a" * 501
    response = client.post("/translate", json={"sentence": long_sentence})
    assert response.status_code == 400
    assert response.json() == {"detail": "The sentence is too long."}

def test_translate_invalid_characters():
    response = client.post("/translate", json={"sentence": "Hello!@#"})
    assert response.status_code == 400
    assert response.json() == {"detail": "The sentence contains invalid characters."}
