# 5. Реализуйте АТД Queue, используя список таким образом,
# чтобы хвост очереди совпадал с его концом.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)