def join(*ws):
    return ('').join(ws)

SPACE, TAB, LF = ' ', '\t', '\n'
STACK_MANIPULATION = SPACE
ARITHMETIC = TAB + SPACE
FLOW_CONTROL = LF
HEAP_ACCESS = TAB + TAB
IO = TAB + LF

PUSH = join(STACK_MANIPULATION, SPACE)
DUP = join(STACK_MANIPULATION, LF, SPACE)
SWAP = join(STACK_MANIPULATION, LF, TAB)
POP = join(STACK_MANIPULATION, LF, LF)
ADD = join(ARITHMETIC, SPACE, SPACE)
SUB = join(ARITHMETIC, SPACE, TAB)
MUL = join(ARITHMETIC, SPACE, LF)
DIV = join(ARITHMETIC, TAB, SPACE)
MOD = join(ARITHMETIC, TAB, TAB)
MARK = join(FLOW_CONTROL, SPACE, SPACE)
JUMP = join(FLOW_CONTROL, SPACE, LF)
JUMP_Z = join(FLOW_CONTROL, TAB, SPACE)
JUMP_N = join(FLOW_CONTROL, TAB, TAB)
EXIT = join(FLOW_CONTROL, LF, LF)
CALL = join(FLOW_CONTROL, SPACE, TAB)
END = join(FLOW_CONTROL, TAB, LF)
STORE = join(HEAP_ACCESS, SPACE)
LOAD = join(HEAP_ACCESS, TAB)
OUTC = join(IO, SPACE, SPACE)
OUTI = join(IO, SPACE, TAB)
INC = join(IO, TAB, SPACE)
INI = join(IO, TAB, TAB)
