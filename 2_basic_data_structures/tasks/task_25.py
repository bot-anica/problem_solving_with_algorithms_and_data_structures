# 25. Продумайте и проведите эксперимент,
# сравнивающий производительности списков Python и списков,
# реализованных как связанные.
import time

from data_structures import UnorderedList, OrderedList


def add_items(list_inst: list | OrderedList | UnorderedList, quantity: int):
    if isinstance(list_inst, list):
        for i in range(quantity):
            list_inst.append(i)
    elif isinstance(list_inst, (OrderedList, UnorderedList)):
        for i in range(quantity):
            list_inst.add(i)


def pop_first_items(list_inst: list | OrderedList | UnorderedList, quantity: int):
    for j in range(quantity):
        list_inst.pop()


def pop_last_items(list_inst: list | OrderedList | UnorderedList, quantity: int):
    if isinstance(list_inst, list):
        for i in range(quantity):
            list_inst.pop(len(list_inst) - 1)
    elif isinstance(list_inst, (OrderedList, UnorderedList)):
        for i in range(quantity):
            list_inst.pop(list_inst.size() - 1)


# Удаляет первый элемент имеющий указанное значение (дубликаты не удаляет)
def remove_first_items(list_inst: list | OrderedList | UnorderedList, quantity: int):
    if isinstance(list_inst, list):
        for i in range(quantity):
            list_inst.remove(i)
    elif isinstance(list_inst, (OrderedList, UnorderedList)):
        for i in range(quantity):
            list_inst.remove_first(i)


def time_lists(list_type: str, method_name: str, quantity: int):
    different_type_lists = {
        "usual_list": [],
        "unordered_list": UnorderedList(),
        "ordered_list": OrderedList(),
    }

    start_time = 0

    def get_target_list(type_of_list: str):
        return different_type_lists[type_of_list]

    # Время начала замеряю только перед основным действием
    if method_name == "add":
        start_time = time.perf_counter()
        add_items(get_target_list(list_type), quantity)
    elif method_name == "pop_first":
        add_items(get_target_list(list_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        pop_first_items(get_target_list(list_type), quantity)
    elif method_name == "pop_last":
        add_items(get_target_list(list_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        pop_last_items(get_target_list(list_type), quantity)
    elif method_name == "remove_first":
        add_items(get_target_list(list_type), quantity)    # Добавил нужное количество элементов в список
        start_time = time.perf_counter()    # Только потом отметил время начала эксперимента
        remove_first_items(get_target_list(list_type), quantity)

    end_time = time.perf_counter()
    return end_time - start_time


def test_add_method(quantity: int):
    usual_list_execution_time = time_lists("usual_list", "add", quantity)
    unordered_list_execution_time = time_lists("unordered_list", "add", quantity)
    ordered_list_execution_time = time_lists("ordered_list", "add", quantity)

    print("Test add method")
    print(f"List time: {usual_list_execution_time}.")
    print(f"Unordered list time: {unordered_list_execution_time}.")
    print(f"Ordered list time: {ordered_list_execution_time}.\n")


def test_pop_first_item_method(quantity: int):
    usual_list_execution_time = time_lists("usual_list", "pop_first", quantity)
    unordered_list_execution_time = time_lists("unordered_list", "pop_first", quantity)
    ordered_list_execution_time = time_lists("ordered_list", "pop_first", quantity)

    print("Test pop first item method")
    print(f"List time: {usual_list_execution_time}.")
    print(f"Unordered list time: {unordered_list_execution_time}.")
    print(f"Ordered list time: {ordered_list_execution_time}.\n")


def test_pop_last_item_method(quantity: int):
    usual_list_execution_time = time_lists("usual_list", "pop_last", quantity)
    unordered_list_execution_time = time_lists("unordered_list", "pop_last", quantity)
    ordered_list_execution_time = time_lists("ordered_list", "pop_last", quantity)

    print("Test pop last item method")
    print(f"List time: {usual_list_execution_time}.")
    print(f"Unordered list time: {unordered_list_execution_time}.")
    print(f"Ordered list time: {ordered_list_execution_time}.\n")


def test_remove_first_item_method(quantity: int):
    usual_list_execution_time = time_lists("usual_list", "remove_first", quantity)
    unordered_list_execution_time = time_lists("unordered_list", "remove_first", quantity)
    ordered_list_execution_time = time_lists("ordered_list", "remove_first", quantity)

    print("Test remove first item method")
    print(f"List time: {usual_list_execution_time}.")
    print(f"Unordered list time: {unordered_list_execution_time}.")
    print(f"Ordered list time: {ordered_list_execution_time}.\n")


test_add_method(10000)   # List time: 0.003176604979671538. Unordered list time: 0.01150785107165575. Ordered list time: 0.015561912907287478.
test_pop_first_item_method(10000)    # List time: 0.0021358049707487226. Unordered list time: 0.004951526992954314. Ordered list time: 0.006614334066398442.
test_pop_last_item_method(10000) # List time: 0.0030267939437180758. Unordered list time: 5.932477131020278. Ordered list time: 5.680695086950436.
test_remove_first_item_method(10000)  # List time: 0.01357950794044882. Unordered list time: 5.9289752879412845. Ordered list time: 11.831360806943849.
