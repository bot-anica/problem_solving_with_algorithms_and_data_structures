from stack import Stack


def reverse_string(mystr):
    new_stack = Stack()
    result = ''

    for i in range(len(mystr)):
        new_stack.push(mystr[i])

    for i in range(new_stack.size()):
        result += new_stack.pop()

    return result


print(reverse_string('apple') == 'elppa')
print(reverse_string('x') == 'x')
print(reverse_string('1234567890') == '0987654321')