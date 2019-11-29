"""module for creating matrix"""
import numpy


def dist(strf: str, strs: str) -> int:
    """calculate Levenstein distance"""
    rows = len(strf) + 1
    cols = len(strs) + 1
    matrix = numpy.zeros((cols, rows))
    matrix[0, :] = numpy.arange(rows)
    matrix[:, 0] = numpy.arange(cols)

    for i in range(1, cols):
        for j in range(1, rows):
            if strs[i-1] == strf[j-1]:
                matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1])
            else:
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1,
                                   matrix[i - 1][j - 1] + 1)

    return matrix[-1][-1]
