'''This module defines dictionary mappings to instructions.'''
from collections import namedtuple

from utils import join
from tokens import SPACE, TAB, LF

Instruction = namedtuple('Instruction', 'opcode param_type')


class Types:
    INTEGER = 'signed'
    LABEL = 'unsigned'


class OpCodes:
    # stack manipulation
    PUSH = Instruction('push', Types.INTEGER)
    POP = Instruction('pop', None)
    SWAP = Instruction('swap', None)
    DUP = Instruction('dup', None)

    # arithmetic
    ADD = Instruction('add', None)
    SUB = Instruction('sub', None)
    MUL = Instruction('mul', None)
    DIV = Instruction('div', None)
    MOD = Instruction('mod', None)

    # heap access
    STORE = Instruction('store', None)
    LOAD = Instruction('load', None)

    # flow control
    MARK = Instruction('mark', Types.LABEL)
    CALL = Instruction('call', Types.LABEL)
    JUMP = Instruction('j', Types.LABEL)
    JUMP_Z = Instruction('jz', Types.LABEL)
    JUMP_N = Instruction('jn', Types.LABEL)
    END = Instruction('end', None)
    EXIT = Instruction('exit', None)

    # IO
    INC = Instruction('read_char', None)
    INI = Instruction('read_num', None)
    OUTC = Instruction('write_char', None)
    OUTI = Instruction('write_num', None)

STACK_MANIPULATION = {
    SPACE: OpCodes.PUSH,
    join(LF, SPACE): OpCodes.DUP,
    join(LF, TAB): OpCodes.SWAP,
    join(LF, LF): OpCodes.POP,
}

ARITHMETIC = {
    join(SPACE, SPACE): OpCodes.ADD,
    join(SPACE, TAB): OpCodes.SUB,
    join(SPACE, LF): OpCodes.MUL,
    join(TAB, SPACE): OpCodes.DIV,
    join(TAB, TAB): OpCodes.MOD,
}

FLOW_CONTROL = {
    join(SPACE, SPACE): OpCodes.MARK,
    join(SPACE, LF): OpCodes.JUMP,
    join(TAB, SPACE): OpCodes.JUMP_Z,
    join(TAB, TAB): OpCodes.JUMP_N,
    join(LF, LF): OpCodes.EXIT,
    join(SPACE, TAB): OpCodes.CALL,
    join(TAB, LF): OpCodes.END,
}

HEAP_ACCESS = {
    SPACE: OpCodes.STORE,
    TAB: OpCodes.LOAD,
}


IO = {
    join(SPACE, SPACE): OpCodes.OUTC,
    join(SPACE, TAB): OpCodes.OUTI,
    join(TAB, SPACE): OpCodes.INC,
    join(TAB, TAB): OpCodes.INI,
}

# INSTRUCTION MODIFICATION PARAMETERS
IMP = {
    SPACE: STACK_MANIPULATION,
    LF: FLOW_CONTROL,
    join(TAB, SPACE): ARITHMETIC,
    join(TAB, TAB): HEAP_ACCESS,
    join(TAB, LF): IO,
}
