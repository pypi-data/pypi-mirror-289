from funcrpn import stack


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
