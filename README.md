# Abyad

A Whitespace interpreter written in Python. Purely as an exercise as I
have never written an interpreter. Abyad means white in Arabic.

# Specification
Copied from [here](http://compsoc.dur.ac.uk/whitespace/tutorial.html).

The only lexical tokens in the whitespace language are Space (ASCII 32),
Tab (ASCII 9) and Line Feed (ASCII 10).

The language itself is an imperative, stack based language. Each
command consists of a series of tokens, beginning with the Instruction
Modification Parameter (IMP). These are listed in the table below.

| IMP           | Meaning            |
| ------------- | ------------------ |
| [Space]       | Stack Manipulation |
| [Tab][Space]  | Arithmetic         |
| [Tab][Tab]    | Heap access        |
| [LF]          | Flow Control       |
| [Tab][LF]     | I/O                |

The virtual machine on which programs run has a stack and a heap. The
programmer is free to push arbitrary width integers onto the stack (only
integers, currently there is no implementation of floating point or real
numbers). The heap can also be accessed by the user as a permanent store
of variables and data structures.

Many commands require numbers or labels as parameters. Numbers can be
any number of bits wide, and are simply represented as a series of
[Space] and [Tab], terminated by a [LF]. [Space] represents the binary
digit 0, [Tab] represents 1. The sign of a number is given by its first
character, [Space] for positive and [Tab] for negative. Note that this
is not twos complement, it just indicates a sign.

Labels are simply [LF] terminated lists of spaces and tabs. There is only one
global namespace so all labels must be unique.

## Stack Manipulation (IMP: [Space])

Stack manipulation is one of the more common operations, hence the shortness
of the IMP [Space]. There are four stack instructions.

| Command        | Parameters | Meaning                             |
| -------------- | ---------- | ----------------------------------- |
| [Space]        | Number     | Push the number onto the stack      |
| [LF][Space]    | -          | Duplicate the top item on the stack |
| [LF][Tab]      | -          | Swap the top two items on the stack |
| [LF][LF]       | -          | Discard the top item on the stack   |

## Arithmetic (IMP: [Tab][Space])

Arithmetic commands operate on the top two items on the stack, and replace
them with the result of the operation. The first item pushed is considered to
be left of the operator.

| Command        | Parameters | Meaning          |
| -------------- | ---------- | ---------------- |
| [Space][Space] | -          | Addition         |
| [Space][Tab]   | -          | Subtraction      |
| [Space][LF]    | -          | Multiplication   |
| [Tab][Space]   | -          | Integer Division |
| [Tab][Tab]     | -          | Modulo           |

## Heap Access (IMP: [Tab][Tab])

Heap access commands look at the stack to find the address of items to
be stored or retrieved. To store an item, push the address then the
value and run the store command. To retrieve an item, push the address
and run the retrieve command, which will place the value stored in the
location at the top of the stack.

| Command        | Parameters | Meaning  |
| -------------- | ---------- | -------- |
| [Space]        | -          | Store    |
| [Tab]          | -          | Retrieve |

## Flow Control (IMP: [LF])

Flow control operations are also common. Subroutines are marked by
labels, as well as the targets of conditional and unconditional jumps,
by which loops can be implemented. Programs must be ended by means of
[LF][LF][LF] so that the interpreter can exit cleanly.

| Command        | Parameters | Meaning                                                  |
| -------------- | ---------- | -------------------------------------------------------- |
| [Space][Space] | Label      | Mark a location in the program                           |
| [Space][Tab]   | Label      | Call a subroutine                                        |
| [Space][LF]    | Label      | Jump unconditionally to a label                          |
| [Tab][Space]   | Label      | Jump to a label if the top of the stack is zero          |
| [Tab][Tab]     | Label      | Jump to a label if the top of the stack is negative      |
| [Tab][LF]      | -          | End a subroutine and transfer control back to the caller |
| [LF][LF]       | -          | End the program                                          |

## I/O (IMP: [Tab][LF])

Finally, we need to be able to interact with the user. There are IO
instructions for reading and writing numbers and individual characters.
With these, string manipulation routines can be written.

The read instructions take the heap address in which to store the result
from the top of the stack.

| Command        | Parameters | Meaning                                                                     |
| -------------- | ---------- | --------------------------------------------------------------------------- |
| [Space][Space] | -          | Output the character at the top of the stack                                |
| [Space][Tab]   | -          | Output the number at the top of the stack                                   |
| [Tab][Space]   | -          | Read a character and place it in the location given by the top of the stack |
| [Tab][Tab]     | -          | Read a number and place it in the location given by the top of the stack    |
