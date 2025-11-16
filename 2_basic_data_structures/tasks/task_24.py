# 24. Реализуйте дек, используя связанный список.
from data_structures import UnorderedList


class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()

    def add_front(self, item):
        self.items.add(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(self.items.size() - 1)

    def __str__(self):
        return self.items.__str__()


d = Deque()
print(d.is_empty())
print(d.size())
d.add_front(2)
d.add_front(3)
d.add_front(4)
d.add_front(5)
print(d)
d.add_rear(1)
print(d)
print(d.remove_front())
print(d)
print(d.remove_rear())
print(d)
