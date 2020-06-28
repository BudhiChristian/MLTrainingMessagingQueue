# NER CRF Training Worker

**NOTE - This application won't run unless a messaging queue is running and identified (see run options below)**

This application is meant to run as a worker node that listens to the messaging queue, crf_training_queue, and executes a training job when it is free. It is also meant to demonstrate a modular approach to building workers. 

In the main file, app.py, a messenger is created and it is fed a callback which will execute the complete training script. training_module can be replaced with any module that contains a main.py that has the class TrainingJob which has an execute() method that will execute training.

``` python
# messenger instance is created
messenger = Messenger(config['messagingConfiguration'])
# training job is instantiated
training_job = TrainingJob(config['trainingConfiguration'])

# training job is linked to messenger via a callback
messenger.start(callback=training_job.execute)
```

## Training Data file 

Training Data file used for this application is a csv file modeled after the data from https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus?select=ner_dataset.csv 

## Build and Run on Docker
```
docker build -t docker-image-name .

docker run -itd --rm --name crf-training \
    --env RABBITMQ_HOST=<rabbitmq-host-location> \
    --mount src=/absolute/path/to/host/mount,target=/external_mount,type=bind \
    docker-image-name
```

`--env RABBITMQ_HOST=<rabbitmq-host-location>`

Replace \<rabbitmq-host-location\> with RabbitMQ host location/ip

`--mount src=/absolute/path/to/host/mount,target=/external_mount,type=bind`

Replace src value with local directory you wish to link to the docker container.

Alternatively you may set up a docker volume and use its name for source, but make sure to change the type value to volume

`--mount src=your-docker-volume,target=/external_mount,type=volume`

## Run Locally
Create a virtual environment with Python 3.7 and install packages using the provided requirements.txt file

`pip install -r requirements.txt`

Edit config.yml to set trainingConfiguration.trainingDetails.outputFile to the absolute path you wish to write the model file to. Also if you are not running an instance of RabbitMQ locally, update messagingConfiguration.host to reflect the host you're using.

run app.py from ner-training-worker directory

`python app.py`