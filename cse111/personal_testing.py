import turtle

def main():
    turtle.setup(800,800)

    fred = turtle.Turtle()
    fred.speed(0)
    fred._tracer(0)

    draw_rec(fred, 10, 10, 40, 60)

    # draw_usa_flag(fred, -350, 350, 400, 250)

    turtle.done()


def draw_square(tur, x, y, length, color):
    draw_rec(tur, x, y, length, length, color)

def draw_rec(tur, x, y, length, width, color='white'):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()

    tur.fillcolor(color)
    tur.beginfill()

    for i in range(2):
        tur.fd(length)
        tur.right(90)
        tur.fd(width)
        tur.right(90)

    tur.endfill()


def draw_star(tur, x, y, size, color='white'):
    ...

def draw_usa_flag(tur, init_x, init_y, init_w, init_h):
    height = init_h // 13
    # bars
    w = init_w // 13
    h = height
    x = init_x
    for i in range (13):
        y = init_y + (i * h)
        if i % 2 == 0:
            # even - red
            draw_rec()
        else:
            # odd - white
            draw_rec()

    # draw blue background for stars
    x = init_x
    y = init_y
    w = init_w * 2/5
    h = height * 7
    # stars
    offset_x = w // 7
    offset_y = height * .65
    size = init_w * 1 / 50 
    row_y = init_y + 15
    for row in range(9):
        y = row_y
        if row % 2 == 0:
            # even - 6 stars
            for i in range(6):
                x = init_x + offset_x // 2 + (i * offset_x)
                draw_star(tur, x, y, size, 'white')
        else:
            # odd - 5 star with an offset
            for i in range(6):
                x = init_x + offset_x // 2 + (i * offset_x)
                draw_star(tur, x, y, size, 'white')
        row_y -= offset_y


main()