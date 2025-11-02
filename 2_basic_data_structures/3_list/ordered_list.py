from node import Node

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


o = OrderedList()

print(o.is_empty() == True)
print(o.size() == 0)
o.add(17)
o.add(9)
o.add(77)
o.add(40)
o.add(83)
print(o.is_empty() == False)
print(o.size() == 5)
print(o.search(17) == True)
print(o.search(50) == False)
o.remove(50)
o.remove(17)
print(o.size() == 4)
print(o.index(40) == 1)
print(o.index(83) == 3)
print(o.index(17) == -1)
print(o.pop() == 83)
print(o.pop(1) == 40)
