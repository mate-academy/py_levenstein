"""Levenstein distance"""
import numpy


def dist(first_string: str, second_string: str) -> int:
    """
    Func calculates Levenstein distance
    :param first_string: first string
    :param second_string: second string
    :return: Levenstein distance
    """
    rows = len(first_string) + 1
    cols = len(second_string) + 1
    distance = numpy.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for j in range(1, cols):
            distance[i][0] = i
            distance[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            if first_string[row-1] == second_string[col-1]:
                cost = 0
            else:
                cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,
                                     distance[row][col-1] + 1,
                                     distance[row-1][col-1] + cost)
    return distance[row][col]
