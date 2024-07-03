#!/usr/bin/python3
"""pascal trinagel """

def factorial(n):
    """This function to find factorial of any number """
    if n < 0:
        return "factorial cannot be define for the negative number"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


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
