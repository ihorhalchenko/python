import pytest

from gun.gun import Gun, OutOfRounds, NotReady


@pytest.mark.parametrize('model, capacity', [
    ('Colt', 7),
    ('Glock 19', 17)
])
def test_gun_constructor(model, capacity):
    gun = Gun(model, capacity)

    assert gun.model == model
    assert gun.capacity == capacity
    assert gun.amount == 0
    assert not gun.ready
    assert gun.total_shots == 0


def test_gun_to_string():
    gun = Gun()

    assert str(gun) == 'Is gun ready: False\n' \
                       'Number of rounds in the magazine: 0\n' \
                       'Magazine capacity: 8\n' \
                       'Total number of shots: 0\n' \
                       'Model: Beretta\n'


def test_gun_prepare():
    gun = Gun()

    gun.prepare()

    assert gun.ready


def test_gun_reload():
    gun = Gun()

    gun.reload()
    gun.prepare()

    assert gun.amount == gun.capacity

    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.reload()

    assert gun.amount == gun.capacity


def test_gun_shoot():
    gun = Gun()

    gun.prepare()
    gun.reload()
    gun.shoot()
    gun.shoot()
    gun.shoot()

    assert gun.amount == 5
    assert gun.total_shots == 3

    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()

    assert gun.amount == 0
    assert gun.total_shots == 8

    gun.reload()

    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()

    assert gun.amount == 4
    assert gun.total_shots == 12


def test_gun_shoot_exception():
    gun = Gun()

    with pytest.raises(NotReady):
        gun.shoot()

    gun.prepare()

    with pytest.raises(OutOfRounds):
        gun.shoot()

    gun.reload()

    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()

    with pytest.raises(OutOfRounds):
        gun.shoot()
