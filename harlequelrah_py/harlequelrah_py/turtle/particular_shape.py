import turtle

t = turtle.Turtle()
s = turtle.Screen()
# heart
def heart(inside_color="white", line_color="black", background_color="white"):
    s.bgcolor = background_color
    t.color(line_color)
    t.begin_fill()
    t.fillcolor(inside_color)
    t.lt(140)
    t.fd(180)
    t.circle(-90, 200)
    # t.lt(120)
    t.seth(60)
    t.circle(-90, 200)
    t.fd(180)
    t.end_fill()
