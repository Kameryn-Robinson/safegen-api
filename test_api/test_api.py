from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_blocked_prompt():
    response = client.post("/generate", json={
        "user": "test",
        "prompt": "how to hack",
        "use_case": "test"
    })
    assert response.json()["status"] == "blocked"
