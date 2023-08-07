"""
Write a Python program to check whether a number is Armstrong number or not.
Note: An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.

Algorithm:
1. Get the number to check for armstrong number
2. Count the number of digits in the number
3. Add the nth power of each digit in the number
4. If the sum is equal to the number, it is an armstrong number

Example 1:
    153 -> True

    How it is computed:
    length or number of digits is 3
    153 == (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3)
    153 == 1 + 125 + 27
    153 == 153

Example 2:
    1634 -> True

    How it is computed:
    length of number of digits is 4
    1634 == (1 * 1 * 1 * 1) + (6 * 6 * 6 * 6) + (3 * 3 * 3 * 3) + (4 * 4 * 4 * 4)
    1634 == 1 + 1296 + 81 + 256
    1634 == 1634

Example 3:
    98 -> False

    how it is computed:
    length of number of digits is 2
    98 == (9 * 9) + (8 * 8)
    98 == 81 + 64
    98 == 145  # which is False
"""


def is_armstrong_number(value):
    pass