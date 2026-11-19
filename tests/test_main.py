from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["project"] == "CloudHeal"

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_demo_failure():
    client.post("/demo/recover")
    client.post("/demo/fail")
    assert client.get("/health").status_code == 503
    client.post("/demo/recover")
