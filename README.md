# ML Training Messaging Queue

This project is meant to demonstrate a modular approach to scheduling training jobs to mulitple workers using a simple messaging queue with RabbitMQ

Before running any of the applications in this project you must run a messaging queue; otherwise they will not find a messaging host to listen to and fail to run. This can be done easily with docker by running the below command.

```
docker run -itd --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

## Planned Architecture

![task Manager](https://christian-budhi-hosting.s3.amazonaws.com/training-manager/trainging_manager_architecture.jpg)

## Task Manager

The Task Manager is a simple Express server that will post messages to specific queues to schedule a training job for the workers to execute. Currently an endpoint, crf-ner/train, exists which accepts a [csv file](https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus?select=ner_dataset.csv) to be processed and used for training an NER model.

This idea can be further expanded with a scheduler that pulls data from your database of choice and posts to the training queue periodically to keep an up to date model.

## NER Training Worker

This application is meant to run as a worker node that listens to the messaging queue, crf_training_queue, and executes a training job when it is free. It is also meant to demonstrate a modular approach to building workers. 