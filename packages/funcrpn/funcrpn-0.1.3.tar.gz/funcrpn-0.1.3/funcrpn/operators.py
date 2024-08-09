from funcrpn import stack
import math


def add(s):
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op1 + op2)


def sub(s):
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2 - op1)


def mul(s):
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op1 * op2)


def div(s):
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2 / op1)


def pow(s):
    s1, op1 = stack.pop(s)
    s2, op2 = stack.pop(s1)
    return stack.push(s2, op2**op1)


def sqrt(s):
    s1, op1 = stack.pop(s)
    return stack.push(s1, math.sqrt(op1))
