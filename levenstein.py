"""PY algoritm Levenshtein Distance"""

def dist(strng1: str, strng2: str) -> int:
    """
    Levenshtein Distance function
    :param strng1: first string
    :param strng2: second string
    :return: Levenshtein Distance
    """
    strng1_len, strng2_len = len(strng1), len(strng2)
    if strng1_len > strng2_len:
        strng1, strng2 = strng2, strng1
        strng1_len, strng2_len = strng2_len, strng1_len
    current_row = []
    for number in range(strng1_len + 1):
        current_row.append(number)
    for i in range(1, strng2_len + 1):
        previous_row, current_row = current_row, [i] + [0] * strng1_len
        for j in range(1, strng1_len + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if strng1[j - 1] != strng2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[strng1_len]
