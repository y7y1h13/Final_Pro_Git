from DAO import *
from komoran import *
from collections import defaultdict, Counter
import random

class Logic:
    def __init__(self):
        self.komo = Preprocess()
        self.dao = JjalDao()

    # 형태소 분석
    def komoran(self, word):
        self.pairs = []
#         self.word = input('문장 입력: ')
        self.word = word
        self.pairs = self.komo.get_keyword(self.word)
     
    # 가져와서 분리 후 리스트로
    def dao_split(self):
        self.ob_result = ''
        self.ac_result = ''
        self.em_result = ''
        self.word_ob = ()
        self.word_ac = ()
        for i in self.pairs:
            pos = i.get_second()
            if pos == 'NNP' or pos == 'NNG':
                self.word_ob = self.dao.sel_object(i.get_first())
                if self.word_ob != ():
                    self.ob_result += self.word_ob[0][0]

            elif i.get_second() in ['VV', 'VX', 'VA', 'XR', 'MAG']:
                self.word_ac = self.dao.sel_action(i.get_first())
                if self.word_ac != ():
                    self.ac_result += self.word_ac[0][0]         

#             elif word_ob == () and word_ac == () and pos == 'VA':#감성분석
#                 self.em_result = self.dao.sel_emaction_onlyion(i.get_first())


        self.ob_result = self.ob_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        if '' in self.ob_result: self.ob_result = self.ob_result.remove('')
        self.ac_result = self.ac_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        if '' in self.ac_result: self.ac_result = self.ac_result.remove('')


    # object, action dictionary count up
    def result(self):

        self.final = []
        self.ob_tmp = []
        self.new_dict = {}
        # action count_dict 구성
        self.ob_count = Counter(self.ob_result)
        self.ac_count = Counter(self.ac_result)
        #em_count = Counter(em_result)
        self.dict_max = None

        # object 2개 이상인 것은 final list에 추가, 2개 미만인 것은 비교를 위해 ob_tmp list에 추가
        for k, v in self.ob_count.items():
            if v >= 2:
                self.final.append(k)
            else: self.ob_tmp.append(k)

        for i in self.ob_tmp:
            # ob가 1인 것들로, value를 action count로 가지는 새로운 딕셔너리 구성
            self.new_dict[i] = self.ac_count[i]

        self.dict_max = [k for k, v in self.new_dict.items() if max(self.new_dict.values()) == v]
        # 만약 dict_max가 하나밖에 없으면?
        # 만약 action값이 존재하지 않고, ob값이 2개 이상인게 없으면?

        # final list가 ob로 채워졌을 때 3개 이상이라면 그대로, 아니라면 1인 것들 비교
        if len(self.final) >= 3:
            self.final = random.sample(self.final, 3)
        elif len(self.final) == 2:
            if len(self.dict_max) >= 1:
                self.final.append(random.sample(self.dict_max, 1)[0])
            else: # action 값이 없을때, ob가 1인 것으로 출력
                self.final.append(random.sample(self.ob_tmp, 1)[0])
        else: # len(self.final) == 1
            if len(self.dict_max) >= 2: # ob가 1이고 ac이 존재하는 값이 2개 이상일 경우
                max_tmp = random.sample(self.dict_max, 2)
                self.final.append(max_tmp[0])
                self.final.append(max_tmp[1])
            elif len(self.dict_max) == 1: # ob가 1이고 ac이 존재하는 값이 1개일 경우
                self.final.append(self.dict_max[0]) # 하나 더 추가해야함
                self.ob_tmp.remove(self.dict_max[0]) # 중복 추가되지 않게 ac값에서 사용된 값 제거
                self.final.append(random.sample(self.ob_tmp, 1)[0]) #ob 1인 것 하나 랜덤 추가
            else: #ob가 2인 값이 1개 뿐인데 ac가 없는 경우
                ob_tmp_random = random.sample(self.ob_tmp, 2)
                self.final.append(ob_tmp_random[0])
                self.final.append(ob_tmp_random[1])
        self.fin()
        return self.final

    def fin(self):
        if '' in self.final:
            self.final.remove('')
            
        for i in self.final:
            print(self.dao.sel_main(i))