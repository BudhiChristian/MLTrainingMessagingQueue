import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

class Featurizer():
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        
    def featurize(self, sentence):
        parts_of_speech = nltk.pos_tag(sentence)
        featured_data = list()
        for idx, (word, pos) in enumerate(parts_of_speech):
            features = self.__featurize_word(word, pos)
            features.update({
                'lower': word.lower(),
                'lemma': self.__lemmatize(word, pos),
                'prefix': word[:3],
                'suffix': word[-4:],
                'pos_simple': pos[:2],
                'BOS': idx == 0,
                'EOS': idx == len(sentence)-1
            })
            features.update(self.__featurize_word(*(parts_of_speech[idx-2] if idx > 1 else ('','')), prefix='-2:'))
            features.update(self.__featurize_word(*(parts_of_speech[idx-1] if idx > 0 else ('','')), prefix='-1:'))
            features.update(self.__featurize_word(*(parts_of_speech[idx+1] if idx < len(sentence)-1 else ('','')), prefix='+1:'))
            features.update(self.__featurize_word(*(parts_of_speech[idx-2] if idx < len(sentence)-2 else ('','')), prefix='+2:'))

            featured_data.append(features)
        return featured_data

    def __featurize_word(self, word, pos, prefix='') -> dict:
        return {
            '{}word'.format(prefix): word,
            '{}pos'.format(prefix): pos
        }

    def __lemmatize(self, word, pos: str):
        wn_pos = ''
        if pos.startswith('J'):
            wn_pos = wordnet.ADJ
        elif pos.startswith('V'):
            wn_pos = wordnet.VERB
        elif pos.startswith('N'):
            wn_pos = wordnet.NOUN
        elif pos.startswith('R'):
            wn_pos = wordnet.ADV
        else:
            wn_pos = wordnet.NOUN
        return self.lemmatizer.lemmatize(word, pos=wn_pos)