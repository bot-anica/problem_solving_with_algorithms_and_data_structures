from node import Node

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
        # If Unordered List has not self.rear variable
        # last_found = False
        # current = self.head
        # while not last_found and not (current is None):
        #     if current.get_next() is None:
        #         last_found = True
        #     else:
        #         current = current.get_next()
        #
        # new_node = Node(item)
        # if self.head is None:
        #     self.head = new_node
        # else:
        #     current.set_next(new_node)
        new_node = Node(item)
        if self.rear is None:
            self.rear =new_node
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

        if found:
            return current_index
        else:
            return None

    def pop(self, index):
        found = False
        current_index = 0
        previous = None
        current = self.head
        while not found and not (current is None):
            if current_index == index:
                found = True
            elif not (current.get_next() is None):
                previous = current
                current = current.get_next()
                current_index += 1

        if not (self.head is None) and previous is None:
            self.head = current.get_next()
        elif index is None:
            previous.set_next(None)
        elif found:
            previous.set_next(current.get_next())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

