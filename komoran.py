from PyKomoran import Komoran, DEFAULT_MODEL

class Preprocess:
    def __init__(self):
        self.Komoran = Komoran(DEFAULT_MODEL['FULL'])

    def get_keyword(self, sentence):
        keyword_list = self.Komoran.get_list(sentence)
        return keyword_list