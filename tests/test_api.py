from fastapi.testclient import TestClient

from ooc.api.main import app

client = TestClient(app)


def test_get_self_initial_state():
    """
    Проверка начального состояния TheSelf через API.
    """
    response = client.get("/self")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "TheSelf"
    assert data["ego_stage"] == "MERGED"
    assert data["ego_stability"] == 1.0
    assert isinstance(data["active_states"], list)
    assert isinstance(data["active_defenses"], list)


def test_send_support_event():
    """
    Проверка отправки события поддержки через API.
    """
    payload = {"name": "Поддержка", "impact": 0.3, "type_": "support"}
    response = client.post("/event", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "current_stage" in data
    assert "current_stability" in data
    assert data["current_stability"] > 1.0


def test_send_trauma_event():
    """
    Проверка отправки травматического события через API.
    """
    payload = {"name": "Травма", "impact": -1.0, "type_": "trauma"}
    response = client.post("/event", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["current_stage"] == "DISRUPTION"
