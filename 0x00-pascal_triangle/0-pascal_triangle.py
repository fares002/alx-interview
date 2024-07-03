#!/usr/bin/python3
from math import factorial


def pascal(rows):
    """
    function thats print pascal tringle with ncr law
    """
    triangle = []
    for n in range(rows):
        row = []
        for r in range(n+1):
            ncr = factorial(n) // (factorial(r) * factorial(n-r))
            row.append(ncr)
        triangle.append(row)
    return triangle
