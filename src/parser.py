import exceptions

SPACE = ' '
TAB = '\t'
LF = '\n'
POS = SPACE
NEG = TAB


def wstoi(ws_integer):
    '''Whitespace integers are represented in binary form where [Space] means
    the binary digit 0, and [Tab] means the binary digit 1.
    The first character signs the integer with [Space] meaning positive, and
    [Tab] meaning negative. It it terminated at the end with [LF].
    This function converts those integers to normal integers.

    param ws_integer: A whitespace string such as
        "[Space][Space][Tab][Space][Tab][Tab][LF]".

    returns: Integer
    '''

    conditions = [
        ws_integer[0] in (SPACE, TAB),  # is signed
        ws_integer[-1] == LF,  # is terminated
        all([d in (SPACE, TAB) for d in ws_integer[1:-1]]),  # all valid digits
    ]

    if not all(conditions):
        raise exceptions.IntegerError, 'Invalid integer.'

    minus = ws_integer[0] == TAB

    binary = ['1' if d == TAB else '0' for d in ws_integer[1:-1]]
    binary = ('').join(binary)
    integer = int(binary, 2)

    if minus:
        integer *= -1

    return integer
