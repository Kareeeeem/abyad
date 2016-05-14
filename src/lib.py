import operator
import exceptions


class Stack(object):
    ERROR = 'Stack has too few items for operation.'

    def __init__(self, stack=None):
        self.stack = stack or []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            self.raise_()

    def dup(self):
        try:
            self.stack.append(self.stack[-1])
        except IndexError:
            self.raise_()

    def swap(self):
        try:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        except IndexError:
            self.raise_()

    def calc(self, operator):
        right = self.pop()
        left = self.pop()
        value = operator(left, right)
        self.push(value)

    def raise_(self):
        raise exceptions.StackError(self.ERROR)


class Heap(object):
    ERROR = 'Location not found in heap.'

    def __init__(self, heap=None):
        self.heap = heap or {}

    def store(self, address, value):
        self.heap[address] = value

    def retrieve(self, address):
        try:
            return self.heap[address]
        except KeyError:
            self.raise_()

    def raise_(self):
        raise exceptions.HeapError(self.ERROR)


class State(object):
    def __init__(self, stack=None, heap=None):
        self._stack = Stack(stack)
        self._heap = Heap(heap)

    @property
    def stack(self):
        return self._stack.stack

    @property
    def heap(self):
        return self._heap.heap

    def push(self, value):
        self._stack.push(value)

    def pop(self):
        return self._stack.pop()

    def dup(self):
        self._stack.dup()

    def swap(self):
        self._stack.swap()

    def store(self):
        value = self.pop()
        address = self.pop()
        self._heap.store(address, value)

    def retrieve(self):
        address = self.pop()
        value = self._heap.retrieve(address)
        self.push(value)

    def add(self):
        self._stack.calc(operator.add)

    def div(self):
        self._stack.calc(operator.div)

    def mod(self):
        self._stack.calc(operator.mod)

    def mul(self):
        self._stack.calc(operator.mul)

    def sub(self):
        self._stack.calc(operator.sub)
