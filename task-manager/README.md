Training Task Manager can be built and run on docker.

```
docker build -t cjbudhi/training-queue/task-manager
docker run -itd --rm --name task-manager -p 3000:3000 --env RABBITMQ_HOST=<rabbitmq-host-location> cjbudhi/training-queue/task-manager
```