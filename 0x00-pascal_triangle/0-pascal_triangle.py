#!/usr/bin/python3
"""Replicate Pascal's triangle with a Python script"""


def pascal_triangle(n):
    """
    produces a list of lists of integers representing the Pascal’s triangle of size n
    """
    

    # return empty list if n <= 0
    if n <= 0:
        return []
    # return Pascal's triangle if n > 0
    triangle = [[1]]
    for k in range(1, n):
        row = [1]
        for j in range(1, k):
            row.append(triangle[k - 1][j - 1] + triangle[k - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
