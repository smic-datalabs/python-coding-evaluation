from unittest import TestCase

from syntax_and_algorithm.task_5_binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        self.assertEqual(2, binary_search([1, 2, 3, 4, 5], 3))
        self.assertEqual(-1, binary_search([1, 2, 3, 4, 5], 6))
        self.assertEqual(0, binary_search([1, 2, 3, 4, 5], 1))
        self.assertEqual(4, binary_search(["a", "b", "c", "d", "e"], "e"))

    def test_binary_search_empty_list(self):
        self.assertEqual(-1, binary_search([], 1))

    def test_binary_search_repeating_elements(self):
        self.assertEqual(3, binary_search([1, 2, 3, 3, 3, 4, 5], 3))
        self.assertEqual(1, binary_search(["a", "b", "c", "c", "d"], "b"))
