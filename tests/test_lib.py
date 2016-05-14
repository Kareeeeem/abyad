import pytest

from src import lib
from src import exceptions

# Stack manipulation
# ==================


def test_pop():
    state = lib.State(stack=[1, 2])
    state.pop()
    assert state.stack == [1]


def test_push():
    state = lib.State()
    state.push(1)
    assert state.stack == [1]


def test_swap():
    state = lib.State(stack=[1, 2])
    state.swap()
    assert state.stack == [2, 1]


def test_dup():
    state = lib.State(stack=[1, 1])
    state.swap()
    assert state.stack == [1, 1]


def test_pop_empty_stack():
    state = lib.State()
    with pytest.raises(exceptions.StackError):
        state.pop()


def test_dup_empty_stack():
    state = lib.State()
    with pytest.raises(exceptions.StackError):
        state.dup()


def test_swap_empty_stack():
    state = lib.State()
    with pytest.raises(exceptions.StackError):
        state.swap()


def test_swap_one_item_in_stack():
    state = lib.State(stack=[1])
    with pytest.raises(exceptions.StackError):
        state.swap()


# Arithmetic
# ==========


def test_add():
    state = lib.State(stack=[1, 2, 3])
    state.add()
    assert state.stack == [1, 5]


def test_mul():
    state = lib.State(stack=[1, 2, 3])
    state.mul()
    assert state.stack == [1, 6]


def test_sub():
    state = lib.State(stack=[1, 2, 3])
    state.sub()
    assert state.stack == [1, -1]


def test_div():
    state = lib.State(stack=[1, 6, 2])
    state.div()
    assert state.stack == [1, 3]


def test_mod():
    state = lib.State(stack=[1, 5, 3])
    state.mod()
    assert state.stack == [1, 2]


# Heap access


def test_store():
    state = lib.State(stack=[5, 80])
    state.store()
    assert state.heap == {5: 80}


def test_store_only_one_item_in_stack():
    state = lib.State(stack=[5])
    with pytest.raises(exceptions.StackError):
        state.store()


def test_store_empty_stack():
    state = lib.State()
    with pytest.raises(exceptions.StackError):
        state.store()


def test_retrieve():
    state = lib.State(heap={5: 80}, stack=[5])
    state.retrieve()
    assert state.stack == [80]


def test_retrieve_empty_stack():
    state = lib.State(heap={5: 80})
    with pytest.raises(exceptions.StackError):
        state.retrieve()


def test_retrieve_key_not_in_heap():
    state = lib.State(stack=[5])
    with pytest.raises(exceptions.HeapError):
        state.retrieve()
