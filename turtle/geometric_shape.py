import turtle

t = turtle.Turtle()
s = turtle.Screen()

# fonction pour tracer une figure d une forme geometrique de différentes couleurs avec le rayon spécifié.


def figure(nbr_figure, rayon, nbr_cote=None, position=[], couleur=[], orientation=0):
    for i in range(nbr_figure):
        t.up()
        t.home()
        t.goto(position[i])
        t.down()
        if not couleur:
            t.color("black")
        else:
            t.color(couleur[i])
        t.begin_fill()
        if not couleur:
            t.fillcolor("white")
        else:
            t.fillcolor(couleur[i])
        if nbr_cote == None:
            t.circle(rayon)
        else:
            t.setheading(orientation)
            t.circle(rayon, steps=int(nbr_cote))
        t.end_fill()
    t.hideturtle()


# pour dessiner un rectangle
def rectangle(L, l, inside_color="white", line_color="black"):
    t.color(line_color)
    t.begin_fill()
    t.fillcolor(inside_color)
    for i in range(2):
        t.forward(L)
        t.rt(90)
        t.fd(l)
        t.rt(90)
    t.end_fill()



