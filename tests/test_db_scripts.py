from unittest import TestCase

from db_scripts import db_connect, getCategory


class Test_db_connection(TestCase):
    def test_db_connect(self):
        result = db_connect()
        self.assertIsNotNone(result)


class Test_getCategory(TestCase):
    def test_get_category(self):
        result = getCategory()
        self.assertIsNotNone()
