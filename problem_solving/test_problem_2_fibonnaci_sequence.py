from unittest import TestCase

from problem_solving.problem_2_fibonnaci_sequence import sum_of_even_fibonacci_terms, get_fibonacci_sequence


class Test(TestCase):
    def test_sum_of_even_fibonacci_terms(self):
        self.assertEqual(44, sum_of_even_fibonacci_terms(100))
        self.assertEqual(798, sum_of_even_fibonacci_terms(1000))
        self.assertEqual(3382, sum_of_even_fibonacci_terms(10000))
        self.assertEqual(60696, sum_of_even_fibonacci_terms(100000))
        self.assertEqual(1089154, sum_of_even_fibonacci_terms(1000000))
        self.assertEqual(4613732, sum_of_even_fibonacci_terms(4000000))

    def test_get_fibonacci_sequence(self):
        self.assertListEqual([1, 2, 3, 5, 8, 13, 21, 34, 55, 89], get_fibonacci_sequence(100))
        self.assertListEqual([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], get_fibonacci_sequence(200))
        self.assertEqual(15, len(get_fibonacci_sequence(1000)))
        self.assertEqual(987, get_fibonacci_sequence(1000)[-1])


