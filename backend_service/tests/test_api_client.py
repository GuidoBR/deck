from app.services.api_client import APIClient

def test_fetch_data():
    api_client = APIClient()
    data = api_client.fetch_data()
    
    assert "id" in data
    assert "name" in data
    assert "value" in data
