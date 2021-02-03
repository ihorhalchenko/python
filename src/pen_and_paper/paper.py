class OutOfSpace(Exception):
    pass


class Paper:
    def __init__(self, max_symbols: int = 4096) -> None:
        self._max_symbols = int(max_symbols)
        self._symbols = 0
        self._content = ''

    @property
    def max_symbols(self) -> int:
        return self._max_symbols

    @property
    def symbols(self) -> int:
        return self._symbols

    def add_content(self, message: str) -> int:
        message_length = len(message)
        free_space = self._max_symbols - self._symbols

        if free_space == 0:
            raise OutOfSpace()

        if message_length > free_space:
            message_length = free_space

        self._content += message[0:message_length]
        self._symbols += message_length

        return message_length

    def show(self) -> None:  # pragma: no cover
        print(self._content)
