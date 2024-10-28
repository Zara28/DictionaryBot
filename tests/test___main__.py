from unittest import TestCase

from __main__ import main


class Test_start_bot(TestCase):
    def test_main(self):
        self.failUnless(main)
