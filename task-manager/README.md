# Task Manager

**NOTE - This application won't run unless a messaging queue is running and identified (see run options below)**

The Task Manager is a simple Express server that will post messages to specific queues to schedule a training job for the workers to execute. Currently an endpoint, crf-ner/train, exists which accepts a [csv file](https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus?select=ner_dataset.csv) to be processed and used for training an NER model.

## Build and Run on Docker

```
docker build -t cjbudhi/training-queue/task-manager .

docker run -itd --rm --name task-manager \
    -p 3000:3000 \
    --env RABBITMQ_HOST=<rabbitmq-host-location> \
    cjbudhi/training-queue/task-manager
```

`-p 3000:3000`

Exposes port 3000 in the docker container to the host machine's port 3000

`--env RABBITMQ_HOST=<rabbitmq-host-location>`

Replace \<rabbitmq-host-location\> with RabbitMQ host location/ip

## Run Locally

1. Install node modules with `npm install`

2. Review environment.js file and edit fields to reflect your environment

3. Run application with `npm start`