import os
from unittest import TestCase, mock

from db_scripts import db_connect, getCategory, getQuestion, getAnswer, addAnswer, getQuestionForApp, appQuest


class Test_db_connection(TestCase):
    @mock.patch.dict(os.environ, {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_db_connect(self):
        result = db_connect()
        self.assertIsNotNone(result)

class Test_getCategory(TestCase):
    @mock.patch.dict(os.environ, {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_get_questions(self):
        result = getQuestion('1', True)
        self.assertIsNotNone(result)

class Test_getAnswer(TestCase):
    @mock.patch.dict(os.environ,
                     {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_get_answer(self):
        result = getAnswer('1')
        self.assertIsNotNone(result)


class Test_CreateAnswer(TestCase):
    @mock.patch.dict(os.environ,
                     {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_create_answer(self):
        category = 1
        question = "Test"
        answer = "Test"
        type = 2
        self.assertIsNotNone(addAnswer(category, type, question, answer))

class Test_GetAppAnswer(TestCase):
    @mock.patch.dict(os.environ,
                     {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_get_app_answer(self):
        ans = getQuestionForApp(False)
        self.assertIsNotNone(ans)

class Test_AppAnswer(TestCase):
    @mock.patch.dict(os.environ,
                     {'DB_CONN_V': 'postgresql://postgres:postgres_password@db.dev-moio.online:31153/dictionary'})
    def test_app_answer(self):
        self.assertIsNotNone(appQuest(0))
