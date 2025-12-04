import turtle

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


myTurtle.left(90)
myTurtle.up()   # Оторвал карандаш от экрана
myTurtle.backward(100)  # отвел карандаш немного вниз, чтобы рисунок получился примерно по центру экрана
myTurtle.down() # Прислонил карандаш к экрана
myTurtle.color("green")

draw_tree(myTurtle, 75)
myScreen.exitonclick()