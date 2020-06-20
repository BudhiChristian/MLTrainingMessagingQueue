from .preparation import prepare_training_data
from .training import train

import logging

logger = logging.getLogger(__name__)

def train_data(data):
    logger.info("Preparing Data")
    training_data = prepare_training_data(data)
    logger.info("Training Model")
    train(train_data)
    logger.info("Training Complete")