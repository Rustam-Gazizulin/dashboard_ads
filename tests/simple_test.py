def test_a():
    assert True


def test_root_not_found(client):
    response = client.get('/')
    assert response.status_code == 200

