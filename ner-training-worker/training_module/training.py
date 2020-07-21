import logging
import pickle
from sklearn_crfsuite import CRF, metrics


class ModelTraining():
    def __init__(self, config):
        self.output_file = config['outputFile']
        self.model_dict = config['modelDict']
        self.logger = logging.getLogger(__name__)

    def execute(self, inputs, outputs, labels):
        self.logger.info("building model")
        model = CRF( **self.model_dict )

        self.logger.info("fitting model")
        model.fit(inputs, outputs)

        self.logger.info("validating model")
        labels.remove('O')
        y_pred = model.predict(inputs)
        
        flat_f1_score = metrics.flat_f1_score(outputs, y_pred, average='weighted', labels=labels)
        self.logger.info('flat f1 score: {}'.format(flat_f1_score))
        
        validation = metrics.flat_classification_report(
            outputs, y_pred, labels=labels, digits=4
        )
        self.logger.info('\n'+validation)

        return model
    