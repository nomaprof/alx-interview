#!/usr/bin/python3
"""
Minimum number of operations needed to reach n number of
pasted items
"""


def minOperations(n):
    """

    :param: n:
    :return: minimum number of operations
    """
    if n <= 1:
        return 0
    for ans in range(2, n+1):
        if n % ans == 0:
            return minOperations(int(n/ans)) + ans
