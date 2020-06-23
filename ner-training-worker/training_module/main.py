from .preparation import DataPreparation
from .training import ModelTraining

import logging

class TrainingJob():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        
        self.preparation_step = DataPreparation(config['dataPreparation'])
        self.training_step = ModelTraining(config['trainingDetails'])

    def execute(self, data):
        self.logger.info("Preparing Data")
        inputs, outputs, labels = self.preparation_step.execute(data)

        self.logger.info("Labels: {}".format(labels))
        
        self.logger.info("Training Model")
        self.training_step.execute(inputs, outputs, labels)
        
        self.logger.info("Training Complete")