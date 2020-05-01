from fastapi import FastAPI
from .models import Task, TaskEntry
from uuid import uuid4


app = FastAPI()

TASKS = []

@app.get('/tasks')
def get_list():
    return TASKS


@app.post('/tasks', response_model=Task, status_code=201)
def post_task(task: TaskEntry):
    new_task = task.dict()
    new_task.update({"id": uuid4()})
    TASKS.append(new_task)
    return new_task