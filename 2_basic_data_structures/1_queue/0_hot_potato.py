from queue import Queue

def hot_potato(namelist, num):
    players_queue = Queue()

    for name in namelist:
        players_queue.enqueue(name)

    while players_queue.size() > 1:
        for i in range(num):
            players_queue.enqueue(players_queue.dequeue())

        players_queue.dequeue()

    return players_queue.dequeue()


print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))