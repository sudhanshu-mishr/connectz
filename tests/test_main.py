from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_read_root():
    response = client.get("/api/docs")
    assert response.status_code == 200

def test_static_fallback():
    response = client.get("/some-random-path")
    assert response.status_code == 200
    if os.path.exists("app/static/index.html"):
        assert "text/html" in response.headers["content-type"]
        assert "<html" in response.text
    else:
        assert "Frontend not built yet" in response.json()["message"]
