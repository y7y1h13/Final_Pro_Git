import pymysql
from sqlalchemy import text, create_engine

class JjalDao:
    def connect(self):
        return pymysql.connect(host='127.0.0.1', user='bigdata',
                              password='dbgusals1',db='chat',charset='utf8')

    def sel_action(self,word):
        conn = self.connect()
        sql = "select idx from action where 단어=%s"
        cursor = conn.cursor()
        cursor.execute(sql,word)
        result = cursor.fetchall()
        conn.close()
        return result
        
    def sel_emotion(self,word):
        conn = self.connect()
        sql = "select idx from emotion where 단어=%s"
        cursor = conn.cursor()
        cursor.execute(sql,word)
        result = cursor.fetchall()
        conn.close()
        return result[0][0]
        
    def sel_object(self,word):
        conn = self.connect()
        sql = "select idx from object where 단어=%s"
        cursor = conn.cursor()
        cursor.execute(sql,word)
        result = cursor.fetchall()
        conn.close()
        return result
        
    def sel_main(self,idx):
        conn = self.connect()
        sql = "select URL from main where IDX=%s"
        cursor = conn.cursor()
        cursor.execute(sql,idx)
        result = cursor.fetchall()
        conn.close()
        return result[0][0]


    
    
