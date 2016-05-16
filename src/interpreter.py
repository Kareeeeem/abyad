import sys

from exc import EOF, IntegerError
from tokens import SPACE, TAB, LF
from instructions import Types, OpCodes, Instruction, IMP


def write_char(c):
    sys.stdout.write(chr(c))


def write_num(i):
    sys.stdout.write(str(i))


def read_char():
    return ord(sys.stdin.read(1))


def read_num():
    digits = []
    chr = sys.stdin.read(1)
    while chr.isdigit():
        digits.append(chr)
        chr = sys.stdin.read(1)
    if digits:
        return int(('').join(digits))


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
    for token, instruction_or_set in tokens.iteritems():
        if ws[ptr:].startswith(token):
            ptr += len(token)
            if isinstance(instruction_or_set, Instruction):
                return instruction_or_set, ptr
            else:
                return get_next_instruction(ws, ptr, instruction_or_set)
    raise EOF('File or program ended unexpectedly, most likely due to a '
              'syntax error or the program was not terminated properly with '
              '\\n\\n\\n.')


def get_signed(instr):
    return instr.param_type == Types.INTEGER


def set_marks(ws):
    '''Walk the entire file looking for marks.'''
    ptr = 0
    marks = {}

    while ptr < len(ws):
        try:
            instruction, ptr = get_next_instruction(ws, ptr, IMP)
        except EOF:
            break
        if instruction.param_type is not None:
            param, ptr = get_param(ws, ptr, signed=get_signed(instruction))
            if instruction == OpCodes.MARK:
                marks[param] = ptr
    return marks


def eval(ws, state):
    ptr = 0
    marks = set_marks(ws)
    callstack = []

    while True:
        instruction, ptr = get_next_instruction(ws, ptr, IMP)

        param = None
        if instruction.param_type is not None:
            param, ptr = get_param(ws, ptr, signed=get_signed(instruction))

        # FLOW CONTROL
        if instruction == OpCodes.EXIT:
            break

        elif instruction == OpCodes.END:
            ptr = callstack.pop()

        elif any([(instruction == OpCodes.JUMP_N and state.pop() < 0),
                  (instruction == OpCodes.JUMP_Z and state.pop() == 0),
                  (instruction == OpCodes.CALL or callstack.append(ptr)),
                  instruction == OpCodes.JUMP]):
            ptr = marks[param]

        # STACK MANIPULATION / HEAP ACCESS / ARITHMETIC
        elif instruction in [OpCodes.PUSH, OpCodes.POP, OpCodes.SWAP,
                             OpCodes.DUP, OpCodes.ADD, OpCodes.SUB,
                             OpCodes.MUL, OpCodes.DIV, OpCodes.MOD,
                             OpCodes.STORE, OpCodes.LOAD]:
            state.execute(instruction.opcode, param)

        elif instruction == OpCodes.INC:
            state.push(read_char())
            state.store()

        elif instruction == OpCodes.INI:
            num = read_num()
            if num:
                state.push(num)
                state.store()

        elif instruction == OpCodes.OUTC:
            write_char(state.pop())

        elif instruction == OpCodes.OUTI:
            write_num(state.pop())

    return state


if __name__ == '__main__':
    print 'hello'
