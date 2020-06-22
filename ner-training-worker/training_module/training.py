import logging
from sklearn_crfsuite import CRF, metrics

logger = logging.getLogger(__name__)

def train(inputs, outputs, labels):
    logging.info("building model")
    model = CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.2,
        max_iterations=100,
        all_possible_transitions=True,
        verbose=True
    )
    logging.info("fitting model")
    model.fit(inputs, outputs)

    logging.info("validating mode")
    labels.remove('O')
    y_pred = model.predict(inputs)
    flat_f1_score = metrics.flat_f1_score(outputs, y_pred, average='weighted', labels=labels)
    logger.info('flat f1 score: {}'.format(flat_f1_score))
    validation = metrics.flat_classification_report(
        outputs, y_pred, labels=labels, digits=4
    )
    logger.info(validation)
    # TODO model save
    