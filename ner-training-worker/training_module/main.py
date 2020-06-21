from .preparation import prepare_training_data
from .training import train

import logging

logger = logging.getLogger(__name__)

def train_data(data):
    logger.info("Preparing Data")
    inputs, outputs, labels = prepare_training_data(data)
    logger.info("Labels: {}".format(labels))
    print(inputs[0])
    print(outputs[0])
    logger.info("Training Model")
    train(inputs, outputs, labels)
    logger.info("Training Complete")