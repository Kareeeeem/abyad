from src import utils
from src import interpreter
from src import lib
from src.tokens import SPACE, TAB, LF


def test_stack_manipulation_program():
    state = lib.State()
    program = utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # push 7
        SPACE, LF, TAB,  # swap
        SPACE, LF, SPACE,  # duplicate
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        SPACE, LF, TAB,  # swap
        SPACE, LF, LF,  # pop
        LF, LF, LF,  # terminate
    )

    interpreter.eval(program, state)
    assert state.stack == [7, 5, 9]


def test_stack_arithmetic_program():
    state = lib.State()
    program = utils.join(
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
    )
    interpreter.eval(program, state)
    assert state.stack == [9]


def test_stack_heap_access_program():
    state = lib.State()
    program = utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # push 7
        TAB, TAB, SPACE,  # store 7 at 5
        SPACE, SPACE, SPACE, TAB, SPACE, SPACE, TAB, LF,  # push 9
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,  # push 5
        TAB, TAB, TAB,  # retrieve 7
        TAB, SPACE, SPACE, TAB,  # sub  result = 2
        LF, LF, LF,  # terminate
    )
    interpreter.eval(program, state)
    assert state.stack == [2]


def test_mark_program():
    state = lib.State()
    # this is the example program from compsoc.dur.ac.uk/whitespace/tutorial.html
    # without the IO.
    program = utils.join(
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
    )
    interpreter.eval(program, state)
    assert state.stack == []


def test_program_termination():
    state = lib.State()
    program = utils.join(
        SPACE, SPACE, SPACE, TAB, SPACE, TAB, LF,
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,
        SPACE, LF, TAB,
        LF, LF, LF,  # terminate
        SPACE, SPACE, SPACE, TAB, TAB, TAB, LF,  # attempt to push again
    )

    interpreter.eval(program, state)
    assert state.stack == [7, 5]
