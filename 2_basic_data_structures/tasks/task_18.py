# 18. Реализуйте оставшиеся операции,
# определённые в АТД UnorderedList (append, index, pop, insert).

from data_structures import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def append(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.rear = new_node
            self.head = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

    def index(self, item):
        found = False
        index = 0
        current = self.head

        while not found and not current is None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1

        if found:
            return index
        else:
            return -1

    def pop(self, index = None):
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

        if found or index is None:
            previous.set_next(current.get_next())
            return current.get_data()
        else:
            return None

    def insert(self, item, index):
        found = False
        previous = None
        current = self.head
        current_index = 0

        while not found and not current is None:
            if current_index == index:
                found = True
            else:
                previous = current
                current = current.get_next()
                current_index += 1

        new_node = Node(item)
        if found:
            if current_index == 0:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                new_node.set_next(current)
                previous.set_next(new_node)
        else:
            previous.set_next(new_node)

    def __str__(self):
        items_list = []

        current = self.head

        while not current is None:
            items_list.append(str(current.get_data()))
            current = current.get_next()

        return f"[{", ".join(items_list)}]"


ul = UnorderedList()
ul.append(1)
ul.append(2)
ul.append(3)
ul.append(4)
print(ul)
print(ul.index(4))
print(ul.pop(2))
print(ul)
print(ul.pop())
print(ul)
ul.insert(5, 1)
ul.insert(7, 7)
print(ul)
