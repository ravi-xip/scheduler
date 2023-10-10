A sample application that shows how to setup Celery in Python.

To run, use the following commands:

```bash
docker-compose up --build
```

Then, in a separate terminal, run the following command:

```bash
curl localhost:8080/
curl localhost:8080/add/1/2
curl localhost:8080/add/async/1/2
curl localhost:8080/add/parallel/1/2/10
```

You should see a task being executed in the logs.