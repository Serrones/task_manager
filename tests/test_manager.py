from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK

from task_manager.manager import app, TASKS

def test_when_list_tasks_should_return_status_200(response_get_tasks):
    assert response_get_tasks.status_code == HTTP_200_OK

def test_when_list_tasks_should_return_json_format(response_get_tasks):
    assert response_get_tasks.headers['Content-Type'] == 'application/json'

def test_when_list_tasks_should_return_list(response_get_tasks):
    assert isinstance(response_get_tasks.json(), list)

def test_when_list_tasks_returned_task_should_have_id():
    TASKS.append({'id': 1})
    client = TestClient(app)
    response = client.get('/tasks')
    assert 'id' in response.json().pop()
    TASKS.clear()

def test_when_list_tasks_returned_task_should_have_title():
    TASKS.append({'title': 'title 1'})
    client = TestClient(app)
    response = client.get('/tasks')
    assert 'title' in response.json().pop()
    TASKS.clear()


def test_when_list_tasks_returned_task_should_have_description():
    TASKS.append({'description': 'description 1'})
    client = TestClient(app)
    response = client.get('/tasks')
    assert 'description' in response.json().pop()
    TASKS.clear()


def test_when_list_tasks_returned_task_should_have_status():
    TASKS.append({'status': 'done'})
    client = TestClient(app)
    response = client.get('/tasks')
    assert 'status' in response.json().pop()
    TASKS.clear()