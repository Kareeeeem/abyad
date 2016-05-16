import pytest

from src import exc
from src.utils import itows
from src.interpreter import wstoi
from src.tokens import SPACE, TAB, LF

POS = SPACE
NEG = TAB


def test_integer_parser():
    assert all([wstoi(itows(i, minus=False)) == i and
                wstoi(itows(i, minus=True)) == i * -1
                for i in xrange(1000)])


def test_integer_parser_not_terminated():
    # integers should end with linefeed
    i = [POS, TAB, SPACE, TAB]
    with pytest.raises(exc.IntegerError):
        wstoi(i)


def test_integer_parser_unsigned():
    # integers should begin with SPACE or TAB sign.
    i = [LF, TAB, SPACE, TAB]
    with pytest.raises(exc.IntegerError):
        wstoi(i)


def test_integer_invalid_digits():
    # integers should begin with SPACE or TAB sign.
    i = [TAB, TAB, LF, TAB, LF]
    with pytest.raises(exc.IntegerError):
        wstoi(i)
