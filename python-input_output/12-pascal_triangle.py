#!/usr/bin/python3
"Task 12"


def pascal_triangle(n):
    """Representation of Pascal's triangle

    Args:
        n (integer): Number of rows

    Returns:
        List: with the values of the Pascal's triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        iterated = pascal[-1]
        appender = [1]
        for i in range(len(iterated) - 1):
            appender.append(iterated[i] + iterated[i + 1])
        appender.append(1)
        pascal.append(appender)
    return pascal