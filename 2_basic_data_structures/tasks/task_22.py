# 22. Реализуйте стек, используя связанный список.
from data_structures import UnorderedList


class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()

    def push(self, item):
        self.items.add(item)

    def peek(self):
        # Я переписал метод .pop() у класса UnorderedList,
        # чтобы он имел сложность O(1), вместо O(n),
        # при вызове без указания индекса.
        # Теперь, в таком случае, он удаляет последний добавленный элемент,
        # а не тот, который находиться в конце.
        last_added_item = self.items.pop()

        if not last_added_item is None:
            self.items.add(last_added_item)

        return last_added_item

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return self.items.__str__()


s = Stack()
print(s.is_empty())
print(s.size())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
print(s.pop())
print(s.pop())
print(s)
print(s.peek())