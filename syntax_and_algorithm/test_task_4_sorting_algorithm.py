from unittest import TestCase

from syntax_and_algorithm.task_4_sorting_algorithm import bubble_sort


class Test(TestCase):
    def test_bubble_sort(self):
        self.assertListEqual([1], bubble_sort([1]))
        self.assertListEqual([1, 2, 3, 4, 5], bubble_sort([5, 4, 3, 2, 1]))
        self.assertListEqual(["a", "b", "c"], bubble_sort(["c", "b", "a"]))
        self.assertListEqual([1, 2, 3, 4, 5], bubble_sort([1, 2, 3, 4, 5]))
        self.assertListEqual(["x"], bubble_sort(["x"]))

    def test_bubble_sort_repeating_elements(self):
        self.assertListEqual([1, 2, 3, 3, 3, 3, 4, 5], bubble_sort([3, 1, 2, 3, 4, 3, 3, 5]))
        self.assertListEqual(["a", "b", "c", "c"], bubble_sort(["a", "c", "b", "c"]))

    def test_bubble_sort_empty_list(self):
        self.assertListEqual([], bubble_sort([]))
