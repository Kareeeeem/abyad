import os
from src import interpreter
from src import lib
import programs


for program in programs.programs:
    programs.tows(program.program, program.name)


def read(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, name + '.ws'), 'rb') as f:
        program = f.read()
    return program


def execute_test(program):
    state = lib.State()
    interpreter.eval(read(program.name), state)
    assert state.stack == program.stack and state.heap == program.heap


def test_ioread_program():
    # INPUT 'a1' at prompt while running tests
    print 'input the string "a1" '
    execute_test(programs.ioread)


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


def test_program_termination():
    execute_test(programs.terminate)
