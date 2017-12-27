from day1 import follow_directions


def test_follow_directions1():
    directions = ["R2", "L3"]

    expected = 5
    actual = follow_directions(directions)

    print(actual)
    assert expected == actual


def test_follow_directions2():
    directions = ["R2", "R2", "R2"]

    expected = 2
    actual = follow_directions(directions)

    print(actual)
    assert expected == actual


def test_follow_directions3():
    directions = ["R5", "L5", "R5", "R3"]

    expected = 12
    actual = follow_directions(directions)

    print(actual)
    assert expected == actual
