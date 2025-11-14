# 20. Реализуйте оставшиеся операции, определённые в АТД OrderedList.
from data_structures import Node


# size, remove, index, pop

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        found = False
        previous = None
        current = self.head

        while not found and not current is None:
            if current.get_data() >= item:
                found = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(item)
        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        elif found:
            new_node.set_next(current)
            previous.set_next(new_node)
        else:
            previous.set_next(new_node)

    def remove(self, item):
        stop = False
        found = False
        previous = None
        current = self.head

        while not stop and not current is None:
            if current.get_data() == item:
                found = True

            if current.get_data() > item:
                stop = True

            if found:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                found = False
            else:
                previous = current

            current = current.get_next()

    def index(self, item):
        stop = False
        found = False
        current = self.head
        index = 0

        while not found and not stop and not current is None:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1

        if stop or not found:
            return -1
        else:
            return index

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
            target_item = current.get_data()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

        if index is None:
            target_item = current.get_data()
            previous.set_next(None)

        return target_item

    def size(self):
        current = self.head
        size = 0
        while not current is None:
            size += 1
            current = current.get_next()

        return size

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
print(ol.pop(5))
print(ol.pop())
print(ol.pop(0))
print(ol)
