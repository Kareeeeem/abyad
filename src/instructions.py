'''This module defines all instructions.'''
from collections import namedtuple

from tokens import PUSH, DUP, SWAP, POP, ADD, SUB, MUL, DIV, MOD, MARK, JUMP, \
    JUMP_Z, JUMP_N, EXIT, CALL, END, STORE, LOAD, OUTC, OUTI, INC, INI

Ins = namedtuple('Ins', 'opcode param_type token')


class ParamTypes:
    INTEGER = 'signed'
    LABEL = 'unsigned'


instructionset = [
    Ins('push', ParamTypes.INTEGER, PUSH),
    Ins('pop', None, POP),
    Ins('swap', None, SWAP),
    Ins('dup', None, DUP),
    Ins('add', None, ADD),
    Ins('sub', None, SUB),
    Ins('mul', None, MUL),
    Ins('div', None, DIV),
    Ins('mod', None, MOD),
    Ins('store', None, STORE),
    Ins('load', None, LOAD),
    Ins('mark', ParamTypes.LABEL, MARK),
    Ins('call', ParamTypes.LABEL, CALL),
    Ins('j', ParamTypes.LABEL, JUMP),
    Ins('jz', ParamTypes.LABEL, JUMP_Z),
    Ins('jn', ParamTypes.LABEL, JUMP_N),
    Ins('end', None, END),
    Ins('exit', None, EXIT),
    Ins('read_char', None, INC),
    Ins('read_num', None, INI),
    Ins('write_char', None, OUTC),
    Ins('write_num', None, OUTI),
]
