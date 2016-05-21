import sys

from exc import EOF, IntegerError
from instructions import ParamTypes, instructionset
from lib import State
import tokens


def write_char(c):
    sys.stdout.write(chr(c))


def write_num(i):
    sys.stdout.write(str(i))


def read_char():
    return ord(sys.stdin.read(1))


def read_num():
    digits = []
    c = sys.stdin.read(1)
    while c.isdigit():
        digits.append(c)
        c = sys.stdin.read(1)
    try:
        return int(('').join(digits))
    except ValueError:
        raise IntegerError('Expecter an integer')


def get_param(ws, ip, signed=False):
    '''Return a parameter and the advanced pointer.'''
    begin = ip
    while ws[ip] != tokens.LF:
        ip += 1
    ip += 1  # advance past the LF
    return wstoi(ws[begin:ip], signed=True), ip


def wstoi(ws, signed=True):
    '''Converts Whitespace params into integers.
    Labels are the same but aren't signed.

    param ws string: A whitespace string such as "[Space][Tab][Tab][LF]".
    param signed bool: indicating the param is signed to indicate pos or neg.
    returns: Integer
    '''
    if not (ws[-1] == tokens.LF and
            all([d in (tokens.SPACE, tokens.TAB) for d in ws[:-1]])):
        raise IntegerError('Invalid integer')

    begin = 1 if signed else 0
    integer = int(('').join(['1' if d == tokens.TAB else '0' for d in ws[begin:-1]]), 2)

    if signed and ws[0] == tokens.TAB:
        integer *= -1

    return integer


def get_next_instruction(ws, ip, instructions):
    for ins in instructions:
        if ws[ip:].startswith(ins.token):
            ip += len(ins.token)
            return ins, ip
    raise EOF('File or program ended unexpectedly, most likely due to a '
              'syntax error or the program was not terminated properly with '
              '\\n\\n\\n.')


def get_signed(instr):
    return instr.param_type == ParamTypes.INTEGER


def set_marks(ws):
    '''Walk the entire file looking for marks.'''
    ip = 0
    marks = {}

    while ip < len(ws):
        try:
            ins, ip = get_next_instruction(ws, ip, instructionset)
        except EOF:
            break
        if ins.param_type is not None:
            param, ip = get_param(ws, ip, signed=get_signed(ins))
            if ins.token == tokens.MARK:
                marks[param] = ip
    return marks


def eval(ws, state=None):
    ip = 0
    state = state or State()
    marks = set_marks(ws)
    callstack = []

    while True:
        ins, ip = get_next_instruction(ws, ip, instructionset)

        param = None
        if ins.param_type is not None:
            param, ip = get_param(ws, ip, signed=get_signed(ins))

        if ins.token == tokens.EXIT:
            break

        elif ins.token == tokens.END:
            ip = callstack.pop()

        elif any([(ins.token == tokens.JUMP_N and state.pop() < 0),
                  (ins.token == tokens.JUMP_Z and state.pop() == 0),
                  ins.token == tokens.JUMP]):
            ip = marks[param]

        elif ins.token == tokens.CALL:
            callstack.append(ip)
            ip = marks[param]

        elif ins.token in [tokens.PUSH, tokens.POP, tokens.SWAP, tokens.DUP,  # stack manipulation
                           tokens.ADD, tokens.SUB, tokens.MUL, tokens.DIV, tokens.MOD,  # arithmetic
                           tokens.STORE, tokens.LOAD]:  # heap access
            state.execute(ins.opcode, param)

        elif ins.token == tokens.INC:
            state.push(read_char())
            state.store()

        elif ins.token == tokens.INI:
            state.push(read_num())
            state.store()

        elif ins.token == tokens.OUTC:
            write_char(state.pop())

        elif ins.token == tokens.OUTI:
            write_num(state.pop())

    return state
