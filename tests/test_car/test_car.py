import pytest

from car.car import Car, Point, OutOfFuel, ToMuchFuel


def test_car_constructor():
    car1 = Car()
    car2 = Car(70, 0.8, Point(1, 1), 'Toyota')

    assert car1.fuel_capacity == 60 and car1.fuel_consumption == 0.6 and car1.fuel_amount == 0
    assert car1.location.x == 0.0 and car1.location.y == 0.0
    assert car1.model == 'Mercedes'

    assert car2.fuel_capacity == 70 and car2.fuel_consumption == 0.8 and car2.fuel_amount == 0
    assert car2.location.x == 1.0 and car2.location.y == 1.0
    assert car2.model == 'Toyota'


@pytest.mark.parametrize('actual, expected', [
    (0, 30),
    (-100, 30),
    (20, 50)
])
def test_car_refill(actual, expected):
    car = Car()
    car.refill(30)
    car.refill(actual)
    assert car.fuel_amount == expected


@pytest.mark.parametrize('value, exception_type', [
    (100, ToMuchFuel),
    ('error', ValueError),
    (dir, TypeError)
])
def test_car_refill_exception(value, exception_type):
    car = Car()
    car.refill(30)

    with pytest.raises(exception_type):
        car.refill(value)


def test_car_drive_to_point():
    car = Car()
    car.refill(60)
    car.drive_to_point(Point(0, 0))
    assert round(car.fuel_amount, 2) == 60.00
    assert car.location == Point(0, 0)

    car.drive_to_point(Point(2, 2))
    assert round(car.fuel_amount, 2) == 58.30
    assert car.location == Point(2, 2)


@pytest.mark.parametrize('value, exception_type', [
    ('error', TypeError),
    (dir, TypeError),
    (Point(100, 100), OutOfFuel)
])
def test_car_drive_to_point_exception(value, exception_type):
    car = Car()

    with pytest.raises(exception_type):
        car.drive_to_point(value)


def test_car_drive():
    car = Car()
    car.refill(60)
    car.drive(0, 0)
    assert round(car.fuel_amount, 2) == 60.00
    assert car.location == Point(0, 0)

    car.drive(2, 2)
    assert round(car.fuel_amount, 2) == 58.30
    assert car.location == Point(2, 2)
