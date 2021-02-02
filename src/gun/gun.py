class NotReady(Exception):
    pass


class OutOfRounds(Exception):
    pass


class Gun:
    def __init__(self, model: str = 'Beretta', capacity: int = 8) -> None:
        self._model = model
        self._capacity = capacity
        self._amount = 0
        self._is_ready = False
        self._total_shots = 0

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def ready(self) -> bool:
        return self._is_ready

    @property
    def model(self) -> str:
        return self._model

    @property
    def total_shots(self) -> int:
        return self._total_shots

    def __str__(self) -> str:
        return f'Is gun ready: {self._is_ready}\n' \
               f'Number of rounds in the magazine: {self._amount}\n' \
               f'Magazine capacity: {self._capacity}\n' \
               f'Total number of shots: {self._total_shots}\n' \
               f'Model: {self._model}\n'

    def prepare(self) -> None:
        self._is_ready = not self._is_ready

    def reload(self) -> None:
        self._amount = self._capacity

    def shoot(self) -> None:
        if not self._is_ready:
            raise NotReady()

        if self._amount == 0:
            raise OutOfRounds()

        print("Bang!")
        self._amount -= 1
        self._total_shots += 1


if __name__ == '__main__':  # pragma: no cover
    gun = Gun()
    print(gun)
    print('-----------------------')
    gun.prepare()
    gun.reload()
    print(gun)
    print('-----------------------')
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    print(gun)
    print('-----------------------')
    gun.reload()
    print(gun)
    print('-----------------------')
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    print(gun)
