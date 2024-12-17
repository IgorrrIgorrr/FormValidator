import requests

BASE_URL = "http://127.0.0.1:8000"


def test_existing_model():
    data = {"user_email": "example@test.com", "order_date": "2023-12-15"}
    response = requests.post(f"{BASE_URL}/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"name": "Order Form"}


def test_nonexistent_template():
    data = {"random_field": "test value", "some_date": "15.12.2023"}
    response = requests.post(f"{BASE_URL}/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"random_field": "text", "some_date": "date"}


if __name__ == "__main__":
    test_existing_model()
    test_nonexistent_template()
    print("All tests passed.")
