from fastapi import FastAPI


app = FastAPI()

TASKS = []

@app.get('/tasks')
def get_list():
    return TASKS
