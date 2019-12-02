"""
Levenstein distance
"""


def dist(word1, word2):
    """Calculates the Levenshtein distance between word1 and word2"""
    len_word1, len_word2 = len(word1), len(word2)
    if len_word1 > len_word2:
        word1, word2 = word2, word1
        len_word1, len_word2 = len_word2, len_word1

    current_row = range(len_word1 + 1)
    for i in range(1, len_word2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_word1
        for j in range(1, len_word1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if word1[j - 1] != word2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[len_word1]
