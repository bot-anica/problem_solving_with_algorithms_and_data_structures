# 15. Измените классы списков, разрешив наличие дубликатов.
# Какие методы затронет это изменение?

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

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        # Не останавливаю поиск даже если нашел элемент,
        # потому что могут быть дубликаты
        while not (current is None):
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            # Если нашел элемент, то удаляю его,
            # меняю значение флага found обратно на False и продолжаю поиск
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
            # Теперь проверяем вариант >=, чтобы учесть случай дубликата
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
        # Не останавливаю поиск даже если нашел элемент,
        # потому что могут быть дубликаты
        while not (current is None) and not stop:
            if current.get_data() > item:
                stop = True
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            # Если нашел элемент, то удаляю его,
            # меняю значение флага found обратно на False и продолжаю поиск
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


# Вывод: У класса UnorderedList поменялся только метод remove,
# добавив возможность удалять сразу несколько элементов с одинаковыми значениями.
# А у класса OrderedList, кроме метода remove, также поменялся метод add,
# добавив возможность добавлять дубликаты