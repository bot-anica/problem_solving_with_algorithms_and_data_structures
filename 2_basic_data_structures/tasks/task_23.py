# 23. Реализуйте очередь, используя связанный список.
from data_structures import UnorderedList


class Queue:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop(self.items.size() - 1)

    def __str__(self):
        return self.items.__str__()
    
    
q = Queue()
print(q.is_empty())
print(q.size())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q)
