"""
docstring
"""
import numpy as np


def dist(str1: str, str2: str) -> int:
    """
    git init
    git add
    git commit
    git push

    :param str1:
    :param str2:
    :return:
    """
    size_str1 = len(str1) + 1
    size_str2 = len(str2) + 1
    matrix = np.zeros((size_str1, size_str2))
    for char in range(size_str1):
        matrix[char, 0] = char
    for char_ in range(size_str2):
        matrix[0, char_] = char_

    for char in range(1, size_str1):
        for char_ in range(1, size_str2):
            if str1[char - 1] == str2[char_ - 1]:
                matrix[char, char_] = min(
                    matrix[char - 1, char_] + 1,
                    matrix[char - 1, char_ - 1],
                    matrix[char, char_ - 1] + 1
                )
            else:
                matrix[char, char_] = min(
                    matrix[char - 1, char_] + 1,
                    matrix[char - 1, char_ - 1] + 1,
                    matrix[char, char_ - 1] + 1
                )
    return matrix[size_str1 - 1, size_str2 - 1]
