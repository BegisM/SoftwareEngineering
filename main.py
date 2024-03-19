import turtle

t = turtle.Pen()


def mv(t: turtle, x: int, y: int) -> None:
    t.pu()
    t.setpos(x, y)
    t.pd()


def square(t, clr, size):
    t.color(clr)
    t.pencolor('black')
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()


def box(t: turtle, size: int, side: int, x: int, y: int) -> None:
    check = 0 if side % 2 == 0 else 1
    k = 255 / (side // 2 + check)
    for i in range(side):
        for j in range(side):
            if j < (side // 2 + check):
                square(t, ((255 - j * k) / 255, (255 - i * k) / 255, 0), size) \
                    if i < (side // 2 + check) \
                    else square(t,((255 - j * k) / 255, (255 - ((side // 2) + check - (1 + check) - (i % ((side // 2 + check)))) * k) / 255, 0), size)
            else:
                square(t, ((255 - ((side // 2) + check - (1 + check) - (j % (side // 2 + check))) * k) / 255, (255 - i * k) / 255, 0), size) \
                    if i < (side // 2 + check) \
                    else square(t, ((255 - ((side // 2) + check - (1 + check) - (j % (side // 2 + check))) * k) / 255, (255 - ((side // 2 + check) - (1 + check) - (i % (side // 2 + check))) * k) / 255, 0), size)
            t.fd(size)
        mv(t, x, y + (-1) * size * (i + 1))




def main(t: turtle, size: int, side: int) -> None:
    mv(t, -1 * (side // 2) * size, (side // 2) * size)
    box(t, size, side,  -1 * (side // 2) * size,  (side // 2) * size)
    turtle.mainloop()


if __name__ == '__main__':
    t = turtle.Pen()
    t.speed(0)
    main(t, 20, 10)