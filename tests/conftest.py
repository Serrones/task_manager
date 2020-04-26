import pytest
from starlette.testclient import TestClient
from task_manager.manager import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client

@pytest.fixture
def response_get_tasks(client):
    response = client.get('/tasks')
    return response
