"""
docstring
"""
import levenstein


def test_equals():
    """

    :return:
    """
    assert levenstein.dist("python", "python") == 0


def test_insert():
    """

    :return:
    """
    assert levenstein.dist("tree", "three") == 1


def test_two_letters():
    """

    :return:
    """
    assert levenstein.dist("boat", "board") == 2


def test_different():
    """

    :return:
    """
    assert levenstein.dist("java", "php") == 4
