import pytest
from starlette.testclient import TestClient

from asgi import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
