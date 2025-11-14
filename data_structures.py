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
        items_list_as_str = '['

        for i in range(len(self.items)):
            if i != 0:
                items_list_as_str += ", "
            items_list_as_str += str(self.items[i])
        else:
            items_list_as_str += ']'

        return items_list_as_str


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
        items_list_as_str = '['

        for i in range(len(self.items)):
            if i != 0:
                items_list_as_str += ", "
            items_list_as_str += str(self.items[i])
        else:
            items_list_as_str += ']'

        return items_list_as_str

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

    def __str__(self):
        items_list_as_str = '['

        for i in range(len(self.items)):
            if i != 0:
                items_list_as_str += ", "
            items_list_as_str += str(self.items[i])
        else:
            items_list_as_str += ']'

        return items_list_as_str


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
        self.list_size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        stop = False
        previous = None
        current = self.head

        while not stop and not (current is None):
            if current.get_data() >= item:
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

        self.list_size += 1

    def size(self):
        return self.list_size

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
        while not (current is None) and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if found:
                self.list_size -= 1
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                current = current.get_next()
                found = False

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

    def pop(self, index=None):
        found = False
        previous = None
        current = self.head
        current_index = 0

        while not found and not current.get_next() is None:
            if current_index == index:
                found = True
            else:
                if not current.get_next() is None:
                    previous = current
                    current = current.get_next()
                    current_index += 1

        target_item = None

        if found:
            self.list_size -= 1
            target_item = current.get_data()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

        if index is None:
            if self.list_size > 0:
                self.list_size -= 1
                target_item = current.get_data()
                previous.set_next(None)

        return target_item

    def __str__(self):
        items_list = []

        current = self.head

        while not current is None:
            items_list.append(str(current.get_data()))
            current = current.get_next()

        return f"[{", ".join(items_list)}]"


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

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while not (current is None):
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if found:
                self.list_size -= 1
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                current = current.get_next()
                found = False

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

    def __str__(self):
        items_list = []

        current = self.head

        while not current is None:
            items_list.append(str(current.get_data()))
            current = current.get_next()

        return f"[{", ".join(items_list)}]"


ol = OrderedList()
ol.add(3)
ol.add(4)
ol.add(1)
ol.add(2)
ol.add(3)
ol.add(4)
print(ol)
print(ol.size())
ol.remove(3)
ol.remove(5)
print(ol)
print(ol.index(2))
print(ol.index(5))
print(ol.size())
print(ol.pop(5))
print(ol.pop())
print(ol.pop(0))
print(ol)
print(ol.size())