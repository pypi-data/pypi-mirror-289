def push(stack: list, item) -> list:
    """Pushes an element into the stack
    Keyword arguments:
    stack -- the stack (a list or tuple is expected)
    item -- the item to push
    Return: the new stack, with the pushed element at the end.
    """

    return stack + [item]


def pop(stack: list) -> tuple:
    """Pops the last element from the stack.
    Keyword arguments:
    stack -- a list
    Return: the new stack and the last element
    """

    return stack[:-1], stack[-1]
