# 14. Реализуйте метод remove, который работал бы корректно,
# если элемент отсутствует в списке.

from data_structures import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.rear = None
        self.list_size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)

        if self.rear is None:
            self.rear = new_node

        self.head = new_node
        self.list_size += 1

    def size(self):
        return self.list_size

    def search(self, item):
        found = False
        current = self.head
        while not (current is None) and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    # Я изначально реализовал его с учетом такого случая
    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while not found and not (current is None):
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            self.list_size -= 1
            next_item = current.get_next()
            if previous is None:
                self.head = next_item
            else:
                previous.set_next(next_item)

    def append(self, item):
        new_node = Node(item)
        self.list_size += 1
        if self.rear is None:
            self.rear = new_node
            self.head = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

    def insert(self, item, index):
        current_index = 0
        previous = None
        current = self.head
        while current_index < index and not (current is None):
            previous = current
            current = current.get_next()
            current_index += 1

        new_node = Node(item)
        self.list_size += 1
        if self.head is None:
            self.head = new_node
        elif current is None:
            previous.set_next(new_node)
        else:
            new_node.set_next(current)
            previous.set_next(new_node)

    def index(self, item):
        found = False
        current_index = 0
        current = self.head
        while not found and not (current is None):
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                current_index += 1

        if found:
            return current_index
        else:
            return -1

    def pop(self, index = None):
        found = False
        current_index = 0
        previous = None
        current = self.head
        while not found and not (current is None):
            if current_index == index:
                found = True
            else:
                previous = current
                current = current.get_next()
                current_index += 1

        target_item = current.get_data() if current else previous.get_data() if previous else None
        if target_item:
            self.list_size -= 1
            if not (self.head is None) and previous is None:
                self.head = current.get_next()
            elif index is None:
                previous.set_next(None)
            elif found:
                previous.set_next(current.get_next())

        return target_item
