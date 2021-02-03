from pen_and_paper.paper import Paper


class OutOfInk(Exception):
    pass


class Pen:
    def __init__(self, ink_capacity: int = 4096) -> None:
        self._ink_capacity = int(ink_capacity)
        self._ink_amount = int(ink_capacity)

    @property
    def ink_capacity(self) -> int:
        return self._ink_capacity

    @property
    def ink_amount(self) -> int:
        return self._ink_amount

    def write(self, paper: Paper, message: str) -> None:
        message_len = len(message)

        if self._ink_amount == 0:
            raise OutOfInk()

        if message_len > self._ink_amount:
            message_len = self.ink_amount

        added_message_length = paper.add_content(message[0:message_len])
        self._ink_amount -= added_message_length

    def refill(self) -> None:
        self._ink_amount = self._ink_capacity


if __name__ == '__main__':  # pragma: no cover
    pen = Pen()
    paper1 = Paper(10)
    paper2 = Paper(5)
    paper3 = Paper()

    pen.write(paper1, 'Hello, world!')
    pen.write(paper2, 'Hello, world!')
    pen.write(paper3, 'Hello, world!')
    paper1.show()
    paper2.show()
    paper3.show()
