from typing import Any


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value <= 0:
        raise ValueError(f'value should be positive, got {value} instead')
    return value


class UnitIsDeadException(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int, damage: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._max_hp = check_numeric(hp)
        self._damage = check_numeric(damage)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    @property
    def damage(self) -> int:
        return self._damage

    @hp.setter
    def hp(self, value) -> None:
        self._hp = value

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.max_hp}/{self.damage})'

    def __check_type(self, enemy: Any):
        if not isinstance(enemy, self.__class__):
            raise TypeError(f'enemy param should be of type {self.__class__.__name__}')

    def __ensure_is_alive(self):
        if self.hp == 0:
            raise UnitIsDeadException()

    def take_damage(self, damage) -> None:
        self.__ensure_is_alive()

        if self.hp - damage < 0:
            self.hp = 0
            return

        self.hp -= damage

    def attack(self, enemy: Any) -> None:
        self.__ensure_is_alive()
        self.__check_type(enemy)

        enemy.take_damage(self.damage)
        enemy.counter_attack(self)

    def counter_attack(self, enemy: Any) -> None:
        self.__ensure_is_alive()
        self.__check_type(enemy)

        enemy.take_damage(int(self.damage/2))


if __name__ == '__main__':  # pragma: no cover
    unit = Unit('SoLdIeR', 100, 30)
    rogue = Unit('Rogue', 100, 20)
    print(unit)
    print(rogue)
    unit.attack(rogue)
    print(unit)
    print(rogue)