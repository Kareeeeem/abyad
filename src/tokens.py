def join(*ws):
    return ('').join(ws)

SPACE = ' '
TAB = '\t'
LF = '\n'

# Stack manipulation
PUSH = join(SPACE, SPACE)
DUP = join(SPACE, LF, SPACE)
SWAP = join(SPACE, LF, TAB)
POP = join(SPACE, LF, LF)

# Arithmetic
ADD = join(TAB, SPACE, SPACE, SPACE)
SUB = join(TAB, SPACE, SPACE, TAB)
MUL = join(TAB, SPACE, SPACE, LF)
DIV = join(TAB, SPACE, TAB, SPACE)
MOD = join(TAB, SPACE, TAB, TAB)

# Flow_control
MARK = join(LF, SPACE, SPACE)
JUMP = join(LF, SPACE, LF)
JUMP_Z = join(LF, TAB, SPACE)
JUMP_N = join(LF, TAB, TAB)
EXIT = join(LF, LF, LF)
CALL = join(LF, SPACE, TAB)
END = join(LF, TAB, LF)

# Heap access
STORE = join(TAB, TAB, SPACE)
LOAD = join(TAB, TAB, TAB)

# IO
OUTC = join(TAB, LF, SPACE, SPACE)
OUTI = join(TAB, LF, SPACE, TAB)
INC = join(TAB, LF, TAB, SPACE)
INI = join(TAB, LF, TAB, TAB)
