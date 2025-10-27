from stack import Stack


def divide_by_2(dec_number):
    stack = Stack()

    while dec_number > 0:
        last = dec_number % 2
        stack.push(last)
        dec_number = dec_number // 2

    result = ''

    while not stack.is_empty():
        result += str(stack.pop())

    return result


print(divide_by_2(42) == '101010')


def base_converter(dec_number, base):
    numbers = '0123456789ABCDEF'
    stack = Stack()

    while dec_number > 0:
        last = dec_number % base
        stack.push(last)
        dec_number = dec_number // base

    result = ''

    while not stack.is_empty():
        result += str(numbers[stack.pop()])

    return result


print(base_converter(26,26) == '10')
print(base_converter(256,16) == '100')