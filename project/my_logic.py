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
            self.final.append(k) if v is v>= 2 else self.ob_tmp.append(k)

        for i in self.ob_tmp:
            # ob가 1인 것들로, value를 action count로 가지는 새로운 딕셔너리 구성
            self.new_dict[i] = self.ac_count[i]
            

        self.dict_max = [k for k, v in self.new_dict.items() if max(self.new_dict.values()) == v]


        
        if len(self.final) >= 3:
            self.final += random.sample(self.final, 3)
            
        if len(self.final) == 2:
            if len(self.ob_tmp) >=1:
                self.final += random.sample(self.ob_tmp, 1)
            
            if len(self.ob_tmp) == 0:
                if len(self.ac_count) < 2:
                    self.final += list(self.ac_count)
                    
                if len(self.ac_count) >=2:
                    self.final += random.sample(list(self.ac_count),1)
            
        if len(self.final) == 1:
            if len(self.ob_tmp) >= 2:
                self.final += random.sample(self.ob_tmp,2)
            
            if len(self.ob_tmp) == 1:
                self.final += self.ob_tmp
                if len(self.ac_count) >= 2:
                    self.final += random.sample(list(self.ac_count),1)
                    
                if len(self.ac_count) < 1:
                    self.final += list(self.ac_count)
                    
                
            if len(self.ob_tmp) == 0:
                if len(self.ac_count) >= 2:
                    self.final += random.sample(list(self.ac_count),2)
                
                if len(self.ac_count) < 2:
                    self.final += list(self.ac_count)
                    
            
        if len(self.final) == 0:
            if len(self.ob_tmp) >= 3:
                self.final += random.sample(self.ob_tmp,3)
            
            if len(self.ob_tmp) == 2:
                self.final += self.ob_tmp
                if len(self.ac_count) >=1:
                    self.final += random.sample(list(self.ac_count),1)
                        
            if len(self.ob_tmp) == 1:
                self.final += self.ob_tmp
                if len(self.ac_count) >=2:
                    self.final += random.sample(list(self.ac_count),2)
                    
                if len(self.ac_count) <1:
                    self.final += list(self.ac_count)
                    
            if len(self.ob_tmp) == 0:
                if len(self.ac_count) >=3:
                    self.final += random.sample(list(self.ac_count),3)
                    
                if len(self.ac_count) <= 2:
                    self.final += list(self.ac_count)

                    
        self.fin()
        return self.final
    
    
    
    
    def fin(self):
        if '' in self.final:
            self.final.remove('')
            
        for i in self.final:
            print(self.dao.sel_main(i))