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
        
        for i in self.pairs:
            if (i.get_second() == 'NNP') or (i.get_second() == 'NNG'):
                self.ob_result += self.dao.sel_object(i.get_first())

            elif i.get_second() == 'VV':
                self.ac_result += self.dao.sel_action(i.get_first())         

        #     elif (ob_result == '') and (ac_result == ''):#감성분석
        #         em_result = dao.sel_emotion(i.get_first())


        self.ob_result = self.ob_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        self.ac_result = self.ac_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        
    # 빈도수 
    def freq(self):
        counter1 = Counter(self.ob_result)
        self.ob = counter1.most_common()
        counter2 = Counter(self.ac_result)
        self.other = counter2.most_common()
        #     self.counter = Counter(em_result)
        #     self.other = counter.most_common()
        
    # 우선순위    
    def rank(self):
        self.ob1 = [] # 개체 1순위
        self.ob3 = [] 
        self.ot = [] # 개체 해당 하지 않는 나머지 액션 값
        self.ob2 = [] # 개체+액션 1순위
        self.ob4 = [] # 개체+액션 2순위
        
        #개체만 분류
        for k,v in self.ob:
            if v != 1:
                self.ob1.append(k)
            else :
                self.ob3.append(k)
                
                
        #액션 추가
        # 개체에 해당하는 액션은 따로 분리해야함 해당하지 않는건 다른 리스트에 추가
        for k,v in self.other:
            if (k not in self.ob1) and (k in self.ob3):
                self.ob3.append(k)
            else:
                self.ot.append(k)
        
        
        counter = Counter(self.ob3)
        tmp = counter.most_common()
        #1이면 1순위에 넣고 1이 아니면 2순위에 넣는다
        for k,v in tmp:
            if v != 1:
                self.ob2.append(k)
            else:
                self.ob4.append(k)
                
                
                
                
    def result(self):
        self.final = []
        a = len(self.ob1)
        b = len(self.ob2)
        c = len(self.ob4)
        # save_final(ob1)
        if a == 1:
            self.save_final(self.ob1)

            if b == 0:

                if c == 0:
                    self.ot_3()

                elif c == 1:
                    self.save_final(self.ob4)
                    self.ot_2()

                elif c == 2:
                    self.save_final(self.ob4)

                elif c >= 3:
                    self.rand(self.ob4)

            elif b == 1:
                self.save_final(self.ob2)

                if c == 0:
                    self.ot_2()

                elif c == 1:
                    self.save_final(self.ob4)

                elif c >= 2:
                    self.rand(self.ob4)

            elif b == 2:
                self.save_final(self.ob2)

            elif b >= 3:
                self.rand(self.ob2)


        elif a == 2:
            self.save_final(self.ob1)

            if b == 0:

                if c == 0:
                    self.ot_2()

                elif c == 1:
                    self.save_final(self.ob4)

                elif c >= 2:
                    self.rand(self.ob4)

        elif a == 3:
            self.save_final(self.ob1)

        elif a >= 4:
            self.rand(self.ob1)

        elif a == 0:

            if b == 0:

                if c == 0:
                    self.ot_4()

                elif c == 1:
                    self.save_final(self.ob4)
                    self.ot_3()

                elif c == 2:
                    self.save_final(self.ob4)
                    self.ot_2()

                elif c == 3:
                    self.save_final(self.ot)

                elif c >= 4:
                    self.rand(self.ob4)

            elif b == 1:
                self.save_final(self.ob2)

                if c == 0:
                    self.ot_3()

                elif c == 1:
                    self.save_final(self.ob4)
                    self.ot_2()

                elif c == 2:
                    self.save_final(self.ob4)

                elif c >= 3:
                    self.rand(self.ob4)            


            elif b == 2:
                self.save_final(self.ob2)

                if c == 0:
                    self.ot_2()

                elif c == 1:
                    self.save_final(self.ob4)
                elif c >= 2:
                    self.rand(self.ob4)          

            elif b == 3:
                self.save_final(self.ob2)

            elif b >= 4:
                self.rand(self.ob2)
        self.fin()
        
                
    def save_final(self,var):
        self.final += self.var
        
    def rand(self, var):
        self.var = var
        while len(self.final)<3:
            a = random.randint(0,(len(self.var)-1))
            if self.var[a] not in self.final:
                self.final.append(self.var[a])
    
    def ot_4(self):
        if len(self.ot) < 4:
            self.save_final(self.ot)
                
        elif len(self.ot) >= 4:
            self.rand(self.ot)   
            
    def ot_3(self):
        if len(self.ot) < 3:
            self.save_final(self.ot)
                
        elif len(self.ot) >= 3:
            self.rand(self.ot)
            
    def ot_2(self):
        if len(self.ot) < 2:
            self.save_final(self.ot)

        elif len(self.ot) >= 2:
            self.rand(self.ot)
            
    def fin(self):
        for i in self.final:
            print(self.dao.sel_main(i))