# 8. Рассмотрите ситуацию из реальной жизни.
# Сформулируйте вопрос и создайте симуляцию, которая поможет на него ответить.
# Возможные ситуации:
#
#     Машины, стоящие в очереди в мойку.
#     Покупатели в очереди на кассе бакалейного магазина.
#     Самолёты, взлетающие и приземляющиеся на взлётно-посадочную полосу.
#     Кассир банка.
#
# Обязательно укажите сделанные вами предположения
# и предоставьте любые вероятностные данные,
# которые нужно будет рассмотреть в качестве части сценария.


# ------------------------------------------------------------------

# ? Я решил попробовать связать цепи Маркова, метод Монте-Карло
# ? и структуры данных Stack, Queue и Deque.

# ------------------------------------------------------------------

# Суть задачи: На основе данных о погоде за последние 365 дней
# определить вероятности погоды на каждый следующий день
# в зависимости от погоды в предыдущие 3 дня. Варианты погоды:
#     ясно (clear - C),
#     облачно (overcast - O),
#     дождь (rain - R).
#
# Вариантов погоды всего 3, потому что чем их будет больше,
# тем огромнее будет количество вариантов выборки в 3 дня,
# учитывая порядок возможных состояний.
# Т.е COR, OCR, ORC и т.д. это будут разные варианты.
# Кроме этого возможны варианты повторения состояний,
# например когда несколько дней подряд ясно или несколько дней подряд был дождь.
#
# В итоге у нас получается всего возможно 3^3 вариантов, т.е. 27
# и в зависимости от каждого из них нужно будет посчитать вероятность
# погоды в следующий день.
#
# Данные о погоде за последние 365 генерируются 1 раз,
# а варианты прогноза погоды на следующие 7 и 30 дней
# можно генерировать большое количество раз
# для определения вероятности погоды на эти дни.
#
# Пока что не придумал более практичной и интересной идеи.

import random
import timeit


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{",".join(self.items)}"


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def __str__(self):
        items_as_string = ",".join(self.items)
        return f"Queue({items_as_string})"

    def __iter__(self):
        return iter(self.items)


def get_data_if_it_exists():
    existed_data = ''

    try:
        with open("task_8_data.txt", "r") as file:
            existed_data = file.read()
    except FileNotFoundError:
        print("File does not exist")

    return existed_data.split(",") if existed_data else []


def write_year_data_to_file(data: list[str]):
    with open("task_8_data.txt", "w") as file:
        file.write(",".join(data))
    print("The data was saved to a file.")



def generate_year_data():
    available_weather = ("C", "O", "R")
    year_data = [available_weather[random.randint(0, 2)] for _ in range(365)]

    return year_data


def get_statistic_data(year_data: list[str]):
    statistic_data = {}

    pre_previous = year_data[0]
    previous = year_data[1]

    for i in range(2, len(year_data) - 1):
        current = year_data[i]
        three_days_weather = f"{pre_previous}{previous}{current}"

        next_day_weather = year_data[i + 1]

        if not three_days_weather in statistic_data:
            statistic_data[three_days_weather] = {}
            statistic_data[three_days_weather][next_day_weather] = 1
        elif next_day_weather in statistic_data[three_days_weather]:
            statistic_data[three_days_weather][next_day_weather] += 1
        else:
            statistic_data[three_days_weather][next_day_weather] = 1

        pre_previous = previous
        previous = current

    return statistic_data


def get_weather_for_next_day(statistic_data, previous_three_days_weather):
    if previous_three_days_weather in statistic_data:
        frequency_sum = 0
        sub_statistic = statistic_data[previous_three_days_weather]

        for key in sub_statistic:
            frequency_sum += sub_statistic[key]

        random_value = random.randint(1, frequency_sum)

        # Допустим у нас есть такие данные {'C': 3, 'R': 7, 'O': 5}
        # Тогда значение 'C' будет выбрано, если выпадет значение 1-3
        #       значение 'R' будет выбрано, если выпадет значение 4-10
        #       значение 'O' будет выбрано, если выпадет значение 11-15

        case_frequency = 0

        for key in sub_statistic:
            case_frequency += sub_statistic[key]
            if random_value <= case_frequency:
                return key
    else:
        available_weather = ("C", "O", "R")
        random_value = random.randint(0, 2)
        next_day_weather = available_weather[random_value]

        statistic_data[previous_three_days_weather] = {}
        statistic_data[previous_three_days_weather][next_day_weather] = 1

        return available_weather[random_value]


def get_weather_data_for_next_seven_days(statistic_data, weather_data):
    weather_data_for_next_seven_days = []

    last_three_days_weather = Queue()

    for i in range(3):
        last_three_days_weather.enqueue(weather_data[-3 + i])

    for i in range(7):
        # Возможно тип данных Queue тут вообще не нужен,
        # учитывая, что в итоге я все равно привожу Queue к типу ланных list
        #
        # Я все таки проверил вариант с использованием списка вместо Queue и,
        # как ожидалось, это увеличило скорость работы на 5-10%,
        # но решил оставить Queue для практики использования
        # этой структуры данных
        forecast_data = get_weather_for_next_day(statistic_data, "".join(list(last_three_days_weather)))
        last_three_days_weather.dequeue()
        last_three_days_weather.enqueue(forecast_data)
        weather_data_for_next_seven_days.append(forecast_data)

    return weather_data_for_next_seven_days

def forecast():
    data = get_data_if_it_exists()

    if not data:
        data = generate_year_data()
        write_year_data_to_file(data)

    statistic_data = get_statistic_data(data)

    weather_data_for_next_seven_days = get_weather_data_for_next_seven_days(statistic_data, data)

    return weather_data_for_next_seven_days


def test_forecast():
    setup_code = "from __main__ import forecast"
    execution_time = timeit.timeit("forecast()", setup=setup_code, number=10000)

    print(f"Execution time: {execution_time}. ")


def main():
    print(forecast())

    # hundred_attempts_forecast = []
    #
    # for i in range(100):
    #     hundred_attempts_forecast.append(forecast())
    #
    # forecast_days = len(hundred_attempts_forecast[0])
    # forecast_frequency = []
    # for i in range(forecast_days):
    #     forecast_frequency.append({})
    #     for j in range(100):
    #         if hundred_attempts_forecast[j][i] in forecast_frequency[-1]:
    #             forecast_frequency[-1][hundred_attempts_forecast[j][i]] += 1
    #         else:
    #             forecast_frequency[-1][hundred_attempts_forecast[j][i]] = 1

    # В итоге я получил ту же вероятность исходов,
    # к которой пришел на этапе получения статистики,
    # что просто подтверждает Теорию больших чисел

    # print(forecast_frequency)

    # Правильнее нверное было бы не использовать рандом
    # на этапе прогнозирования погоды на следующий день,
    # а просто брать вариант, у которого большая вероятность.

    # Также этот эксперимент очень упрощен,
    # беря во внимание только последние 3 дня
    # и имея всего 3 возможных варианта погоды.
    # Также исходные данные содержат информацию только о погоде в последний год,
    # чего тоже на самом деле очень мало для прогнозирования.


if __name__ == "__main__":
    # test_forecast()
    main()
