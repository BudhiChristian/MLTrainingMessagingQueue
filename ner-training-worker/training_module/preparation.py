import csv
from io import StringIO
import logging

from .featurizer import Featurizer
featurizer = Featurizer()
logger = logging.getLogger(__name__)

def prepare_training_data(data):
    logger.info("buidling list of list generator")
    data_generator = read_csv(data)

    logger.info("building parsed data generator")
    sentence_generator = parse_sentences(data_generator)

    logger.info("featurizing data and pulling labels")
    inputs = list()
    outputs = list()
    labels = set()
    for sentence, tags in sentence_generator:
        inputs.append(featurizer.featurize(sentence))
        outputs.append(tags)
        labels.update(tags)
    return inputs, outputs, sorted(labels)


def read_csv(data):
    f = StringIO(data)
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        yield row

def parse_sentences(data):
    sentence = None
    skip_header = True
    for entry in data:
        if skip_header:
            skip_header = False
            continue
        if entry[0]:
            if sentence:
                yield (sentence['words'], sentence['tags'])
            sentence = {
                'words': list(),
                'tags': list()
            }
        sentence['words'].append(entry[1])
        sentence['tags'].append(entry[3])
    if sentence:
        yield (sentence['words'], sentence['tags'])