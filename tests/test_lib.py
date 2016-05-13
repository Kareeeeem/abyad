import pytest

from src import lib
from src import exceptions

# Stack manipulation
# ==================


def test_pop():
    stack = [1, 2]
    stack = lib.pop(stack)
    assert stack == [1]


def test_push():
    stack = []
    stack = lib.push(stack, 1)
    assert stack == [1]


def test_swap():
    stack = [1, 2]
    stack = lib.swap(stack)
    assert stack == [2, 1]


def test_dup():
    stack = [1, 1]
    stack = lib.swap(stack)
    assert stack == [1, 1]


def test_pop_empty_stack():
    stack = []
    with pytest.raises(exceptions.StackError):
        lib.pop(stack)


def test_dup_empty_stack():
    stack = []
    with pytest.raises(exceptions.StackError):
        lib.dup(stack)


def test_swap_empty_stack():
    stack = []
    with pytest.raises(exceptions.StackError):
        lib.swap(stack)


def test_swap_one_item_in_stack():
    stack = [1]
    with pytest.raises(exceptions.StackError):
        lib.swap(stack)


# Arithmetic
# ==========


def test_add():
    stack = [1, 2, 3]
    stack = lib.add(stack)
    assert stack == [1, 5]


def test_mul():
    stack = [1, 2, 3]
    stack = lib.mul(stack)
    assert stack == [1, 6]


def test_sub():
    stack = [1, 2, 3]
    stack = lib.sub(stack)
    assert stack == [1, -1]


def test_div():
    stack = [1, 6, 2]
    stack = lib.div(stack)
    assert stack == [1, 3]


def test_mod():
    stack = [1, 5, 3]
    stack = lib.mod(stack)
    assert stack == [1, 2]


def test_left_right_empty_stack():
    stack = [1]
    with pytest.raises(exceptions.StackError):
        lib.get_stack_left_right(stack)


# Heap access


def test_store():
    stack = [5, 80]
    heap = {}
    _, heap = lib.store(stack, heap)
    assert heap == {5: 80}


def test_store_only_one_item_in_stack():
    stack = [5]
    heap = {}
    with pytest.raises(exceptions.StackError):
        lib.store(stack, heap)


def test_store_empty_stack():
    stack = []
    heap = {}
    with pytest.raises(exceptions.StackError):
        lib.store(stack, heap)


def test_retrieve():
    heap = {5: 80}
    stack = [5]
    stack, _ = lib.retrieve(stack, heap)
    assert stack == [5, 80]


def test_retrieve_empty_stack():
    heap = {5: 80}
    stack = []
    with pytest.raises(exceptions.StackError):
        lib.retrieve(stack, heap)


def test_retrieve_key_not_in_heap():
    heap = {}
    stack = [5]
    with pytest.raises(exceptions.HeapError):
        lib.retrieve(stack, heap)
