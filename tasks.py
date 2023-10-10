from celery import app


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