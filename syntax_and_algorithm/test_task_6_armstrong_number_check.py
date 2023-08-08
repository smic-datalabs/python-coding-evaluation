from unittest import TestCase

from syntax_and_algorithm.task_6_armstrong_number_check import is_armstrong_number


class Test(TestCase):
    def test_is_armstrong_number(self):
        self.assertTrue(is_armstrong_number(153))
        self.assertTrue(is_armstrong_number(370))

    def test_is_not_armstrong_number(self):
        self.assertFalse(is_armstrong_number(154))
        self.assertFalse(is_armstrong_number(372))

    def test_is_not_armstrong_number_negative(self):
        self.assertFalse(is_armstrong_number(-154))
        self.assertFalse(is_armstrong_number(-371))

    def test_is_not_armstrong_number_zero(self):
        self.assertTrue(is_armstrong_number(0))

