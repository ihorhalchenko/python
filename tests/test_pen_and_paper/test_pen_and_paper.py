import pytest

from pen_and_paper.pen import Pen, OutOfInk
from pen_and_paper.paper import Paper, OutOfSpace


@pytest.mark.parametrize('value', [
    10,
    100
])
def test_paper_constructor(value):
    paper = Paper(value)
    assert paper.max_symbols == value
    assert paper.symbols == 0


@pytest.mark.parametrize('free_space, message, added_message_length', [
    (13, 'Hello, world!', 13),
    (100, 'Lorem ipsum dolor sit amet', 26),
    (11, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 11)
])
def test_paper_add_content(free_space, message, added_message_length):
    paper = Paper(free_space)
    assert added_message_length == paper.add_content(message)


def test_paper_add_content_exception():
    paper1 = Paper(0)
    paper2 = Paper(10)

    with pytest.raises(OutOfSpace):
        paper1.add_content('Hello, world!')

    paper2.add_content('Hello, world!')

    with pytest.raises(OutOfSpace):
        paper2.add_content('Hello, world!')


@pytest.mark.parametrize('value', [
    10,
    100
])
def test_pen_constructor(value):
    pen = Pen(value)
    assert pen.ink_capacity == value
    assert pen.ink_amount == value


@pytest.mark.parametrize('ink_capacity, space_on_paper, message, expected_ink_amount', [
    (100, 100, 'Hello, world!', 87),
    (13, 100, 'Hello, world!', 0),
    (10, 100, 'Hello, world!', 0),
    (100, 10, 'Hello, world!', 90),
    (10, 5, 'Hello, world!', 5)
])
def test_pen_write(ink_capacity, space_on_paper, message, expected_ink_amount):
    pen = Pen(ink_capacity)
    paper = Paper(space_on_paper)

    pen.write(paper, message)
    assert pen.ink_amount == expected_ink_amount


def test_pen_write_exception():
    pen1 = Pen(0)
    pen2 = Pen(10)
    paper = Paper()

    with pytest.raises(OutOfInk):
        pen1.write(paper, 'Hello, world!')

    pen2.write(paper, 'Hello, world!')

    with pytest.raises(OutOfInk):
        pen2.write(paper, 'Hello, world!')


def test_pen_refill():
    pen = Pen(10)
    paper = Paper()

    pen.write(paper, 'Hello, world!')
    pen.refill()
    assert pen.ink_amount == 10

    pen.write(paper, 'Hello!')
    pen.refill()
    assert pen.ink_amount == 10

    pen.refill()
    assert pen.ink_amount == 10
