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
        self.semifinal = []
        # action count_dict 구성
        self.ob_count = Counter(self.ob_result)
        self.ac_count = Counter(self.ac_result)
        #self.em_count = Counter(em_result)

        self.ob2_count = []
        self.ob1_count = []
        self.ac2_count = []
        self.ac1_count = []

        # ob, ac 개수대로 list 완성
        for k, v in self.ob_count.items():
            if v >= 2: self.ob2_count.append(k)
            else: self.ob1_count.append(k)

        for k, v in self.ac_count.items():
            if v >= 2: self.ac2_count.append(k)
            else: self.ac1_count.append(k)

        self.ob2_count_set = set(self.ob2_count)
        self.ob1_count_set = set(self.ob1_count)
        self.ac2_count_set = set(self.ac2_count)
        self.ac1_count_set = set(self.ac1_count)

        #ob가 2개인 경우
        first_priority = self.ob2_count_set & self.ac2_count_set
        for i in first_priority: self.final.append(i)

        second_priority = self.ob2_count_set & self.ac1_count_set
        if len(self.final) + len(second_priority) > 3:
            tmp = random.sample(second_priority, 3 - len(self.final))
            for i in tmp: self.final.append(i)
        else:
            for i in second_priority: self.final.append(i)
            third_priority = self.ob2_count_set - first_priority - second_priority
            if len(self.final) + len(third_priority) > 3:
                tmp = random.sample(third_priority, 3 - len(self.final))
                for i in tmp: self.final.append(i)
            else:
                for i in third_priority: self.final.append(i)
                # ob가 1개인 경우
                fourth_priority = self.ob1_count_set & self.ac2_count_set
                if len(self.final) + len(fourth_priority) > 3:
                    tmp = random.sample(fourth_priority, 3 - len(self.final))
                    for i in tmp: self.final.append(i)
                else:
                    for i in fourth_priority: self.final.append(i)
                    fifth_priority = self.ob1_count_set & self.ac1_count_set
                    if len(self.final) + len(fifth_priority) > 3:
                        tmp = random.sample(fifth_priority, 3 - len(self.final))
                        for i in tmp: self.final.append(i)
                    else:
                        for i in fifth_priority: self.final.append(i)
                        sixth_priority = self.ob1_count_set - fourth_priority - fifth_priority
                        if len(self.final) + len(sixth_priority) > 3:
                            tmp = random.sample(sixth_priority, 3 - len(self.final))
                            for i in tmp: self.final.append(i)
                        else:
                            for i in sixth_priority: self.final.append(i)
                            seventh_priority = self.ac2_count_set - first_priority - fourth_priority
                            if len(self.final) + len(seventh_priority) > 3:
                                tmp = random.sample(seventh_priority, 3 - len(self.final))
                                for i in tmp: self.final.append(i)
                            else:
                                for i in seventh_priority: self.final.append(i)
                                # ob가 없는경우
                                eighth_priority = self.ac1_count_set - second_priority - fifth_priority
                                if len(self.final) + len(eighth_priority) > 3:
                                    tmp = random.sample(eighth_priority, 3 - len(self.final))
                                    for i in tmp: self.final.append(i)
                                else:
                                    for i in eighth_priority: self.final.append(i)
                    
        self.fin()
        return self.final

    def fin(self):
        if '' in self.final:
            self.final.remove('')
            
        for i in self.final:
            print(self.dao.sel_main(i))