from PyKomoran import Komoran, DEFAULT_MODEL

class Preprocess:
    def __init__(self, userdict = 'dic.user'):
        # 형태소 분석기 초기화
        self.Komoran = Komoran(DEFAULT_MODEL['FULL'])
        # 사용자 사전 추가
        self.Komoran.set_user_dic(userdict)

    def get_keyword(self, sentence):
        keyword_list = self.Komoran.get_list(sentence + ' *')
        return keyword_list