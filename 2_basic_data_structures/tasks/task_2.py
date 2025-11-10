# 2. Измените алгоритм вычисления постфиксного выражения таким образом, чтобы он обрабатывал ошибки.

from data_structures import Stack


def token_validation(token):
    if token.isalpha():
        raise ValueError(
            "Expression should includes only integer numbers and math operators: +, -, *, /, ^")

    if "." in token:
        raise ValueError("You can use only integer numbers.")

    # -1, -30 and so on
    if len(token) >= 2 and token[0] == "-" and token[1].isnumeric():
        raise ValueError("You can use only numbers more than 0.")


def postfix_eval(postfix_expr):
    op_stack = Stack()
    tokens_list = postfix_expr.split()

    for token in tokens_list:
        token_validation(token)

        if token.isnumeric():
            op_stack.push(int(token))
        else:
            if op_stack.size() >= 2:
                op2 = op_stack.pop()
                op1 = op_stack.pop()
                math_result = do_math(token, op1, op2)
                op_stack.push(math_result)
            else:
                raise ValueError("There is one or more extra mathematical operators. You should remove extra math operators or add missing operands (numbers).")

    if op_stack.size() > 1:
        raise ValueError("There is one or more extra operands (numbers). You should remove extra operands (numbers) or add missing math operators.")

    return op_stack.pop()


def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
            raise ValueError("Division by zero is prohibited.")
        return op1 / op2
    elif op == "^":
        return op1 ** op2
    else:
        raise ValueError("You used unknown math operator. You can use only +, -, *, / and ^.")


print(postfix_eval('7 8 + 3 2 + /'))
