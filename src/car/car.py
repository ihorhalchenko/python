from point.point import Point


class OutOfFuel(Exception):
    pass


class ToMuchFuel(Exception):
    pass


class Car:
    def __init__(self,
                 capacity: float = 60,
                 consumption: float = 0.6,
                 location: Point = Point(0, 0),
                 model: str = 'Mercedes'
                 ) -> None:
        self._fuel_amount = 0
        self._fuel_capacity = float(capacity)
        self._fuel_consumption = float(consumption)
        self._model = str(model)
        self._location = location

    @property
    def fuel_amount(self) -> float:
        return self._fuel_amount

    @property
    def fuel_capacity(self) -> float:
        return self._fuel_capacity

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @property
    def location(self) -> Point:
        return self._location

    @property
    def model(self) -> str:
        return self._model

    def __str__(self) -> str:
        return f'Car location: {self._location}\n' \
               f'Fuel amount: {self._fuel_amount}\n' \
               f'Fuel capacity: {self._fuel_capacity}\n' \
               f'Fuel consumption: {self._fuel_consumption}\n' \
               f'Car model: {self._model}\n'

    def refill(self, fuel: float) -> None:
        fuel = float(fuel)

        if fuel <= 0:
            return

        if self._fuel_amount + fuel > self.fuel_capacity:
            raise ToMuchFuel()

        self._fuel_amount += fuel

    def drive_to_point(self, destination: Point) -> None:
        fuel_needed = self._location.distance(destination) * self.fuel_consumption

        if self._fuel_amount < fuel_needed:
            raise OutOfFuel()

        self._fuel_amount -= fuel_needed
        self._location = destination

    def drive(self, x: float, y: float) -> None:
        self.drive_to_point(Point(float(x), float(y)))


if __name__ == '__main__':  # pragma: no cover
    car = Car()
    print(car)
    car.refill(60)
    car.drive_to_point(Point(0, 0))
    print(car)
