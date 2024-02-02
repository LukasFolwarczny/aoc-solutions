from lib import Vec2D


def test_equality():
    a = Vec2D(1, 2)
    b = Vec2D(1, 2)
    c = Vec2D(1, 3)
    d = Vec2D(2, 2)

    assert a == b
    assert a != c
    assert a != d


def test_addition():
    a = Vec2D(1, 3)
    b = Vec2D(2, -4)
    c = (1, 2)

    assert a + b == Vec2D(3, -1)
    assert a + c == Vec2D(2, 5)
    assert c + a == Vec2D(2, 5)


def test_subtraction():
    a = Vec2D(1, 3)
    b = Vec2D(2, -4)
    c = (1, 2)

    assert a - b == Vec2D(-1, 7)
    assert a - c == Vec2D(0, 1)
    assert c - a == Vec2D(0, -1)


def test_indices():
    a = Vec2D(1, 2)
    a[0] = 2
    a[1] = 3

    assert a == Vec2D(2, 3)
    assert a[0] == 2
    assert a[1] == 3
