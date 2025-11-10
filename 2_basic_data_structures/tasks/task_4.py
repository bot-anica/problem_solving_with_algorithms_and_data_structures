# 4. Оберните результат предыдущего задания в калькулятор.

from data_structures import Stack


def check_char_type(char: str):
    if char in "^*/+-":
        return "operator"
    elif char.isnumeric():
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

def validate_ex_as_list(ex_as_list):
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

    validate_ex_as_list(ex_as_list)

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


def convert_infix_to_postfix_and_eval(infix_ex: str):
    postfix_ex = infix_to_postfix(infix_ex)
    result = postfix_eval(postfix_ex)

    return result


def show_help_message():
    print("Write math expression.\n"
          "It can includes math operators +, -, *, / and ^.\n"
          "Also It can includes brackets ( and ).\n"
          "Between each element of the expression should be space.\n"
          "Example of the right expression: 5 * 3 ^ ( 4 - 2 )\n")


def calculator():
    print("It is simple calculator.\n")

    show_help_message()

    while True:
        print("Write \"help\" to see calculator rules")
        user_ex = input("Your expression: ")

        if user_ex == "help":
            print()
            show_help_message()
            continue

        try:
            result = convert_infix_to_postfix_and_eval(user_ex)
        except ValueError as error:
            print(error)
            continue

        print(f"Result is: {result}")
        print("You can calculate 1 more expression\n")


def main():
    calculator()


if __name__ == "__main__":
    main()
