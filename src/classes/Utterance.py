

class Utterance:

    def __init__(self, raw_utterance):
        self.raw_uttrance = raw_utterance
        self.bag_of_words = toBagOfWord(raw_utterance)


