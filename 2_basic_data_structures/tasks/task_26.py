# 26. Продумайте и проведите эксперимент,
# сравнивающий производительность стека и очереди, основанных на списках Python,
# с реализациями на основе связанного списка.
import time

from data_structures import UnorderedList, Stack, Queue


class LinkedListStack:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def size(self):
        return self.items.size()

    def push(self, item):
        self.items.add(item)

    def peek(self):
        last_added_item = self.items.pop()

        if not last_added_item is None:
            self.items.add(last_added_item)

        return last_added_item

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return self.items.__str__()


class LinkedListQueue:
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


def stack_push_items(stack_inst: Stack | LinkedListStack, quantity: int):
    for i in range(quantity):
        stack_inst.push(i)


def stack_peek_items(stack_inst: Stack | LinkedListStack, quantity: int):
    for i in range(quantity):
        stack_inst.peek()


def stack_pop_items(stack_inst: Stack | LinkedListStack, quantity: int):
    for i in range(quantity):
        stack_inst.pop()


def queue_enqueue_items(queue_inst: Queue | LinkedListQueue, quantity: int):
    for i in range(quantity):
        queue_inst.enqueue(i)


def queue_dequeue_items(queue_inst: Queue | LinkedListQueue, quantity: int):
    for i in range(quantity):
        queue_inst.dequeue()


def time_stack(stack_type: str, method_name: str, quantity: int):
    different_type_stacks = {
        "usual_list_stack": Stack(),
        "linked_list_stack": LinkedListStack(),
    }

    start_time = 0

    def get_target_stack(type_of_stack: str):
        return different_type_stacks[type_of_stack]

    # Время начала замеряю только перед основным действием
    if method_name == "push":
        start_time = time.perf_counter()
        stack_push_items(get_target_stack(stack_type), quantity)
    elif method_name == "peek":
        stack_push_items(get_target_stack(stack_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        stack_peek_items(get_target_stack(stack_type), quantity)
    elif method_name == "pop":
        stack_push_items(get_target_stack(stack_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        stack_pop_items(get_target_stack(stack_type), quantity)

    end_time = time.perf_counter()
    return end_time - start_time


def time_queue(queue_type: str, method_name: str, quantity: int):
    different_type_queues = {
        "usual_list_queue": Queue(),
        "linked_list_queue": LinkedListQueue(),
    }

    start_time = 0

    def get_target_queue(type_of_queue: str):
        return different_type_queues[type_of_queue]

    # Время начала замеряю только перед основным действием
    if method_name == "enqueue":
        start_time = time.perf_counter()
        queue_enqueue_items(get_target_queue(queue_type), quantity)
    elif method_name == "dequeue":
        queue_enqueue_items(get_target_queue(queue_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        queue_dequeue_items(get_target_queue(queue_type), quantity)

    end_time = time.perf_counter()
    return end_time - start_time


def test_stack_method(method: str, quantity: int):
    usual_list_stack_execution_time = time_stack("usual_list_stack", method, quantity)
    linked_list_stack_execution_time = time_stack("linked_list_stack", method, quantity)

    print(f"Test {method} stack method")
    print(f"Usual list stack time: {usual_list_stack_execution_time}.")
    print(f"Linked list stack time: {linked_list_stack_execution_time}.\n")


def test_queue_method(method: str, quantity: int):
    usual_list_queue_execution_time = time_queue("usual_list_queue", method, quantity)
    linked_list_queue_execution_time = time_queue("linked_list_queue", method, quantity)

    print(f"Test {method} queue method")
    print(f"Usual list queue time: {usual_list_queue_execution_time}.")
    print(f"Linked list queue time: {linked_list_queue_execution_time}.\n")


test_stack_method("push", 10000)
test_stack_method("peek", 10000)
test_stack_method("pop", 10000)

test_queue_method("enqueue", 10000)
test_queue_method("dequeue", 10000)
