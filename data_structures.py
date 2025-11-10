class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{",".join(self.items)}"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        items_as_string = ",".join(self.items)
        return f"Queue({items_as_string})"

    def __iter__(self):
        return iter(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        stop = False
        previous = None
        current = self.head

        while not stop and not (current is None):
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(item)
        new_node.set_next(self.head)

        if self.head is None:
            self.head = new_node
        else:
            if previous is None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                new_node.set_next(current)
                previous.set_next(new_node)

    def size(self):
        count = 0
        current = self.head
        while not current is None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        stop = False
        found = False
        current = self.head
        while not (current is None) and not found and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        stop = False
        found = False
        previous = None
        current = self.head
        while not found and not (current is None) and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def index(self, item):
        stop = False
        found = False
        current_index = 0
        current = self.head
        while not found and not (current is None) and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
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
        if not (self.head is None) and previous is None:
            self.head = current.get_next()
        elif index is None:
            previous.set_next(None)
        elif found:
            previous.set_next(current.get_next())

        return target_item


class UnorderedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)

        if self.rear is None:
            self.rear = new_node

        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while not current is None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        found = False
        current = self.head
        while not (current is None) and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

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
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def append(self, item):
        new_node = Node(item)
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

    def pop(self, index=None):
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
        if not (self.head is None) and previous is None:
            self.head = current.get_next()
        elif index is None:
            previous.set_next(None)
        elif found:
            previous.set_next(current.get_next())

        return target_item

