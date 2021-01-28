import pytest

from unit.unit import prettify_string, check_numeric, Unit, UnitIsDeadException


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
    ('error', ValueError),
    (dir, TypeError)
])
def test_check_numeric_exception(value, exception_type):
    with pytest.raises(exception_type):
        check_numeric(value)


def test_unit_constructor():
    soldier = Unit('Soldier', 100, 20)

    assert soldier.name == 'Soldier'
    assert soldier.hp == 100
    assert soldier.max_hp == 100
    assert soldier.damage == 20


def test_unit_to_string():
    soldier = Unit('Soldier', 100, 20)

    assert str(soldier) == 'Soldier: (100/100), dmg: 20'


def test_unit_setter():
    soldier = Unit('Soldier', 100, 20)

    assert soldier.hp == 100

    soldier.hp = 50
    assert soldier.hp == 50

    soldier.hp += 50
    assert soldier.hp == 100

    soldier.hp -= 90
    assert soldier.hp == 10

    with pytest.raises(ValueError):
        soldier.hp = -100

    assert soldier.hp == 10

    with pytest.raises(ValueError):
        soldier.hp -= 100

    assert soldier.hp == 10


@pytest.mark.parametrize('actual, expected', [
    (100, 100),
    (50, 100),
    (-100, 50),
    (0, 50),
    (25, 75)
])
def test_add_hit_points(actual, expected):
    unit = Unit('Soldier', 100, 20)
    unit.hp = 50
    unit.add_hit_points(actual)
    assert unit.hp == expected


def test_unit_attack():
    soldier = Unit('Soldier', 100, 20)
    warrior = Unit('Warrior', 100, 20)

    assert soldier.hp == 100
    assert warrior.hp == 100

    soldier.attack(warrior)

    assert soldier.hp == 90
    assert warrior.hp == 80


def test_unit_attack_exception():
    soldier = Unit('Soldier', 0, 20)
    warrior = Unit('Warrior', 100, 20)

    with pytest.raises(UnitIsDeadException):
        soldier.attack(warrior)

    with pytest.raises(UnitIsDeadException):
        soldier.counter_attack(warrior)

    with pytest.raises(UnitIsDeadException):
        soldier.take_damage(warrior.damage)

    with pytest.raises(TypeError):
        warrior.attack(dir)


def test_damage_greater_than_hp():
    soldier = Unit('Soldier', 20, 20)

    soldier.take_damage(30)
    assert soldier.hp == 0
