def test_index(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
