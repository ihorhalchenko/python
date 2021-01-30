import pytest

from complex.complex import Complex


@pytest.mark.parametrize('re, im', [
    (0.0, 0.0),
    (1.1, 2.2)
])
def test_complex_constructor(re, im):
    complex_number = Complex(re, im)
    assert complex_number.re == re
    assert complex_number.im == im


def test_complex_setters():
    complex_number = Complex()

    complex_number.re = 42.0
    complex_number.im = 43.0

    assert complex_number.re == 42
    assert complex_number.im == 43


@pytest.mark.parametrize('value, exception_type', [
    ('error', ValueError),
    (dir, TypeError)
])
def test_complex_setters_exception(value, exception_type):
    complex_number = Complex()

    with pytest.raises(exception_type):
        complex_number.re = value

    with pytest.raises(exception_type):
        complex_number.im = value


def test_complex_to_string():
    complex_number = Complex()
    assert str(complex_number) == '0.0+0.0i'

    complex_number = Complex(2, 3)
    assert str(complex_number) == '2+3i'

    complex_number = Complex(2, -3)
    assert str(complex_number) == '2-3i'


def test_complex_equality():
    c1 = Complex()
    c2 = Complex()
    c3 = Complex(2, 10)

    assert c1 == c2
    assert not c1 == c3
    assert c1 != c3
    assert not c1 != c2


def test_complex_increment_decrement():
    c1 = Complex(1.2, 2.3)
    c2 = Complex(3.4, 4.5)

    c1 += c2
    assert c1.re == 4.6 and c1.im == 6.8

    c1 -= c2
    assert round(c1.re, 1) == 1.2 and round(c1.im, 1) == 2.3


def test_complex_sum_diff():
    c1 = Complex(1.2, 2.3)
    c2 = Complex(3.4, 4.5)

    assert c1 + c2 == Complex(4.6, 6.8)
    assert c2 - c1 == Complex(2.2, 2.2)


def test_complex_multiplication():
    c1 = Complex(1.2, 2.3)
    c2 = Complex(3.4, 4.5)
    c3 = Complex(-2, -4)

    c4 = c1 * c2
    c5 = c1 * c3

    assert round(c4.re, 2) == -6.27 and round(c4.im, 2) == 13.22
    assert round(c5.re, 1) == 6.8 and round(c5.im, 1) == -9.4


def test_type_exception():
    with pytest.raises(TypeError):
        c1 = Complex()
        c1 == dir
