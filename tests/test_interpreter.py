import os
import mock

from src import interpreter
from src.state import State
import programs


for program in programs.programs:
    programs.tows(program.program, program.name)


def read(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, name + '.ws'), 'rb') as f:
        program = f.read()
    return program


# IO tests

def test_ioread_char():
    state = State()
    program = programs.ioread
    with mock.patch('sys.stdin.read', side_effect=['a', '1', '\n']):
        interpreter.eval(read(program.name), state)
        assert state.stack == program.stack and state.heap == program.heap


def test_iowrite(capfd):
    state = State()
    program = programs.iowrite
    interpreter.eval(read(program.name), state)
    assert state.stack == program.stack and state.heap == program.heap
    out, err = capfd.readouterr()
    assert out == 'a5'


def test_iocount(capfd):
    state = State()
    program = programs.iocount
    interpreter.eval(read(program.name), state)
    assert state.stack == program.stack and state.heap == program.heap
    out, err = capfd.readouterr()
    assert out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'


# Everything without IO

def execute_test(program):
    state = State()
    interpreter.eval(read(program.name), state)
    assert state.stack == program.stack and state.heap == program.heap


def test_routine_program():
    execute_test(programs.subroutine)


def test_stack_manipulation_program():
    execute_test(programs.stack_manipulation)


def test_stack_arithmetic_program():
    execute_test(programs.arithmetic)


def test_heap_program():
    execute_test(programs.heap)


def test_count_program():
    execute_test(programs.count)


def test_comment_program():
    execute_test(programs.comments_stack_manipulation)


def test_program_termination():
    execute_test(programs.terminate)
