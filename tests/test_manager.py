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


def test_tasks_should_accept_post_method(response_post_tasks):
    assert response_post_tasks.status_code != 405


def test_submit_task_should_have_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 422


def test_title_should_have_between_3_and_50_chars(
    client,
    task
):
    task['title'] = 2 * '*'
    response = client.post('/tasks', json=task)
    assert response.status_code == 422
    
    task['title'] = 51 * '*'
    response = client.post('/tasks', json=task)
    assert response.status_code == 422


def test_when_submit_task_should_have_description(client):
    response = client.post('/tasks', json={'title': 'title'})
    assert response.status_code == 422


def test_description_should_have_140_chars_max(
    client,
    task
):
    task['description'] = '*' * 141
    response = client.post('/tasks',json=task)
    assert response.status_code == 422


def test_when_create_task_it_should_be_returned(
    client,
    task
):
    response = client.post('/tasks', json=task)
    assert response.json()['title'] == task['title']
    assert response.json()['description'] == task['description']
    TASKS.clear()


def test_when_create_task_its_id_should_be_unique(
    client,
    task
):
    task_1 = {
        'title': 'title_1',
        'description': 'description_1'
    }
    response = client.post('/tasks', json=task)
    response_1 = client.post('/tasks', json=task_1)
    assert response.json()['id'] != response_1.json()['id']
    TASKS.clear()


def test_when_create_task_status_should_be_in_progress(
    client,
    task
):
    response = client.post('/tasks', json=task)
    assert response.json()['status'] ==  'in progress'
    TASKS.clear()


def test_when_create_task_status_code_should_be_201(
    client,
    task
):
    response = client.post('/tasks', json=task)
    assert response.status_code == 201
    TASKS.clear()


def test_when_create_task_should_be_stored(
    client,
    task
):
    response = client.post('/tasks', json=task)
    assert response.status_code == 201
    assert len(TASKS) == 1
    TASKS.clear()
