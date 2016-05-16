from itertools import chain
from tokens import SPACE, TAB, LF
POS, NEG = SPACE, TAB


def join(*ws):
    return ('').join(ws)


visible_ws = {
    ' ': '[SPACE]',
    '\t': '[TAB]',
    '\n': '[LF]',
}


def print_ws(ws):
    visible = (' ').join([visible_ws[char] for char in ws])
    print visible


def itows(i, minus=False):
    binary = str(bin(i))[2:]
    sign = [NEG if minus else POS]
    ws_digits = [SPACE if d == '0' else TAB for d in binary]
    return ('').join(chain(sign, ws_digits, [LF]))
