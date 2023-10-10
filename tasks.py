from celery import Celery
import time

app = Celery('tasks')
app.config_from_object('celery_config')


@app.task
def my_periodic_task():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Task executed at {current_time}")


@app.task
def add_t(x, y):
    print("Adding")
    return x + y


@app.task
def mul_t(x, y):
    return x * y


@app.task
def xsum_t(numbers):
    return sum(numbers)
