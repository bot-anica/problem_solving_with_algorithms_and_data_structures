from queue import Queue
import random


class Task:
    def __init__(self, time, max_pages_per_file):
        self.timestamp = time
        self.pages_number = random.randrange(1, max_pages_per_file + 1)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages_number

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Printer:
    def __init__(self, ppr: int):
        self.pages_per_minute = ppr
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task: Task):
        if self.current_task is None:
            self.current_task = new_task
            self.time_remaining = new_task.get_pages() * 60 / self.pages_per_minute


def new_print_task(total_time_in_sec: int, tasks_quantity: int):
    average_time_between_tasks: int = round(total_time_in_sec / tasks_quantity)
    num = random.randrange(1, average_time_between_tasks + 1)
    return num == average_time_between_tasks


def simulation(num_seconds: int, pages_per_minute: int, students_quantity: int, files_per_student: int, max_pages_per_file: int):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(num_seconds, students_quantity * files_per_student):
            new_task = Task(current_second, max_pages_per_file)
            print_queue.enqueue(new_task)

        if (not printer.busy()) and (not print_queue.is_empty()):
            next_task: Task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times)/len(waiting_times) if len(waiting_times) else 0
    print(f"Average Wait {round(average_wait, 2)} sec. {print_queue.size()} tasks remaining.")


for i in range(10):
    simulation(3600, 10, 10, 3, 20)

