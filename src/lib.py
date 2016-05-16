import operator
import exceptions


class State(object):
    STACK_ERROR = exceptions.StackError('Stack has too few items for operation.')
    HEAP_ERROR = exceptions.HeapError('Location not found in heap.')

    def __init__(self, stack=None, heap=None):
        self.stack = stack or []
        self.heap = heap or {}

    def execute(self, opcode, param=None):
        if param:
            return getattr(self, opcode)(param)
        else:
            return getattr(self, opcode)()

    # stack manipulation

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise self.STACK_ERROR

    def dup(self):
        try:
            self.stack.append(self.stack[-1])
        except IndexError:
            raise self.STACK_ERROR

    def swap(self):
        try:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        except IndexError:
            raise self.STACK_ERROR

    # heap access

    def store(self):
        value = self.pop()
        address = self.pop()
        self.heap[address] = value

    def load(self):
        address = self.pop()
        try:
            value = self.heap[address]
            self.push(value)
        except KeyError:
            raise self.HEAP_ERROR

    # arithmetic

    def calc(self, operator):
        right = self.pop()
        left = self.pop()
        value = operator(left, right)
        self.push(value)

    def add(self):
        self.calc(operator.add)

    def div(self):
        self.calc(operator.div)

    def mod(self):
        self.calc(operator.mod)

    def mul(self):
        self.calc(operator.mul)

    def sub(self):
        self.calc(operator.sub)
