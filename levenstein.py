"""
module Levenstein algorithm
"""


def dist(seq1: str, seq2: str) -> int:
    """
    Recursive implementation of Levenstein distance.
    :param seq1: str
    :param seq2: str
    :return: int
    """
    if seq1 == "":
        return len(seq2)
    if seq2 == "":
        return len(seq1)
    if seq1[-1] == seq2[-1]:
        cost = 0
    else:
        cost = 1

    res = min([dist(seq1[:-1], seq2) + 1,
               dist(seq1, seq2[:-1]) + 1,
               dist(seq1[:-1], seq2[:-1]) + cost])
    return res
