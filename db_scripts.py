import os
import psycopg2
def db_connect():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect('postgresql://postgres:12345@localhost:5432/directory')
        return conn
    except:
        # в случае сбоя подключения будет выведено сообщение  в STDOUT
        print('Can`t establish connection to database')


def getCategory() -> dict():
    conn = psycopg2.connect('postgresql://postgres:12345@localhost:5432/directory')
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
    except:
        print("ERROR")
