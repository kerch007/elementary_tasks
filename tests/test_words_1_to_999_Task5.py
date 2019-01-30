from unittest import TestCase
from elementary_task_5 import words_1_to_999

class TestWords_1_to_999(TestCase):
    def test_negative_enter_words_1_to_999(self):
        self.assertFalse(words_1_to_999(-3))

    def test_positive_enter_words_1_to_999(self):
        self.assertTrue(words_1_to_999(3))

    def test_string_enter_words_1_to_999(self):
        self.assertFalse(words_1_to_999('asdasd'))

    def test_Equal_words_1_to_999(self):
        self.assertEqual(words_1_to_999(132),'сто тридцать два')

    def test_Not_Equal_words_1_to_999(self):
        self.assertNotEqual(words_1_to_999(1132),'сто тридцать два')

if __name__ == "__main__":

    TestWords_1_to_999()


