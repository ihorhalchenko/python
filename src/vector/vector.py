from typing import Any
from math import hypot


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Any) -> bool:
        self.__check_type(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __iadd__(self, other: Any) -> 'Vector':
        self.__check_type(other)
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: Any) -> 'Vector':
        self.__check_type(other)
        self.x -= other.x
        self.y -= other.y
        return self

    def __add__(self, other: Any) -> 'Vector':
        self.__check_type(other)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Any) -> 'Vector':
        self.__check_type(other)
        return Vector(self.x - other.x, self.y - other.y)

    def __check_type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'Other param should be of type {self.__class__.__name__}')

    def len(self) -> float:
        return hypot(self.x, self.y)


if __name__ == '__main__':  # pragma: no cover
    vector1 = Vector(1.1, 2.2)
    vector2 = Vector(2.2, 3.3)

    if vector1 == vector2:
        print('yes')
    else:
        print('no')

    if vector1 != vector2:
        print('yes')
    else:
        print('no')

    vector1 += vector2
    print(vector1)
    vector1 -= vector2
    print(vector1)

    print(vector1.len())

    print(vector1 + vector2)
    print(vector1 - vector2)
