# 9. Измените симуляцию “Hot Potato”,
# чтобы можно было случайным образом выбирать значение для отсчёта.
# Таким образом, результат каждого прохода станет непредсказуемым.
import random

from data_structures import Queue


# Генерируется случайное число,
# игроки передают это количество раз мячик,
# а тот на ком остановился мяч - выбывает.
# Затем снова генерируется новое число и игра повторяется,
# пока не останется 1 игрок.
def hot_potato(namelist):
    players_queue = Queue()

    for name in namelist:
        players_queue.enqueue(name)

    while players_queue.size() > 1:
        # Я ограничил максимальное рандомное число,
        # чтобы не делать лишние итерации, лишние круги
        step_quantity = random.randint(1, players_queue.size())

        for i in range(step_quantity):
            players_queue.enqueue(players_queue.dequeue())

        players_queue.dequeue()

    return players_queue.dequeue()


print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"]))