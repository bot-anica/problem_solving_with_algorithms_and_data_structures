from data_structures import Stack
from utils import test_equal

# Предположим, что вместо объединения результатов рекурсивных вызовов toStr
# со строкой из convertString, мы изменим наш алгоритм таким образом,
# чтобы он складывал строки в стек перед тем, как сделать рекурсивный вызов.

def to_str(n, base):
    chars = "0123456789ABCDEF"
    result_stack = Stack()
    result = ''

    while n > 0:
        if n < base:
            result_stack.push(chars[n])
        else:
            result_stack.push(chars[n % base])

        n = n // base

    while not result_stack.is_empty():
        result += result_stack.pop()

    return result


test_equal(to_str(1453, 16), "5AD")
test_equal(to_str(10, 2), "1010")