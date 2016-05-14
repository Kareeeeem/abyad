'''This module defines dictionary mappings to instructions.'''

from collections import namedtuple

import utils
from tokens import SPACE, TAB, LF

Instruction = namedtuple('Instruction', 'instruction type param_signed children')


class Types:
    STACK_MANIPULATION = 'STACK_MANIPULATION'
    HEAP_ACCESS = 'HEAP_ACCESS'
    FLOW_CONTROL = 'FLOW_CONTROL'
    ARITHMETIC = 'ARITHMETIC'
    IMP = 'IMP'


STACK_MANIPULATION = {
    SPACE: Instruction('push', Types.STACK_MANIPULATION, True, None),
    utils.join(LF, SPACE): Instruction('dup', Types.STACK_MANIPULATION, None, None),
    utils.join(LF, TAB): Instruction('swap', Types.STACK_MANIPULATION, None, None),
    utils.join(LF, LF): Instruction('pop', Types.STACK_MANIPULATION, None, None),
}

ARITHMETIC = {
    utils.join(SPACE, SPACE): Instruction('add', Types.ARITHMETIC, None, None),
    utils.join(SPACE, TAB): Instruction('sub', Types.ARITHMETIC, None, None),
    utils.join(SPACE, LF): Instruction('mul', Types.ARITHMETIC, None, None),
    utils.join(TAB, SPACE): Instruction('div', Types.ARITHMETIC, None, None),
    utils.join(TAB, TAB): Instruction('mod', Types.ARITHMETIC, None, None),
}

FLOW_CONTROL = {
    utils.join(SPACE, SPACE): Instruction('mark', Types.FLOW_CONTROL, False, None),
    utils.join(SPACE, LF): Instruction('jump', Types.FLOW_CONTROL, False, None),
    utils.join(TAB, SPACE): Instruction('jump_if_0', Types.FLOW_CONTROL, False, None),
    utils.join(TAB, TAB): Instruction('jump_if_neg', Types.FLOW_CONTROL, False, None),
    utils.join(LF, LF): Instruction('exit', Types.FLOW_CONTROL, None, None),
    utils.join(SPACE, TAB): Instruction('call', Types.FLOW_CONTROL, False, None),
    utils.join(TAB, LF): Instruction('end', Types.FLOW_CONTROL, None, None),
}

HEAP_ACCESS = {
    SPACE: Instruction('store', Types.HEAP_ACCESS, None, None),
    TAB: Instruction('retrieve', Types.HEAP_ACCESS, None, None),
}

IMP = {
    SPACE: Instruction(None, Types.IMP, None, STACK_MANIPULATION),
    LF: Instruction(None, Types.IMP, None, FLOW_CONTROL),
    utils.join(TAB, SPACE): Instruction(None, Types.IMP, None, ARITHMETIC),
    utils.join(TAB, TAB): Instruction(None, Types.IMP, None, HEAP_ACCESS),
    # utils.join(TAB, LF): IO,
}
