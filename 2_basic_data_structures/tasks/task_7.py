# 7. Существует возможность реализовать очередь таким образом,
# чтобы обе операции enqueue и dequeue в среднем имели производительность O(1).
# Это подразумевает, что большую часть времени они будут O(1),
# за исключением единственного случая, при котором dequeue будет O(n).

import timeit


class OptimizedQueue:
    def __init__(self):
        self.items = []
        self.begin_index = 0

    def is_empty(self):
        return self.items == [] or len(self.items) - self.begin_index == 0

    def size(self):
        return len(self.items) - self.begin_index

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        dequeued_item = self.items[self.begin_index]
        self.items[self.begin_index] = None
        self.begin_index += 1

        return dequeued_item

    def __str__(self):
        existed_items = self.items[self.begin_index:]
        items_as_string = ",".join(existed_items)
        return f"Queue({items_as_string})"


queue = OptimizedQueue()


def test_queue():
    setup_code = "from __main__ import queue"
    enqueue_execution_time = timeit.timeit("queue.enqueue('-')", setup=setup_code, number=10000000)
    dequeue_execution_time = timeit.timeit("queue.dequeue()", setup=setup_code, number=10000000)

    print(f"Enqueue time: {enqueue_execution_time}. Dequeue time: {dequeue_execution_time}. ")


test_queue()