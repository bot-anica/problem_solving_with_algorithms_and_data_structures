import random


def generate_random_char():
    letters = 'abcdefghijklmnopqrstuvwxyz '
    index = random.randint(0, len(letters) - 1)
    return letters[index]


def update_phrase(target, phrase):
    updated_phrase = ''

    for i in range(len(target)):
        if phrase[i] != target[i]:
            new_char = generate_random_char()

            if new_char == target[i]:
                updated_phrase += new_char
            else:
                updated_phrase += phrase[i]
        else:
            updated_phrase += phrase[i]

    return updated_phrase


def compare_phrase_with_target(phrase, target = ''):
    right_chars_quantity = 0

    for i in range(len(phrase)):
        if phrase[i] == target[i]:
            right_chars_quantity += 1

    return right_chars_quantity / len(phrase)


def main():
    target = 'methinks it is like a weasel'

    iteration_number = 0
    best_comparing_result = 0
    best_phrase = ['-'] * len(target)

    while True:
        iteration_number += 1

        updated_phrase = update_phrase(target, best_phrase)

        if best_phrase != updated_phrase:
            best_phrase = updated_phrase

        comparing_result = compare_phrase_with_target(best_phrase, target)

        if comparing_result > best_comparing_result:
            best_comparing_result = comparing_result
            print(f"{best_phrase} - {round(best_comparing_result * 100)}")

        if comparing_result == 1:
            break

    print(iteration_number)
    print(best_phrase)


main()