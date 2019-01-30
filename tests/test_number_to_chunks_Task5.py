from unittest import TestCase
from elementary_task_5 import number_to_chunks

class TestNumber_to_chunks(TestCase):

    def test_number_to_chunks(self):
        for x in number_to_chunks(123456):
            if x % 2 == 0:
                self.assertTrue(True, "Found value %d" % x)
                return
        self.assertTrue(False, "No even found in Anything")

    def test_negative_number_to_chunks(self):
        for x in number_to_chunks(-356):
            if x % 2 == 0:
                self.assertFalse(True, "Found value %d" % x)
                return
        self.assertFalse(False, "No even found in Anything")

if __name__ == '__main__':

    TestNumber_to_chunks()

