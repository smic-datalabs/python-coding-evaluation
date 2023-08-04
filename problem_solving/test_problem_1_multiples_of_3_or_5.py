from unittest import TestCase

from problem_solving.problem_1_multiples_of_3_or_5 import sum_of_multiples_of_3_or_5


class Test(TestCase):
    def test_sum_of_multiples_of_3_or_5(self):
        self.assertEqual(23, sum_of_multiples_of_3_or_5(10))
        self.assertEqual(78, sum_of_multiples_of_3_or_5(20))
        self.assertEqual(9168, sum_of_multiples_of_3_or_5(200))
        self.assertEqual(233168, sum_of_multiples_of_3_or_5(1000))
        self.assertEqual(16687353, sum_of_multiples_of_3_or_5(8456))

