import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url', action='store', help='url for status check'
    )
    parser.addoption(
        '--status_code', action='store', help='status code for url check'
    )


@pytest.fixture
def url_check(request):
    url = request.config.getoption('--url')
    status_code = request.config.getoption('--status_code')
    return {"url": url, "status_code": status_code}

