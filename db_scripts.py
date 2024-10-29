import os
import psycopg2

from config import DB_CONN

# 'postgresql://postgres:12345@localhost:5432/directory'
def db_connect():
    try:
        # пытаемся подключиться к базе данных
        if DB_CONN is None:
            conn = psycopg2.connect(os.environ['DB_CONN_V'])
        else:
            conn = psycopg2.connect(DB_CONN)
        return conn
    except:
        # в случае сбоя подключения будет выведено сообщение  в STDOUT
        print('Can`t establish connection to database')


def getCategory() -> dict():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("Select * from category")
    cats = cursor.fetchall()
    cursor.close()
    conn.close()
    return cats

def getQuestion(id, isApp):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f"Select id, type, quest, answer from questions where category = "+id+f" and isapp = {isApp}")
    quest = cursor.fetchall()
    cursor.close()
    conn.close()
    return quest

def getQuestionForApp(isApp):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f"Select id, category, quest, answer from questions where isapp = {isApp}")
    quest = cursor.fetchall()
    cursor.close()
    conn.close()
    return quest

def getAnswer(id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("Select answer, type from questions where id = " + id)
    ans = cursor.fetchall()
    cursor.close()
    conn.close()
    return ans[0]

def addAnswer(categoryId, type, quest, ans):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        text = f"INSERT INTO public.questions\
            (category, type, quest, answer, isapp)\
            VALUES({categoryId}, {type}, '{quest}', '{ans}', false);"
        cursor.execute(text)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        print("ERROR")

def appQuest(id):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        text = f"Update public.questions\
             set isapp = true where id = {id};"
        cursor.execute(text)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("ERROR")
