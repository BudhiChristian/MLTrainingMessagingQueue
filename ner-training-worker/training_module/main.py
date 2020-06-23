from .preparation import prepare_training_data
from .training import train

import logging

class TrainingJob():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)

    def execute(self, data):
        self.logger.info("Preparing Data")
        inputs, outputs, labels = prepare_training_data(data)

        self.logger.info("Labels: {}".format(labels))
        
        self.logger.info("Training Model")
        train(inputs, outputs, labels)
        
        self.logger.info("Training Complete")