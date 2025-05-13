import pytest
from backend.app import app

# Set up a fixture to create a test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route using the fixture
def test_home(client):
    response = client.get("/")
    assert response.data == b"Welcome Ehsan"
    assert response.status_code == 200
