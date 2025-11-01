from deque import Deque


def palindrome_checker(word):
    deque = Deque()
    is_palindrome = True

    for i in range(len(word)):
        deque.add_front(word[i])

    while deque.size() > 1 and is_palindrome:
        if not deque.remove_front() == deque.remove_rear():
            is_palindrome = False

    return is_palindrome


print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))