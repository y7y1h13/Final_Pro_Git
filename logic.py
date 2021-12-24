from DAO import *
from komoran import *
from collections import defaultdict, Counter
import random

class Rank:   
    
    # 형태소 분석
    def komoran(self,word):
        komo = Preprocess()
#         pairs = komo.get_keyword('최민수 허세부리다')
        pairs = komo.get_keyword(word)
        return pairs
        
        
        #가져와서 나누기
    def split(self, pairs):
        ob_result = ''
        ac_result = ''
        em_result = ''
        

        for i in pairs:
            if (i.get_second() == 'NNP') or (i.get_second() == 'NNG'):
                ob_result += JjalDao().sel_object(i.get_first())

            elif i.get_second() == 'VV':
                ac_result += JjalDao().sel_action(i.get_first())

            elif i.get_second() == 'VA':
                em_result += JjalDao().sel_emotion(i.get_first())
        ob_result = ob_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        ac_result = ac_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')
        em_result = em_result.replace('][',',').replace('[','').replace(']','').replace(' ','').split(',')

        return ob_result,ac_result,em_result


    def ob_counter(self,ob_result):
        if ob_result[0] != '':
            counter = Counter(ob_result)
            ob = counter.most_common()
        return ob
        
    def ac_counter(self,ac_result):
        if ac_result[0] != '':
            counter = Counter(ac_result)
            other = counter.most_common()
        return other
            
            
    def em_counter(self,em_result):
        if em_result[0] != '':
            counter = Counter(em_result)
            other = counter.most_common()   
        return other



    def st1(self, ob):
        first, second = [], []
        for k,v in ob:
            if v !=1:
                first.append(k)
            else :
                second.append(k)
        return first, second
         
        
    def st2(self, other, first, second):         
        for k,v in other:
            if k not in first:
                second.append(k)
        return second
              
                
    def st3(self,first, second):
        test1, test2 = [], []
        if len(first) == 1:
            counter = Counter(second)
            test = counter.most_common()
            for k,v in test:
                if v != 1:
                    test1.append(k)
                else:
                    test2.append(k)

            # 여기서 또 나눠야함....;;

            if len(test1) == 1:
                pass

            elif len(test1) == 2:
                pass

            elif len(test1) > 2:
                pass


            #일단은 결과 보는게 중요하기 때문에 나중에 하고 대충 해보겠음


            #random으로 숫자 뽑기
        #     a = random.sample(range(0,len(test2)),2)
        #     first.append(a)
            while len(first) < 3:
                a = str(random.randint(1,(len(test2)+1)))
                if a not in first:
                    first.append(a)




        elif len(first) == 2:
            pass

        elif len(first) == 3:
            pass

        elif len(first) > 3:
            pass           
        
        return first
    def result(self,first):
        for i in first:
            print(JjalDao().sel_main(i))