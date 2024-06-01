import pytest
from fastapi import HTTPException
from api.service import validate_sentence

def test_validate_sentence_success():
    assert validate_sentence("Hello, how are you?") is None

def test_validate_sentence_empty():
    with pytest.raises(HTTPException) as excinfo:
        validate_sentence("")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "The sentence cannot be empty."

def test_validate_sentence_short():
    with pytest.raises(HTTPException) as excinfo:
        validate_sentence("Hi")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "The sentence is too short."

def test_validate_sentence_long():
    long_sentence = "a" * 501
    with pytest.raises(HTTPException) as excinfo:
        validate_sentence(long_sentence)
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "The sentence is too long."

def test_validate_sentence_invalid_characters():
    with pytest.raises(HTTPException) as excinfo:
        validate_sentence("Hello!@#")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "The sentence contains invalid characters."
