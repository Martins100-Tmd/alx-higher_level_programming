#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Creates the pascal triangle sequence

    Args:
        n (number): number of rows
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    all = []
    for i in range(1, n + 1):
        row = []
        for j in range(0, i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                row.append(all[i - 2][j - 1] + all[i - 2][j])
        all.append(row)
    return all
