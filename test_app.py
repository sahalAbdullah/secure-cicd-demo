from app import app


def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_page():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Sahal Abdullah" in r.data
