NER CRF Training Job can build built and run on docker after RabbitMQ is running. Replace \<rabbitmq-host-location\> with RabbitMQ host. 

``` bash
docker build -t cjbudhi/training-queue/crf-training .
docker run -itd --rm --name crf-training --env RABBITMQ_HOST=<rabbitmq-host-location> cjbudhi/training-queue/crf-training
```