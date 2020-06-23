Training Task Manager can build built and run on docker after RabbitMQ is running. Replace \<rabbitmq-host-location\> with RabbitMQ host. 

```
docker build -t cjbudhi/training-queue/task-manager .
docker run -itd --rm --name task-manager -p 3000:3000 --env RABBITMQ_HOST=<rabbitmq-host-location> cjbudhi/training-queue/task-manager
```