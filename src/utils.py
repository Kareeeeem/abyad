from itertools import chain
from tokens import SPACE, TAB, LF


def strip_comments(program):
    '''Only keep TAB, SPACE and LF in a program.'''
    return ('').join(char for char in program if char in [SPACE, TAB, LF])


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


def itows(i, minus=False, label=False):
    binary = str(bin(i))[2:]
    sign = []
    if not label:
        sign = [TAB if minus else SPACE]
    ws_digits = [SPACE if d == '0' else TAB for d in binary]
    return ('').join(chain(sign, ws_digits, [LF]))
