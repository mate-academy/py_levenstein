"""This program counts Levenstein difference being
number of edits to be made to change one word into another

"Якщо в слові "хліб" зробити 4 помилки, можна отримати слово "пиво""
"""

def dist(string1: str, string2: str) -> int:
    """Check symbol-by-symbol the given strings and
    add extra points if strings' lengths differ"""

    horizontals = len(string1) + 1
    verticals = len(string2) + 1
    lev_dist = [[0 for x in range(verticals)] for x in range(horizontals)]
    for index in range(1, horizontals):
        lev_dist[index][0] = index
    for index in range(1, verticals):
        lev_dist[0][index] = index

    for col in range(1, verticals):
        for row in range(1, horizontals):
            if string1[row - 1] == string2[col - 1]:
                cost = 0
            else:
                cost = 1
            lev_dist[row][col] = min(lev_dist[row - 1][col] + 1,
                                     lev_dist[row][col - 1] + 1,
                                     lev_dist[row - 1][col - 1] + cost)

    return lev_dist[row][col]
