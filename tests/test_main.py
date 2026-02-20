from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/api/docs")
    assert response.status_code == 200

def test_static_fallback():
    # Since static folder is empty in test environment, it might return 404 or the error message
    # In my code: if not os.path.exists("app/static/index.html"): return {"message": ...}
    response = client.get("/some-random-path")
    assert response.status_code == 200
    assert "Frontend not built yet" in response.json()["message"]
