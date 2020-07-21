from .preparation import DataPreparation
from .training import ModelTraining
from .persistence import ModelPersistence

import logging

class TrainingJob():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        
        self.preparation_step = DataPreparation(config['dataPreparation'])
        self.training_step = ModelTraining(config['trainingDetails'])
        self.persistence_step = ModelPersistence(config['trainingDetails'])

    def execute(self, data):
        self.logger.info("Preparing Data")
        inputs, outputs, labels = self.preparation_step.execute(data)

        self.logger.info("Labels: {}".format(labels))
        
        self.logger.info("Training Model")
        model = self.training_step.execute(inputs, outputs, labels)

        self.logger.info("Saving Model")
        self.persistence_step.save(model)
        
        self.logger.info("Training Complete")