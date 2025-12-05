import turtle
import random


myTurtle = turtle.Turtle()
myScreen = turtle.Screen()

def draw_spiral(my_turtle: turtle.Turtle, line_len: int):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


# draw_spiral(myTurtle, 100)
# myScreen.exitonclick()


def draw_tree(my_turtle: turtle.Turtle, line_len: int):
    if line_len > 5:
        my_turtle.forward(line_len)
        my_turtle.right(20)
        draw_tree(my_turtle, line_len - 15)
        my_turtle.left(40)
        draw_tree(my_turtle, line_len - 15)
        my_turtle.right(20)
        my_turtle.backward(line_len)


# myTurtle.left(90)
# myTurtle.up()   # Оторвал карандаш от экрана
# myTurtle.backward(100)  # отвел карандаш немного вниз, чтобы рисунок получился примерно по центру экрана
# myTurtle.down() # Прислонил карандаш к экрана
# myTurtle.color("green")
#
# draw_tree(myTurtle, 75)
# myScreen.exitonclick()


# --------------------------------------------------------------
# Измените программу для рекурсивного дерева, используя одну из следующих идей:
#
#     Измените толщину ветвей, чтобы при уменьшении branchLen линии становились тоньше.
#     Измените цвет ветвей таким образом, чтобы самые корокие ветви окрашивались как листья.
#     Измените угол поворота черепахи, чтобы каждая ветвь поворачиваласьпроизвольным образом в некотором диапазоне. Например, выбирайте угол между 15-ю и 45-ю градусами. Поэкспрериментируйте в поисках лучшего вида.
#     Измените рекурсивную часть branchLen, чтобы каждый раз вычиталось произвольное значение из некоторого диапазона вместо некой постоянной величины.

def get_random_angle():
    return random.randint(15, 25)

def get_size_delta():
    return random.randint(5, 15)

def draw_random_tree(my_turtle: turtle.Turtle, line_len: int, line_width: int):
    myTurtle.pensize(line_width)
    myTurtle.down()
    angle = get_random_angle()

    if line_len <= 20:
        my_turtle.color("green")
    else:
        myTurtle.color("brown")

    if line_len > 5:
        my_turtle.forward(line_len)
        my_turtle.right(angle)
        draw_random_tree(my_turtle, line_len - get_size_delta(), line_width - 1)
        my_turtle.left(angle * 2)
        draw_random_tree(my_turtle, line_len - get_size_delta(), line_width - 1)
        my_turtle.right(angle)
        my_turtle.up()
        my_turtle.backward(line_len)


myTurtle.left(90)
myTurtle.up()   # Оторвал карандаш от экрана
myTurtle.backward(100)  # отвел карандаш немного вниз, чтобы рисунок получился примерно по центру экрана

draw_random_tree(myTurtle, 75, 10)
myScreen.exitonclick()