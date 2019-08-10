from celery import Celery

result_backend = 'db+sqlite:///results.db'

app = Celery('tasks',backend=result_backend, broker='pyamqp://guest@localhost')

@app.task
def add(x,y):
    return x+y
