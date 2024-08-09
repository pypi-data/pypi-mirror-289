"Wrapper functions for the operators"

import math
from funcrpn import stack


def add(s):
    "Adds two numbers from the stack"
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op1 + op2)


def sub(s):
    "Calculates the difference of two numbers from the stack"
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2 - op1)


def mul(s):
    "Multiplicates two numbers from the stack"
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op1 * op2)


def div(s):
    "Divides 2 numbers from the stack"
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2 / op1)


def power(s):
    "Calculates a power"
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2**op1)


def sqrt(s):
    "Calculates a square root"
    s1, op1 = stack.pop(s)
    return stack.push(s1, math.sqrt(op1))
