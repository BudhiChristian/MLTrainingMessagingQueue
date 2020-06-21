import nltk 

nltk.download('averaged_perceptron_tagger')

class Featurizer():
    def __init__(self):
        # set up 
        pass
    def featurize(self, sentence):
        parts_of_speech = nltk.pos_tag(sentence)
        featured_data = list()
        for word, pos in zip(sentence, parts_of_speech):
            featured_data.append({
                "word": word,
                "pos": pos[1]
            })
        return featured_data