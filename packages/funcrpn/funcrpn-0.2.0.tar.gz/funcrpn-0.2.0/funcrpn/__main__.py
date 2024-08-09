"Main executable"

# Idk if you will read this, but today I'm really happy!

from funcrpn import stack, operators

NUMBER = 1
OPERATOR = 2


class NotACommandError(Exception):
    "The error to raise when you get a nonexistent command"
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self):
        return self.msg


def detect_type(val):
    """Detects the type of the input."""
    try:
        return float(val), NUMBER
    except ValueError:
        return val, OPERATOR


def evaluate(s, val):
    "Execute a command"
    v, t = detect_type(val)
    if t == NUMBER:
        return stack.push(s, v)
    match v:
        case "+":
            return operators.add(s)
        case "-":
            return operators.sub(s)
        case "*":
            return operators.mul(s)
        case "/":
            return operators.div(s)
        case "^":
            return operators.power(s)
        case "sq":
            return operators.sqrt(s)
        case _:
            raise NotACommandError("that is not an existent command")


def main():
    "Main function"
    # s = []
    print("ciao")


if __name__ == '__main__':
    main()
