import os
from collections import namedtuple

from src.utils import join, itows
from src.tokens import SPACE, TAB, LF, PUSH, DUP, SWAP, POP, ADD, SUB, MUL, \
    DIV, MOD, MARK, JUMP, JUMP_Z, JUMP_N, EXIT, CALL, END, STORE, LOAD, OUTC, \
    OUTI, INC, INI


Program = namedtuple('Program', 'name program stack heap')
programs = []

ioread = Program(
    name='ioread',
    program=join(PUSH, itows(5), PUSH, itows(9), INC, INI, EXIT),
    stack=[],
    heap={9: ord('a'), 5: 1}
)
programs.append(ioread)

iowrite = Program(
    name='iowrite',
    program=join(PUSH, itows(5), PUSH, itows(97), OUTC, OUTI, EXIT),
    stack=[],
    heap={}
)
programs.append(iowrite)

subroutine = Program(
    name='subroutine',
    program=join(
        PUSH, itows(5),
        PUSH, itows(5),
        CALL, itows(45, label=True),
        EXIT,
        MARK, itows(45, label=True),
        MUL,
        END,
    ),
    stack=[25],
    heap={}
)
programs.append(subroutine)

comments_stack_manipulation = Program(
    'comments_stack_manipulation',
    join(
        SPACE, 'PUSH', SPACE, '5', SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, 'AND', SPACE, 'THEN', SPACE, 'PUSH', TAB, '7', TAB, TAB, LF,  # push 7
        SPACE, 'SWAP', LF, 'THE', TAB, 'TOP',  # swap
        SPACE, 'TWO', LF, 'ITEMS', SPACE, 'AND',  # duplicate
        SPACE, 'DUPLICATE', SPACE, 'AND', SPACE, 'PUSH', TAB, '9', SPACE, SPACE, TAB, LF,  # push 9
        SPACE, 'SWAP', LF, 'AGAIN', TAB,  # swap
        SPACE, 'AND', LF, 'POP', LF,  # pop
        LF, LF, LF,  # terminate
    ),
    stack=[7, 5, 9],
    heap={}
)
programs.append(comments_stack_manipulation)

stack_manipulation = Program(
    'stack_manipulation',
    join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # push 7
        SPACE, LF, TAB,  # swap
        SPACE, LF, SPACE,  # duplicate
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        SPACE, LF, TAB,  # swap
        SPACE, LF, LF,  # pop
        LF, LF, LF,  # terminate
    ),
    stack=[7, 5, 9],
    heap={}
)

programs.append(stack_manipulation)

arithmetic = Program(
    'arithmetic',
    join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # push 7
        TAB, SPACE, SPACE, SPACE,  # add - result = 12
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        TAB, SPACE, SPACE, TAB,  # sub - result = 3
        SPACE, SPACE, SPACE, TAB, SPACE, LF,  # push 2
        TAB, SPACE, TAB, TAB,  # mod - result = 1
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        SPACE, LF, TAB,  # swap
        TAB, SPACE, TAB, SPACE,  # div - result = 9
        LF, LF, LF,  # terminate
    ),
    stack=[9],
    heap={}
)
programs.append(arithmetic)

count = Program(
    'count',
    # this is the example program from compsoc.dur.ac.uk/whitespace/tutorial.html
    # without the IO.
    join(
        SPACE, SPACE, SPACE, TAB, LF,
        LF, SPACE, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, SPACE, TAB, TAB, LF,
        SPACE, SPACE, SPACE, TAB, LF,
        TAB, SPACE, SPACE, SPACE,
        SPACE, LF, SPACE,
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, TAB, LF,
        TAB, SPACE, SPACE, TAB,
        LF, TAB, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        LF, SPACE, LF, SPACE, TAB, SPACE, SPACE, SPACE, SPACE, TAB, TAB, LF,
        LF, SPACE, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        SPACE, LF, LF,
        LF, LF, LF,
    ),
    stack=[],
    heap={}
)


programs.append(count)

terminate = Program(
    'terminate',
    join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,
        SPACE, LF, TAB,
        LF, LF, LF,  # terminate
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # attempt to push again
    ),
    stack=[7, 5],
    heap={}
)
programs.append(terminate)

heap = Program(
    'heap',
    join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # push 7
        TAB, TAB, SPACE,  # store 7 at 5
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        TAB, TAB, TAB,  # retrieve 7
        TAB, SPACE, SPACE, TAB,  # sub  result = 2
        LF, LF, LF,  # terminate
    ),
    stack=[2],
    heap={5: 7}
)
programs.append(heap)

# this is the example program from compsoc.dur.ac.uk/whitespace/tutorial.html
iocount = Program(
    'iocount',
    join(
        SPACE, SPACE, SPACE, TAB, LF,
        LF, SPACE, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, SPACE, TAB, TAB, LF,
        SPACE, LF, SPACE,
        TAB, LF, SPACE, TAB,
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, SPACE, LF,
        TAB, LF, SPACE, SPACE,
        SPACE, SPACE, SPACE, TAB, LF,
        TAB, SPACE, SPACE, SPACE,
        SPACE, LF, SPACE,
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, TAB, LF,
        TAB, SPACE, SPACE, TAB,
        LF, TAB, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        LF, SPACE, LF, SPACE, TAB, SPACE, SPACE, SPACE, SPACE, TAB, TAB, LF,
        LF, SPACE, SPACE, SPACE, TAB, SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        SPACE, LF, LF,
        LF, LF, LF,
    ),
    stack=[],
    heap={}
)
programs.append(iocount)


def tows(program, name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, name + '.ws'), 'wb') as f:
        f.write(program)
