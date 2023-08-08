from unittest import TestCase

from syntax_and_algorithm.task_3_list_manipulation import unique_elements, reverse_list, max_element


class Test(TestCase):
    def test_unique_elements(self):
        self.assertListEqual([1, 2, 3, 4, 5], unique_elements([1, 2, 3, 3, 3, 3, 4, 5]))
        self.assertListEqual(["a", "b", "c"], unique_elements(["a", "b", "c", "c"]))

    def test_reverse_list(self):
        self.assertListEqual([5, 4, 3, 2, 1], reverse_list([1, 2, 3, 4, 5]))
        self.assertListEqual(["c", "b", "a"], reverse_list(["a", "b", "c"]))
        self.assertListEqual([1, 2, 3, 4, 5], reverse_list([5, 4, 3, 2, 1]))

    def test_max_element(self):
        self.assertEqual(5, max_element([1, 2, 3, 4, 5]))
        self.assertEqual("c", max_element(["a", "b", "c"]))
        self.assertEqual(5, max_element([5, 4, 3, 2, 1]))
