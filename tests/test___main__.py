from unittest import TestCase
import pythonping


class Test_Telegram(TestCase):
    def test_telegram(self):
        result = pythonping.ping("telegram.com", verbose=False).success()
        self.assertEqual(result, True)

