class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{",".join(self.items)}"


# 1. Измените алгоритм “из инфикса в постфикс” таким образом, чтобы он обрабатывал ошибки.

def check_char_type(char):
    if char in "^*/+-":
        return "operator"
    elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or char in "0123456789":
        return "operand"
    elif char == "(":
        return "open_bracket"
    elif char == ")":
        return "close_bracket"
    else:
        raise ValueError(f"Element has unknown type. It can been happened if you forgot place space between element or if you placed more then one space between two elements. Element: \"{char}\"")

def compare_char_types(char_1, char_2):
    if check_char_type(char_1) == "open_bracket" and check_char_type(char_2) == "close_bracket":
        raise ValueError("There is close bracket placed next to open bracket")
    elif check_char_type(char_2) == "open_bracket" and check_char_type(char_1) == "close_bracket":
        raise ValueError("There is open bracket placed next to close bracket")
    elif check_char_type(char_1) == check_char_type(char_2):
        raise ValueError(
            "There are two or more elements that have same type and placed one by one")

def validate(ex_as_list):
    brackets = Stack()
    previous = None
    current = None

    for index, char in enumerate(ex_as_list):
        if index != 0:
            previous = current
        current = char

        if index != 0:
            compare_char_types(previous, current)

        if char == "(":
            brackets.push(char)
        elif char == ")":
            if brackets.peek() == "(":
                brackets.pop()
            else:
                raise ValueError(
                    "Is close bracket but is not open bracket before it")

    if not brackets.is_empty():
        raise ValueError("Open brackets more than close brackets")

def infix_to_postfix(infix_expr):
    token_list = infix_expr.split()

    validate(token_list)

    prec = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    op_stack = Stack()
    result = []

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            result.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while not op_stack.peek() == "(":
                result.append(op_stack.pop())
            if op_stack.peek() == "(":
                op_stack.pop()
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                result.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        result.append(op_stack.pop())

    return " ".join(result)


print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
