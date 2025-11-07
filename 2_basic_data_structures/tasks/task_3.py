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


# 3. Создайте направленный инфиксный вычислитель, который совмещает
# функциональность преобразования из инфикса в постфикс
# и алгоритм постфиксных вычислений.


def token_validation(token):
    if token.isalpha():
        print(token)
        raise ValueError(
            "Expression should includes only integer numbers and math operators: +, -, *, /, ^")

    if "." in token:
        raise ValueError("You can use only integer numbers.")

    # -1, -30 and so on
    if len(token) >= 2 and token[0] == "-" and token[1].isnumeric():
        raise ValueError("You can use only numbers more than 0.")


def infix_to_postfix(ex: str):
    ex_as_list = ex.split()

    prec = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    operators = Stack()
    result_list = []

    for token in ex_as_list:
        token_validation(token)

        if token.isnumeric():
            result_list.append(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                result_list.append(operators.pop())

            if operators.peek() == "(":
                operators.pop()
            else:
                raise ValueError("There is not open bracket before close bracket")
        elif token in "+-*/^":
            while not operators.is_empty() and prec[operators.peek()] > prec[token]:
                result_list.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        result_list.append(operators.pop())

    return " ".join(result_list)


print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))


def do_math(operand, op1, op2):
    if operand == "+":
        return op1 + op2
    elif operand == "-":
        return op1 - op2
    elif operand == "*":
        return op1 * op2
    elif operand == "/":
        return op1 / op2
    elif operand == "^":
        return op1 ** op2

def postfix_eval(ex: str):
    ex_as_list = ex.split()

    operands = Stack()

    for token in ex_as_list:
        token_validation(token)

        if token.isnumeric():
            operands.push(int(token))
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.push(do_math(token, op1, op2))

    return operands.pop()


print(postfix_eval('7 8 + 3 2 + /'))


def convert_infix_to_postfix_and_eval(infix_ex: str):
    postfix_ex = infix_to_postfix(infix_ex)
    result = postfix_eval(postfix_ex)

    return result


print(convert_infix_to_postfix_and_eval("5 * 3 ^ ( 4 - 2 )"))
