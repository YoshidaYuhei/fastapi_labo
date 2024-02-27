from fastapi.testclient import TestClient

def test_read_main(client: TestClient):
    response = client.get("/system/healthcheck")
    assert response.status_code == 200
