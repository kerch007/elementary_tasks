from unittest import TestCase
from elementary_task_1 import Chess_desk

class TestChess_desk(TestCase):


    def test_negative_enter_Chess_desk(self):
        self.assertTrue(Chess_desk(-3,8))

    def test_positive_enter_Chess_desk(self):
        self.assertTrue(Chess_desk(6,6))

    def test_string_enter_Chess_desk(self):
        self.assertTrue(Chess_desk('asdasd',6))

    def test_Not_equal_Chess_desk(self):
        self.assertNotEqual(Chess_desk(4,1),'* * ')



if __name__ == "__main__":
    TestChess_desk()