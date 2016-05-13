import pytest
from itertools import chain

from src import exceptions
from src.parser import wstoi

SPACE = ' '
TAB = '\t'
LF = '\n'
POS = SPACE
NEG = TAB


def test_integer_parser():
    ws_integers = {}
    for i in xrange(1000):
        binary_string = str(bin(i))[2:]
        ws_integer_string = [SPACE if d == '0' else TAB for d in binary_string]
        pos = ('').join(chain([POS], ws_integer_string, [LF]))
        neg = ('').join(chain([NEG], ws_integer_string, [LF]))

        ws_integers[i] = pos
        ws_integers[i * -1] = neg
    assert all([wstoi(value) == key for key, value in ws_integers.iteritems()])


def test_integer_minus_parser():
    imin5 = [NEG, TAB, SPACE, TAB, LF]
    assert wstoi(imin5) == -5


def test_integer_parser_not_terminated():
    # integers should end with linefeed
    i = [POS, TAB, SPACE, TAB]
    with pytest.raises(exceptions.IntegerError):
        wstoi(i)


def test_integer_parser_unsigned():
    # integers should begin with SPACE or TAB sign.
    i = [LF, TAB, SPACE, TAB]
    with pytest.raises(exceptions.IntegerError):
        wstoi(i)


def test_integer_invalid_digits():
    # integers should begin with SPACE or TAB sign.
    i = [TAB, TAB, LF, TAB, LF]
    with pytest.raises(exceptions.IntegerError):
        wstoi(i)
