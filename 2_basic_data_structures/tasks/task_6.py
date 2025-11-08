# 6. Продумайте и воплотите эксперимент по тестовому сравнению
# двух реализаций очереди. Какие выводы вы можете из него сделать?

import timeit

class Queue1:
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


class Queue2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


queue_1 = Queue1()
queue_2 = Queue2()


def test_queue_1():
    setup_code = "from __main__ import queue_1"
    enqueue_execution_time = timeit.timeit("queue_1.enqueue('-')", setup=setup_code, number=100000)
    dequeue_execution_time = timeit.timeit("queue_1.dequeue()", setup=setup_code, number=100000)

    print(f"Enqueue time: {enqueue_execution_time}. Dequeue time: {dequeue_execution_time}. ")


def test_queue_2():
    setup_code = "from __main__ import queue_2"
    enqueue_execution_time = timeit.timeit("queue_2.enqueue('-')", setup=setup_code, number=100000)
    dequeue_execution_time = timeit.timeit("queue_2.dequeue()", setup=setup_code, number=100000)

    print(f"Enqueue time: {enqueue_execution_time}. Dequeue time: {dequeue_execution_time}. ")


test_queue_1()
test_queue_2()


# Depending on the implementation of the queue class,
# the enqueue and dequeue methods will have complexity
# O(1) and O(n) or O(n) and O(1)
