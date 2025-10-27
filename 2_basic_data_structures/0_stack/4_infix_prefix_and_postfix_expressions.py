from stack import Stack


def infix_to_postfix(infix_expr):
    prec = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    op_stack = Stack()
    token_list = infix_expr.split()
    result = []

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            result.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while not op_stack.peek() == "(":
                result.append(op_stack.pop())
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


def postfix_eval(postfix_expr):
    op_stack = Stack()
    tokens_list = postfix_expr.split()

    for token in tokens_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            math_result = do_math(token, op1, op2)
            op_stack.push(math_result)

    return op_stack.pop()


def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "^":
        return op1 ^ op2


print(postfix_eval('7 8 + 3 2 + /'))
