from typing import Any


class Complex:
    def __init__(self, re: float = 0.0, im: float = 0.0) -> None:
        self._re = re
        self._im = im

    @property
    def re(self) -> float:
        return self._re

    @property
    def im(self) -> float:
        return self._im

    @re.setter
    def re(self, value: float) -> None:
        self._re = float(value)

    @im.setter
    def im(self, value: float) -> None:
        self._im = float(value)

    def __str__(self) -> str:
        out = f'{self.re}+{self.im}i'

        if self.im < 0:
            out = f'{self.re}-{self.im * -1}i'

        return out

    def __eq__(self, other: Any) -> bool:
        self.__check_type(other)
        return self.re == other.re and self.im == other.im

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __iadd__(self, other: Any) -> 'Complex':
        self.__check_type(other)
        self.re += other.re
        self.im += other.im
        return self

    def __isub__(self, other: Any) -> 'Complex':
        self.__check_type(other)
        self.re -= other.re
        self.im -= other.im
        return self

    def __add__(self, other: Any) -> 'Complex':
        self.__check_type(other)
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: Any) -> 'Complex':
        self.__check_type(other)
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other: Any) -> 'Complex':
        self.__check_type(other)
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re

        return Complex(re, im)

    def __check_type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'Other param should be of type {self.__class__.__name__}')


if __name__ == '__main__':  # pragma: no cover
    a = Complex(5, 3)
    b = Complex(4, 7)
    c = Complex(4, -7)

    if a == b:
        print('yes')
    else:
        print('no')

    if a != b:
        print('yes')
    else:
        print('no')

    print('--------------------')

    print(a)
    print(b)
    print(c)

    print('--------------------')

    a += b
    print(a)

    a -= b
    print(a)

    print('--------------------')

    print(a + b)
    print(a - b)
    print(a * b)
    print(a * c)
