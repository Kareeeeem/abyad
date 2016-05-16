import os
from collections import namedtuple

from src.tokens import SPACE, TAB, LF
from src import utils


Program = namedtuple('Program', 'name program stack heap')
programs = []

ioread = Program(
    name='ioread',
    program=utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        TAB, LF, TAB, SPACE,  # read char
        TAB, LF, TAB, TAB,  # read int
        LF, LF, LF,  # terminate
    ),
    stack=[],
    heap={9: ord('a'), 5: 1}
)
programs.append(ioread)

iowrite = Program(
    name='iowrite',
    program=utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, SPACE, SPACE, SPACE, SPACE, TAB, LF,  # push 97
        TAB, LF, SPACE, SPACE,  # write char
        TAB, LF, SPACE, TAB,  # write int
        LF, LF, LF,  # terminate
    ),
    stack=[],
    heap={}
)
programs.append(iowrite)

subroutine = Program(
    name='subroutine',
    program=utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        LF, SPACE, LF, TAB, SPACE, TAB, TAB, SPACE, TAB, LF,  # call routine
        LF, LF, LF,  # terminate
        LF, SPACE, SPACE, TAB, SPACE, TAB, TAB, SPACE, TAB, LF,  # mark routine
        TAB, SPACE, SPACE, LF,  # mul
        LF, TAB, LF  # end routine
    ),
    stack=[25],
    heap={}
)
programs.append(subroutine)

stack_manipulation = Program(
    'stack_manipulation',
    utils.join(
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
    utils.join(
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
    utils.join(
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
    utils.join(
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
    utils.join(
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
    utils.join(
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
