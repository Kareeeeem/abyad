import exceptions

# Stack manipulation

STACK_ERROR = 'Stack has too few items for operation.'
HEAP_ERROR = 'Location not found in heap.'


def push(stack, number):
    '''Push the number onto stack.'''
    stack.append(number)
    return stack


def pop(stack):
    '''Discard the top item on the stack.'''
    try:
        stack.pop()
    except IndexError:
        raise exceptions.StackError, STACK_ERROR
    return stack


def dup(stack):
    '''Duplicate the top item on the stack.'''
    try:
        stack.append(stack[-1])
    except IndexError:
        raise exceptions.StackError, STACK_ERROR
    return stack


def swap(stack):
    '''Swap the top two items on the stack.'''
    try:
        stack[-1], stack[-2] = stack[-2], stack[-1]
    except IndexError:
        raise exceptions.StackError, STACK_ERROR
    return stack

# Arithmetic
# Arithmetic commands operate on the top two items on the stack, and replace
# them with the result of the operation. The first item pushed is
# considered to be left of the operator.


def get_stack_left_right(stack):
    '''Take the last two items of the stack and return a tuple of the stack,
    the second to last, and the last element.
    '''
    try:
        stack, (left, right) = stack[:-2], stack[-2:]
    except ValueError:
        raise exceptions.StackError, STACK_ERROR
    return stack, left, right


def add(stack):
    '''Take last two items off the stack and replace them with the sum.'''
    stack, left, right = get_stack_left_right(stack)
    stack.append(left + right)
    return stack


def sub(stack):
    '''Take last two items off the stack and replace them with the
    substraction result.
    '''
    stack, left, right = get_stack_left_right(stack)
    stack.append(left - right)
    return stack


def mul(stack):
    '''Take last two items off the stack and replace them with the product.'''
    stack, left, right = get_stack_left_right(stack)
    stack.append(left * right)
    return stack


def div(stack):
    '''Take last two items off the stack and replace them with the integer
    division result.
    '''
    stack, left, right = get_stack_left_right(stack)
    stack.append(left / right)
    return stack


def mod(stack):
    '''Take last two items off the stack and replace them with the modulus.'''
    stack, left, right = get_stack_left_right(stack)
    stack.append(left % right)
    return stack


# Heap access
# Heap access commands look at the stack to find the address of items to
# be stored or retrieved. To store an item, push the address then the
# value and run the store command. To retrieve an item, push the address
# and run the retrieve command, which will place the value stored in the
# location at the top of the stack.


def store(stack, heap):
    '''Store the value at the top of the stack at the address stored at
    top-1 of the stack.
    '''
    try:
        address, value = stack[-2:]
    except ValueError:
        raise exceptions.StackError, STACK_ERROR
    heap[address] = value
    return stack, heap


def retrieve(stack, heap):
    '''Retrieve the value from the heap stored at the address at the top of the
    Stack.
    '''
    try:
        address = stack[-1]
    except IndexError:
        raise exceptions.StackError, STACK_ERROR

    try:
        value = heap[address]
    except KeyError:
        raise exceptions.HeapError, HEAP_ERROR

    stack.append(value)
    return stack, heap
