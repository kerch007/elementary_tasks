from unittest import TestCase
from elementary_task_5 import number_to_words

class TestNumber_to_words(TestCase):
    def test_negative_enter_number_to_words(self):
        self.assertFalse(number_to_words(-33))

    def test_positive_enter_number_to_words(self):
        self.assertTrue(number_to_words(3333))

    def test_string_enter_number_to_words(self):
        self.assertFalse(number_to_words('asdasd'))

    def test_equal_number_to_words(self):
        self.assertEqual(number_to_words(1132),'одна тысяча сто тридцать два')

    def test_Not_equal_number_to_words(self):
        self.assertNotEqual(number_to_words(1132),'Две тысяча сто тридцать два')

if __name__ == "__main__":
    TestNumber_to_words()

