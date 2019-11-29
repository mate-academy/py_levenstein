"""PY algoritm Levenshtein Distance"""

def dist(strng1: str, strng2: str) -> int:
    """
    Levenshtein Distance function
    :param strng1: first string
    :param strng2: second string
    :return: Levenshtein Distance
    """
    strng1_len, strng2_len = len(strng1), len(strng2)
    if strng1_len < strng2_len:
        strng1, strng2 = strng2, strng1
        strng1_len, strng2_len = strng2_len, strng1_len
    result = 0
    for i in range(strng2_len):
        if strng1[i] == strng2[i]:
            continue
        if strng1[i+1] == strng2[i]:
            strng1 = strng1[:i] + strng1[i+1:]
            result += 1
        elif strng1[i+1] != strng2[i]:
            result += 1
    result += len(strng1) - strng2_len
    return result
