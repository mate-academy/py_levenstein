"""
levenstein - This module provides function
dist() that returns levenstein distance between
two strings
"""


def dist(str_1: str, str_2: str) -> int:
    """
    Return levenstein distance between strings
    str_1 and str_2
    :param str_1: str
    :param str_2: str
    :return: int
    """
    len_1 = len(str_1) + 1
    len_2 = len(str_2) + 1
    arr = [[i + j if not i*j else 0 for i in range(len_1)] for j in range(len_2)]

    for i in range(len_2 - 1):
        for j in range(len_1 - 1):
            if str_1[j] != str_2[i]:
                arr[i+1][j+1] = min(arr[i][j+1], arr[i+1][j], arr[i][j]) + 1
            else:
                arr[i+1][j+1] = arr[i][j]
    return arr[-1][-1]
