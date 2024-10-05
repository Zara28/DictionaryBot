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

# def init_sqlite():
#     if os.path.isfile('database.db'):
#         conn = sqlite_connect()
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS muteusers (id integer primary key, user_id integer, user_name text, date_end datetime, cause text)''')
#         c.execute('''CREATE TABLE IF NOT EXISTS banusers (  id integer primary key, user_id integer, user_name text, date_ban datetime, status bool, count int, cause text)''')
#         conn.commit()
#         conn.close()
#     return

def getCategory() -> dict():
    conn = psycopg2.connect('postgresql://postgres:12345@localhost:5432/directory')
    cursor = conn.cursor()
    cursor.execute("Select * from category")
    cats = cursor.fetchall()
    cursor.close()
    conn.close()
    return cats

def getQuestion(id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("Select id, quest from questions where category = "+id)
    quest = cursor.fetchall()
    cursor.close()
    conn.close()
    return quest

def getAnswer(id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("Select answer from questions where id = " + id)
    ans = cursor.fetchall()
    cursor.close()
    conn.close()
    return ans[0][0]