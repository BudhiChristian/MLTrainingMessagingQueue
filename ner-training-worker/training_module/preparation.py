import csv
from io import StringIO
import logging

from .featurizer import Featurizer

class DataPreparation():
    def __init__(self, config):
        self.featurizer = Featurizer()
        self.logger = logging.getLogger(__name__)

        self.sentence_index = config['sentenceIndex']
        self.word_index = config['wordIndex']
        self.tag_index = config['tagIndex']

    def execute(self, data):
        self.logger.info("buidling list of list generator")
        data_generator = self.__read_csv(data)

        self.logger.info("building parsed data generator")
        sentence_generator = self.__parse_sentences(data_generator)

        self.logger.info("featurizing data and pulling labels")
        inputs = list()
        outputs = list()
        labels = set()
        for sentence, tags in sentence_generator:
            inputs.append(self.featurizer.featurize(sentence))
            outputs.append(tags)
            labels.update(tags)
        return inputs, outputs, sorted(labels)


    def __read_csv(self, data):
        f = StringIO(data)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield row

    def __parse_sentences(self, data):
        sentence = None
        skip_header = True
        for entry in data:
            if skip_header:
                skip_header = False
                continue
            if entry[self.sentence_index]:
                if sentence:
                    yield (sentence['words'], sentence['tags'])
                sentence = {
                    'words': list(),
                    'tags': list()
                }
            sentence['words'].append(entry[self.word_index])
            sentence['tags'].append(entry[self.tag_index])
        if sentence:
            yield (sentence['words'], sentence['tags'])