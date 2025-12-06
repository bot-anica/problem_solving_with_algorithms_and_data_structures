import turtle
import random


def get_mid(point_1: list[int], point_2: list[int]):
    x = (point_1[0] + point_2[0]) / 2
    y = (point_1[1] + point_2[1]) / 2
    return [x, y]


def draw_triangle(my_turtle: turtle.Turtle, points: list[list[int]], color: str):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def draw_sierpinski(my_turtle: turtle.Turtle, points: list[list[int]], degree):
    colors = ['red', 'orange', 'green', 'blue', 'purple']

    draw_triangle(my_turtle, points, colors[degree % len(colors)])

    if degree > 0:
        draw_sierpinski(my_turtle, [get_mid(points[0], points[1]), points[1], get_mid(points[1], points[2])], degree - 1)
        draw_sierpinski(my_turtle, [points[0], get_mid(points[0], points[1]), get_mid(points[2], points[0])], degree - 1)
        draw_sierpinski(my_turtle, [get_mid(points[0], points[2]), get_mid(points[1], points[2]), points[2]], degree - 1)


def get_random_point_coordinate(max_abs_coord: int):
    x = random.randint(-max_abs_coord, max_abs_coord)
    y = random.randint(-max_abs_coord, max_abs_coord)
    return [x, y]


def main():
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()
    points = [get_random_point_coordinate(400) for _ in range(3)]

    draw_sierpinski(myTurtle, points, 5)

    myScreen.exitonclick()


if __name__ == '__main__':
    main()
