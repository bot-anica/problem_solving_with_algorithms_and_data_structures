# 21. Рассмотрите отношения между упорядоченными и неупорядоченными списками.
# Возможно ли использовать наследование для создания
# более эффективной реализации? Воплотите эту наследственную иерархию.

# ------------------------------------------------------------------

# У этих классов отличаются методы add, search, remove, append, insert и index.
# Основные причины: использование свойства rear у неупорядоченного списка,
# что упрощает работу с ним, а также использование условий упорядочивания
# у упорядоченного списка

# Как вариант можео создать класс, который будет предком этих двух видов списков

# ------------------------------------------------------------------

from abc import ABC, abstractmethod
from enum import Enum

from data_structures import Node


# Далее создал абстрактный класс,
# чтобы нельзя было создавать его экземпляры напрямую,
# а также чтобы добавить обязательный абстрактный метов add,
# который нужно будет обязательно реализовать в классах наследниках
class List(ABC):
    def __init__(self, order=None):
        self.head = None
        self.order = order
        self.list_size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.list_size

    # Я решил создать отдельную функцию,
    # которая будет использоваться для сравнения двух элементов при необходимости
    def compare_items(self, a, b):
        if self.order == "ascent":
            return a > b
        elif self.order == "descent":
            return a < b
        else:
            return False

    # Метод, который имеет разную реализацию в разных типах списков,
    # но он является обязательным
    @abstractmethod
    def add(self, item):
        pass

    def search(self, item):
        stop = False
        found = False
        current = self.head
        while not (current is None) and not found and not stop:
            if not self.order is None and self.compare_items(item, current.get_data()):
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove_first(self, item):
        stop = False
        found = False
        previous = None
        current = self.head
        while not found and not current is None and not stop:
            if not self.order is None and self.compare_items(item, current.get_data()):
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

    def remove_all(self, item):
        stop = False
        found = False
        previous = None
        current = self.head
        while not (current is None) and not stop:
            if not self.order is None and self.compare_items(item, current.get_data()):
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
            if not self.order is None and self.compare_items(item, current.get_data()):
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

        while (not index is None) and (not found) and (not current is None):
            if current_index == index:
                found = True
            else:
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
                target_item = self.head.get_data()
                self.head = current.get_next()

        return target_item

    def __str__(self):
        items_list = []

        current = self.head

        while not current is None:
            items_list.append(str(current.get_data()))
            current = current.get_next()

        return f"[{", ".join(items_list)}]"


class OrderedList(List):
    def __init__(self, order="ascent"):
        super().__init__(order)

    def add(self, item):
        stop = False
        previous = None
        current = self.head

        while not stop and not (current is None):
            if self.compare_items(item, current.get_data()):
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


class UnorderedList(List):
    def __init__(self):
        super().__init__(order=None)
        self.rear = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)

        if self.rear is None:
            self.rear = new_node

        self.head = new_node
        self.list_size += 1

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



ol_1 = OrderedList()

ol_1.add(1)
ol_1.add(2)
ol_1.add(3)
ol_1.add(4)
ol_1.add(5)
print(ol_1)

ol_2 = OrderedList("descent")

ol_2.add("aaa")
ol_2.add("baa")
ol_2.add("bbb")
ol_2.add("aab")
ol_2.add("aba")
print(ol_2)

ul = UnorderedList()
ul.add(1)
ul.add(2)
ul.add(3)
ul.add(4)
ul.add(5)
print(ul)