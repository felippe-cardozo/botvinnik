from unittest import TestCase
from botvinnik import Botvinnik
import os


class TestBotvinnikClass(TestCase):
    def setUp(self):
        self.bot = Botvinnik

    def test_it_initializes_with_valid_token(self):
        valid_token = os.environ.get('TELEGRAM')
        b = self.bot(token=valid_token)
        self.assertTrue(b)
