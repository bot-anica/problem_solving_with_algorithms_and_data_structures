from stack import Stack


def par_checker(value):
    symbols = Stack()
    balanced = True
    index = 0

    while index < len(value) and balanced:
        symbol = value[index]

        if symbol == "(":
            symbols.push(symbol)
        else:
            if symbols.is_empty():
                balanced = False
            else:
                symbols.pop()

        index += 1

    return balanced and symbols.is_empty()


print(par_checker('((()))') == True)
print(par_checker('(()') == False)


def upgraded_par_checker(value):
    symbols = Stack()
    balanced = True
    index = 0

    while index < len(value) and balanced:
        symbol = value[index]

        if symbol in "({[":
            symbols.push(symbol)
        else:
            if symbols.is_empty():
                balanced = False
            elif matches(symbol, symbols.peek()):
                symbols.pop()

        index += 1

    return balanced and symbols.is_empty()


def matches(open_s, close_s):
    open_symbols = "({["
    close_symbols = ")}]"
    return close_symbols.find(close_s) == open_symbols.find(open_s)


print(upgraded_par_checker('{{([][])}()}') == True)
print(upgraded_par_checker('[{()]') == False)