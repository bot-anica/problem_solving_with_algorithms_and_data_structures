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


# 1. Преобразуйте следующие значения в двоичный вид, используя “деление на 2”. Выведите стек из остатков.
#
#     17
#     45
#     96


def convert_num_to_2(num):
    stack = Stack()
    current_num = num

    while current_num > 0:
        stack.push(current_num % 2)
        current_num = current_num // 2

    result = ''

    while not stack.is_empty():
        result += str(stack.pop())

    return result


print(convert_num_to_2(17))
print(convert_num_to_2(45))
print(convert_num_to_2(96))


# 2. Преобразуйте следующие инфиксные выражения в префиксные (используя полную расстановку скобок)
#
#     (A+B)*(C+D)*(E+F)
#     A+((B+C)*(D+E))
#     A*B*C*D+E+F


def infix_to_prefix(ex):
    precedence = { "^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1, }

    def is_operator(char):
        return char in "^*/+-"

    def has_higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    math_symbols = Stack()
    result_list = []

    for char in reversed(ex):
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or char in "0123456789":
            result_list.append(char)
        elif char == ")":
            math_symbols.push(char)
        elif char == "(":
            while not math_symbols.is_empty() and math_symbols.peek() != ")":
                result_list.append(math_symbols.pop())
            math_symbols.pop()
        elif is_operator(char):
            while not math_symbols.is_empty() and math_symbols.peek() != ")" and has_higher_precedence(math_symbols.peek(), char):
                result_list.append(math_symbols.pop())
            math_symbols.push(char)

    while not math_symbols.is_empty():
        result_list.append(math_symbols.pop())

    return "".join(reversed(result_list))


print(infix_to_prefix("(A+B)*(C+D)*(E+F)")) # **+AB+CD+EF
print(infix_to_prefix("A+((B+C)*(D+E))")) # +A*+BC+DE
print(infix_to_prefix("A*B*C*D+E+F"))  # ++***ABCDEF
print(infix_to_prefix("A*B+C/D"))  # +*AB/CD


# 3. Преобразуйте приведённые выше инфиксные выражения в постфиксные (используя полную расстановку скобок).
#
#     (A+B)*(C+D)*(E+F)
#     A+((B+C)*(D+E))
#     A*B*C*D+E+F

def infix_to_postfix(ex):
    precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1, }

    math_symbols = Stack()
    result_list = []

    for char in ex:
        if char in "0123456789" or char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result_list.append(char)
        elif char == "(":
            math_symbols.push(char)
        elif char == ")":
            while not math_symbols.is_empty() and math_symbols.peek() != "(":
                result_list.append(math_symbols.pop())

            math_symbols.pop()
        elif char in "^*/+-":
            while not math_symbols.is_empty() and precedence[math_symbols.peek()] >= precedence[char]:
                result_list.append(math_symbols.pop())
            math_symbols.push(char)

    while not math_symbols.is_empty():
        result_list.append(math_symbols.pop())

    return "".join(result_list)


print(infix_to_postfix("(A+B)*(C+D)*(E+F)"))
print(infix_to_postfix("A+((B+C)*(D+E))"))
print(infix_to_postfix("A*B*C*D+E+F"))
print(infix_to_postfix("A*B+C/D"))


# 4. Вычислите следующие постфиксные выражения. Выведите стек в процессе обработки каждого операнда и оператора.
#
#     2 3 * 4 +
#     1 2 + 3 + 4 + 5 +
#     1 2 3 4 5 * + * +


def make_math(op1, op2, action):
    if action == "^":
        return op1 ^ op2
    elif action == "*":
        return op1 * op2
    elif action == "/":
        return op1 / op2
    elif action == "+":
        return op1 + op2
    elif action == "-":
        return op1 - op2

def calculate_postfix(ex):
    operands = Stack()
    ex_as_array = ex.split()

    for char in ex_as_array:
        if char in "0123456789":
            operands.push(int(char))
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.push(make_math(op1, op2, char))

    return operands.pop()


print(calculate_postfix("2 3 * 4 +"))
print(calculate_postfix("1 2 + 3 + 4 + 5 +"))
print(calculate_postfix("1 2 3 4 5 * + * +"))



