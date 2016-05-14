import os
from src import interpreter
from src import lib
import programs


for program in programs.programs:
    programs.tows(program.program, program.name)


def read(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, name + '.wso'), 'rb') as f:
        program = f.read()
    return program


def test_stack_manipulation_program():
    state = lib.State()
    program = read(programs.stack_manipulation.name)
    interpreter.eval(program, state)
    assert state.stack == programs.stack_manipulation.stack


def test_stack_arithmetic_program():
    state = lib.State()
    program = read(programs.arithmetic.name)
    interpreter.eval(program, state)
    assert state.stack == programs.arithmetic.stack


def test_heap_program():
    state = lib.State()
    program = read(programs.heap.name)
    interpreter.eval(program, state)
    assert state.stack == programs.heap.stack


def test_count_program():
    state = lib.State()
    program = read(programs.count.name)
    interpreter.eval(program, state)
    assert state.stack == programs.count.stack


def test_program_termination():
    state = lib.State()
    program = read(programs.terminate.name)
    interpreter.eval(program, state)
    assert state.stack == programs.terminate.stack
