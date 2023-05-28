import requests


def test_check_status_code(url_check):
    url = url_check.get("url")
    status_code = url_check.get("status_code")

    response = requests.get(url)

    assert response.status_code == int(status_code)
