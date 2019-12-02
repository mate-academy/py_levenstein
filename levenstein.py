"""Levenstein distance"""

def dist(first_string: str, second_string: str) -> int:
    """
    Func calculates Levenstein distance
    :param first_string: first string
    :param second_string: second string
    :return: Levenstein distance
    """
    distance = 0
    if len(first_string) != len(second_string):
        longest_string = max(first_string, second_string, key=len)
        smallest_string = min(first_string, second_string, key=len)
    else:
        longest_string, smallest_string = first_string, second_string
    for i in longest_string:
        if i not in smallest_string:
            distance += 1
    return distance
