from datetime import timedelta

broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/1'
timezone = 'UTC'
accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'

beat_schedule = {
    'execute-every-10-seconds': {
        'task': 'tasks.my_periodic_task',
        'schedule': timedelta(seconds=10),
    },
}