"""Write a function to calculate the Levenstein distance"""


def dist(string_one: str, string_two: str) -> int:
    """Return the Levenshtein edit distance between two strings"""
    if not string_one:
        return len(string_two)
    if not string_two:
        return len(string_one)
    if string_one[0] == string_two[0]:
        return dist(string_one[1:], string_two[1:])
    first = dist(string_one, string_two[1:])
    second = dist(string_one[1:], string_two)
    third = dist(string_one[1:], string_two[1:])
    return min(first, second, third) + 1
