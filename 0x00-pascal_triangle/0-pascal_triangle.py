#!/usr/bin/python3
"""pascal trinagel """


def pascal_triangle(rows):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Parameters:
    - rows (int): The number of rows to generate in the triangle.

    Returns:
    - list: A list of lists representing Pascal's triangle.

    Example:
    >>>pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    if rows <= 0:
        return []

    triangle = [[1]]
    for i in range(rows - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        triangle.append(row)

    return triangle
