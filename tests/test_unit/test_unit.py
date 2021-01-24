import pytest

from unit.unit import Unit, UnitIsDeadException,  prettify_string, check_numeric


@pytest.mark.parametrize('actual, expected', [
    ('SOLDIER', 'Soldier'),
    ('soldier\n', 'Soldier'),
    ('\tSoLdIeR', 'Soldier'),
    (' SoLdIeR ', 'Soldier'),
    ('Soldier', 'Soldier')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


def test_prettify_string_exception():
    with pytest.raises(TypeError):
        prettify_string(10000)


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (100.0, 100),
    ('100', 100)
])
def test_check_numeric(actual, expected):
    assert check_numeric(actual) == expected


@pytest.mark.parametrize('value, exception_type', [
    (-100, ValueError),
    (0, ValueError),
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)


@pytest.mark.parametrize('actual, expected', [
    (100, 0),
    (150, 0),
    (0, 100),
    (20, 80),
])
def test_take_damage(actual, expected):
    unit = Unit('Soldier', 100, 20)
    unit.take_damage(actual)
    assert unit.hp == expected


def test_take_damage_exception():
    with pytest.raises(UnitIsDeadException):
        unit = Unit('Soldier', 100, 20)
        unit.hp = 0
        unit.take_damage(10)


def test_attack_exception_alive():
    with pytest.raises(UnitIsDeadException):
        unit = Unit('Soldier', 100, 20)
        enemy = Unit('Enemy', 100, 20)
        enemy.hp = 0
        unit.attack(enemy)


@pytest.mark.parametrize('actual, expected', [
    (20, 80),
    (30, 70),
    (90, 10),
])
def test_attack(actual, expected):
    unit = Unit('Soldier', 100, actual)
    enemy = Unit('Enemy', 100, actual)
    unit.attack(enemy)
    enemy.hp = expected


def test_counter_attack_exception_alive():
    with pytest.raises(UnitIsDeadException):
        unit = Unit('Soldier', 100, 20)
        enemy = Unit('Enemy', 100, 20)
        enemy.hp = 0
        enemy.counter_attack(unit)


@pytest.mark.parametrize('actual, expected', [
    (20, 90),
    (30, 85),
    (90, 55),
])
def test_counter_attack(actual, expected):
    unit = Unit('Soldier', 100, actual)
    enemy = Unit('Enemy', 100, actual)
    enemy.counter_attack(unit)
    assert unit.hp == expected


