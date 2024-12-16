import pytest
from src.app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Ufa! Estou funcionando."
    assert response.status_code == 200
