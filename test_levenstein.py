import levenstein


def test_equals():
    assert levenstein.dist("python", "python") == 0


def test_insert():
    assert levenstein.dist("tree", "three") == 1


def test_two_letters():
    assert levenstein.dist("boat", "board") == 2


def test_different():
    assert levenstein.dist("java", "php") == 4
