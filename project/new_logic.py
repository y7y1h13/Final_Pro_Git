from DAO import *
from komoran import *
from collections import defaultdict, Counter
import random

class Logic:
    def __init__(self):
        self.komo = Preprocess()
        self.dao = JjalDao()
        
    # 형태소 분석
    def komoran(self):
        self.pairs = []
        self.word = input('문장 입력: ')
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

            elif i.get_second() == 'VV':
                self.word_ac = self.dao.sel_action(i.get_first())
                if self.word_ac != ():
                    self.ac_result += self.word_ac[0][0]         

#             elif word_ob == () and word_ac == () and pos == 'VA':#감성분석
#                 self.em_result = self.dao.sel_emaction_onlyion(i.get_first())


        self.ob_result = self.ob_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        self.ac_result = self.ac_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        
        
    # 빈도수 
    def freq(self):
        counter1 = Counter(self.ob_result)
        self.ob = counter1.most_common()
        counter2 = Counter(self.ac_result)
        self.action_onlyher = counter2.most_common()
        #     self.counter = Counter(em_result)
        #     self.action_onlyher = counter.most_common()
        
    # 우선순위    
    def rank(self):
        self.ob_only = [] # 개체 1순위
        self.ob_only_second = [] 
        self.action_only = [] # 개체 해당 하지 않는 나머지 액션 값
        self.ob_ac_first = [] # 개체+액션 1순위
        self.ob_ac_second = [] # 개체+액션 2순위
        
        #개체만 분류
        for k,v in self.ob:
            if v != 1:
                self.ob_only.append(k)
            else :
                self.ob_only_second.append(k)
                
                
        #액션 추가
        # 개체에 해당하는 액션은 따로 분리해야함 해당하지 않는건 다른 리스트에 추가
        for k,v in self.action_onlyher:
            if (k in self.ob_only) and (k in self.ob_only_second):
                self.ob_only_second.append(k)
            else:
                self.action_only.append(k)
        
        
        counter = Counter(self.ob_only_second)
        tmp = counter.most_common()
        #1이면 1순위에 넣고 1이 아니면 2순위에 넣는다
        for k,v in tmp:
            if v != 1:
                self.ob_ac_first.append(k)
            else:
                self.ob_ac_second.append(k)
                
                
                
                
    def result(self):
        self.final = []
        ob_only_len = len(self.ob_only)
        ob_ac_first_len = len(self.ob_ac_first)
        ob_ac_second_len = len(self.ob_ac_second)
        if ob_only_len == 1:
            self.save_final(self.ob_only)

            if ob_ac_first_len == 0:

                if ob_ac_second_len == 0:
                    self.action_only_3()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)
                    self.action_only_2()

                elif ob_ac_second_len == 2:
                    self.save_final(self.ob_ac_second)

                elif ob_ac_second_len >= 3:
                    self.rand(self.ob_ac_second)

            elif ob_ac_first_len == 1:
                self.save_final(self.ob_ac_first)

                if ob_ac_second_len == 0:
                    self.action_only_2()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)

                elif ob_ac_second_len >= 2:
                    self.rand(self.ob_ac_second)

            elif ob_ac_first_len == 2:
                self.save_final(self.ob_ac_first)

            elif ob_ac_first_len >= 3:
                self.rand(self.ob_ac_first)


        elif ob_only_len == 2:
            self.save_final(self.ob_only)

            if ob_ac_first_len == 0:

                if ob_ac_second_len == 0:
                    self.action_only_2()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)

                elif ob_ac_second_len >= 2:
                    self.rand(self.ob_ac_second)

        elif ob_only_len == 3:
            self.save_final(self.ob_only)

        elif ob_only_len >= 4:
            self.rand(self.ob_only)

        elif ob_only_len == 0:

            if ob_ac_first_len == 0:

                if ob_ac_second_len == 0:
                    self.action_only_4()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)
                    self.action_only_3()

                elif ob_ac_second_len == 2:
                    self.save_final(self.ob_ac_second)
                    self.action_only_2()

                elif ob_ac_second_len == 3:
                    self.save_final(self.action_only)

                elif ob_ac_second_len >= 4:
                    self.rand(self.ob_ac_second)

            elif ob_ac_first_len == 1:
                self.save_final(self.ob_ac_first)

                if ob_ac_second_len == 0:
                    self.action_only_3()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)
                    self.action_only_2()

                elif ob_ac_second_len == 2:
                    self.save_final(self.ob_ac_second)

                elif ob_ac_second_len >= 3:
                    self.rand(self.ob_ac_second)            


            elif ob_ac_first_len == 2:
                self.save_final(self.ob_ac_first)

                if ob_ac_second_len == 0:
                    self.action_only_2()

                elif ob_ac_second_len == 1:
                    self.save_final(self.ob_ac_second)
                elif ob_ac_second_len >= 2:
                    self.rand(self.ob_ac_second)          

            elif ob_ac_first_len == 3:
                self.save_final(self.ob_ac_first)

            elif ob_ac_first_len >= 4:
                self.rand(self.ob_ac_first)
        self.fin()
        
                
    def save_final(self,var):
        self.var = var
        self.final += self.var
        
    def rand(self, var):
        self.var = var
        while len(self.final)<3:
            a = random.randint(0,(len(self.var)-1))
            if self.var[a] in self.final:
                self.final.append(self.var[a])
    
    def action_only_4(self):
        if len(self.action_only) < 4:
            self.save_final(self.action_only)
                
        elif len(self.action_only) >= 4:
            self.rand(self.action_only)   
            
    def action_only_3(self):
        if len(self.action_only) < 3:
            self.save_final(self.action_only)
                
        elif len(self.action_only) >= 3:
            self.rand(self.action_only)
            
    def action_only_2(self):
        if len(self.action_only) < 2:
            self.save_final(self.action_only)

        elif len(self.action_only) >= 2:
            self.rand(self.action_only)
            
    def fin(self):
        if '' in self.final:
            self.final.remove('')
            
        for i in self.final:
            print(self.dao.sel_main(i))