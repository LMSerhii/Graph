import colorsys as cs
import random
import turtle


def figure():
    bob = turtle.Turtle()

    bob.speed(15)
    bob.up()
    bob.setposition(-30, -90)
    bob.down()

    def right_mnog(n, a=100):
        sum_angle = (n - 2) * 180
        if sum_angle % n == 0:
            angle = sum_angle // n
            for i in range(n):
                bob.forward(a)
                bob.left(180 - angle)

    for i in range(3, 11):
        right_mnog(i)

    turtle.done()


def ball():
    window = turtle.Screen()

    border = turtle.Turtle()
    border.speed(0)
    border.hideturtle()
    border.up()
    border.pensize(7)
    border.color('#800000')
    border.goto(300, 300)
    border.down()
    border.goto(300, -300)
    border.goto(-300, -300)
    border.goto(-300, 300)
    border.goto(300, 300)

    ball_ = turtle.Turtle()
    ball_.shape('circle')
    ball_.up()

    randx = random.randint(-290, 290)
    randy = random.randint(-290, 290)

    ball_.goto(randx, randy)

    dx = 3
    dy = 5
    while True:
        x, y = ball_.position()
        if x + dx > 300 or x + dx < -300:
            dx = -dx
        if y + dy >= 300 or y + dy <= -300:
            dy = -dy
        ball_.goto(x + dx, y + dy)

    window.mainloop()


def her():
    turtle.setup(800, 800)
    turtle.tracer(10)
    turtle.width(4)
    turtle.bgcolor('black')
    turtle.speed(15)

    def square(x):
        for i in range(3):
            turtle.forward(x)
            turtle.left(90)
        turtle.forward(x)

    for j in range(20):
        for i in range(10):
            turtle.color(cs.hsv_to_rgb(i / 10, 1 - j / 20, 1))
            turtle.right(135)
            square(200 - j * 4)
            turtle.right(135)
            turtle.circle(50, 36)
    turtle.hideturtle()
    turtle.done()


def main():
    # figure()
    # ball()
    her()


if __name__ == '__main__':
    main()
