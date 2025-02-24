from fastapi.testclient import TestClient
from main import app
from unittest.mock import AsyncMock, MagicMock


# Mock the lifespan
app.router.lifespan_context = AsyncMock(return_value=None)
mock_db=MagicMock()
app.state.db=mock_db

client = TestClient(app)

def test_health():
    response = client.get("/health")  
    assert response.status_code == 200
    assert response.json()["status"] =="healthy"

def test_always_true():
    assert 4%2==0
