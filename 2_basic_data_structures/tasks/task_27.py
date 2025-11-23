# 27. Данная выше реализация связанного списка
# называется единичным связанным списком,
# поскольку каждый его узел содержит единственную ссылку
# на следующий в последовательности.
# Альтернативная реализация известна как двойной связанный список.
# В ней нужный узел ссылается на следующий за ним (next)
# и на предыдущий ему (back).
# Голова также имеет две ссылки: одну на первый узел в связанном списке,
# а вторую - на последний. Закодируйте эту реализацию в Python.

class DoubleLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node


class DoubleLinkedUnorderList:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.list_size

    def add(self, item):
        new_node = DoubleLinkedNode(item)

        if not self.head is None:
            last_node = self.head.get_prev()
            new_node.set_prev(last_node if not last_node is None else self.head)    # add link to last node
            self.head.set_prev(new_node)
            new_node.set_next(self.head)

        self.head = new_node
        self.list_size += 1

    def append(self, item):
        new_node = DoubleLinkedNode(item)

        if self.head is None:
            self.head = new_node
        else:
            current_last_node = self.head.get_prev()
            if current_last_node is None:
                self.head.set_next(new_node)
            else:
                current_last_node.set_next(new_node)
            new_node.set_prev(current_last_node)
            self.head.set_prev(new_node)

        self.list_size += 1

    def insert(self, item, index):
        new_node = DoubleLinkedNode(item)
        current = self.head
        current_index = 0

        while current_index < index and not current is None:
            current = current.get_next()
            current_index += 1

        if current_index == index:
            prev_node = current.get_prev()
            new_node.set_prev(prev_node)

            if index != 0:
                prev_node.set_next(new_node)
            else:
                self.head = new_node

            new_node.set_next(current)
            current.set_prev(new_node)
        elif current is None:
            self.head = new_node
        else:
            current_last_node = self.head.get_prev()
            current_last_node.set_next(new_node)
            new_node.set_prev(current_last_node)
            self.head.set_prev(new_node)

        self.list_size += 1

    def search(self, item):
        current = self.head
        current_index = 0
        found = False

        while not found and not current is None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                current_index += 1

        return found

    def index(self, item):
        current = self.head
        current_index = 0
        found = False

        while not found and not current is None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                current_index += 1

        return current_index if found else -1

    def remove(self, item):
        current = self.head
        current_index = 0
        found = False

        while not found and not current is None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                current_index += 1

        if found:
            previous_node = current.get_prev()
            next_node = current.get_next()
            self.list_size -= 1

            if previous_node is None:
                self.head = None
            elif next_node is None:
                previous_node.set_next(None)
            else:
                previous_node.set_next(next_node)
                next_node.set_prev(previous_node)

    def pop(self, index=None):
        if self.head is None:
            return None
        elif index is None:
            index = 0

        found = False
        current = self.head
        current_index = 0

        while not found and not current is None:
            if current_index == index:
                found = True
            else:
                current = current.get_next()
                current_index += 1

        if not found:
            return None

        target_item = current.get_data()
        previous_node = current.get_prev()
        next_node = current.get_next()
        self.list_size -= 1

        if next_node is None:
            previous_node.set_next(None)
        else:
            previous_node.set_next(next_node)
            next_node.set_prev(previous_node)

        return target_item

    def __str__(self):
        items_list = []

        current = self.head

        while not current is None:
            items_list.append(str(current.get_data()))
            current = current.get_next()

        return f"[{", ".join(items_list)}]"


dl_ul = DoubleLinkedUnorderList()

print(dl_ul.size())
print(dl_ul.is_empty())

dl_ul.add(2)
dl_ul.add(4)
dl_ul.add(5)

dl_ul.insert(3, 2)
dl_ul.insert(6, 0)

dl_ul.append(1)

print(dl_ul)

print(dl_ul.size())
print(dl_ul.search(1))
print(dl_ul.search(7))

dl_ul.add(7)
print(dl_ul)
print(dl_ul.search(7))
print(dl_ul.index(7))
print(dl_ul.size())

dl_ul.remove(5)
print(dl_ul.size())
dl_ul.remove(6)
print(dl_ul.size())
dl_ul.remove(4)
print(dl_ul.size())
print(dl_ul.search(5))

print(dl_ul)
print(dl_ul.pop(5))
print(dl_ul.pop(1))
print(dl_ul.pop())
