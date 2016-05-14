from exceptions import EOF, IntegerError
from tokens import SPACE, TAB, LF
from instructions import Types, IMP


def get_param(ws, ptr, signed=False):
    '''Return a parameter and the advanced pointer.'''
    begin = ptr
    while ws[ptr] != LF:
        ptr += 1
    ptr += 1  # advance past the LF
    return wstoi(ws[begin:ptr], signed=True), ptr


def wstoi(ws, signed=True):
    '''Converts Whitespace params into integers.
    Labels are the same but aren't signed.

    param ws string: A whitespace string such as "[Space][Tab][Tab][LF]".
    param signed bool: indicating the param is signed to indicate pos or neg.
    returns: Integer
    '''
    if not (ws[-1] == LF and all([d in (SPACE, TAB) for d in ws[:-1]])):
        raise IntegerError('Invalid integer')

    begin = 1 if signed else 0
    integer = int(('').join(['1' if d == TAB else '0' for d in ws[begin:-1]]), 2)

    if signed and ws[0] == TAB:
        integer *= -1

    return integer


def get_next_instruction(ws, ptr, tokens):
    for token, instruction in tokens.iteritems():
        if ws[ptr:].startswith(token):
            ptr += len(token)
            if not instruction.children:
                return instruction, ptr
            else:
                return get_next_instruction(ws, ptr, instruction.children)
    raise EOF('File or program ended unexpectedly, most likely due to a '
              'syntax error or the program was not terminated properly with '
              '\\n\\n\\n.')


def set_marks(ws):
    '''Walk the entire file looking for marks.'''
    ptr = 0
    marks = {}

    while ptr < len(ws):
        try:
            instruction, ptr = get_next_instruction(ws, ptr, IMP)
        except EOF:
            break
        if instruction.param_signed is not None:
            param, ptr = get_param(ws, ptr, signed=instruction.param_signed)
            if instruction.instruction == 'mark':
                marks[param] = ptr
    return marks


def eval(ws, state):
    ptr = 0
    marks = set_marks(ws)
    # callstack = []

    while True:
        instruction, ptr = get_next_instruction(ws, ptr, IMP)

        if instruction.param_signed is not None:
            param, ptr = get_param(ws, ptr, signed=instruction.param_signed)
        else:
            param = None

        if instruction.type == Types.FLOW_CONTROL:
            if instruction.instruction == 'exit':
                break
            elif instruction.instruction == 'jump_if_neg' and state.pop() < 0:
                ptr = marks[param]
            elif instruction.instruction == 'jump_if_0' and state.pop() == 0:
                ptr = marks[param]
            elif instruction.instruction == 'jump':
                ptr = marks[param]
            # elif instruction.instruction == 'call':
            #     callstack.append(ptr)
            #     ptr = marks[param]
            # elif instruction.instruction == 'end':
            #     ptr = callstack.pop()

        elif instruction.type in [Types.STACK_MANIPULATION, Types.ARITHMETIC,
                                  Types.HEAP_ACCESS]:
            if param:
                getattr(state, instruction.instruction)(param)
            else:
                getattr(state, instruction.instruction)()

    return state
