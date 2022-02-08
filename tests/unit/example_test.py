import unittest

from src.example import Example


class TestExample(unittest.TestCase):
    def test_value(self):
        self.assertEqual(Example(), 7)