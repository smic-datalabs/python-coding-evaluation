import time
from unittest import TestCase

import timeout_decorator

from problem_solving.problem_3_palindromes import is_palindrome, get_largest_palindrome_product


class Test(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(9009))
        self.assertFalse(is_palindrome(9899))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Was it a cat I saw"))
        self.assertFalse(is_palindrome("Was it a cat I saw?"))

    def test_get_largest_palindrome_product(self):
        self.assertEqual(9009, get_largest_palindrome_product(2))
        self.assertEqual(906609, get_largest_palindrome_product(3))

    def test_get_largest_palindrome_product_of_4_and_5(self):
        self.assertEqual(99000099, get_largest_palindrome_product(4))
        # start_time = time.time()
        self.assertEqual(9966006699, get_largest_palindrome_product(5))
        # print("Time taken: ", time.time() - start_time)

    @timeout_decorator.timeout(1, exception_message="Time limit exceeded")
    def test_get_largest_palindrome_product_of_6_and_7(self):
        # start_time = time.time()
        self.assertEqual(999000000999, get_largest_palindrome_product(6))
        # print("Time taken: ", time.time() - start_time)
        start_time = time.time()
        self.assertEqual(99956644665999, get_largest_palindrome_product(7))
        # print("Time taken: ", time.time() - start_time)

