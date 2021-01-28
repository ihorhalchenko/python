import pytest

from vector.vector import Vector


@pytest.mark.parametrize('x, y', [
    (0.0, 0.0),
    (1.1, 2.2)
])
def test_vector_constructor(x, y):
    vector = Vector(x, y)
    assert vector.x == x
    assert vector.y == y


def test_vector_setters():
    vector = Vector()

    vector.x = 42.0
    vector.y = 42.0

    assert vector.x == 42.0
    assert vector.y == 42.0


@pytest.mark.parametrize('value, exception_type', [
    ('error', ValueError),
    (dir, TypeError)
])
def test_vector_setters_exception(value, exception_type):
    vector = Vector()

    with pytest.raises(exception_type):
        vector.x = value

    with pytest.raises(exception_type):
        vector.y = value


def test_vector_to_string():
    vector = Vector()

    assert str(vector) == '(0.0, 0.0)'


def test_vector_equality():
    v1 = Vector()
    v2 = Vector()
    v3 = Vector(2, 10)

    assert v1 == v2
    assert not v1 == v3
    assert not v1 != v2
    assert v1 != v3


def test_vector_increment_decrement():
    v1 = Vector(1.2, 2.3)
    v2 = Vector(3.4, 4.5)

    v1 += v2
    assert v1.x == 4.6 and v1.y == 6.8

    v1 -= v2
    assert round(v1.x, 1) == 1.2 and round(v1.y, 1) == 2.3


def test_vector_sum_diff():
    v1 = Vector(1.2, 2.3)
    v2 = Vector(3.4, 4.5)

    assert (v1 + v2) == Vector(4.6, 6.8)
    assert (v2 - v1) == Vector(2.2, 2.2)


def test_check_type_exception():
    with pytest.raises(TypeError):
        v1 = Vector()
        v1 == dir


def test_vector_len():
    vector = Vector(2, 4)

    assert vector.len() == 4.47213595499958
