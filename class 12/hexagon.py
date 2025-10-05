import turtle
screen=tutle.Screen()
screen.screensize(400,400)
screen.title("polygon")
screen.bgcolor("cyan")

t=turtle.Turtle()
t.color('navy')
t.width(10)
t.fillcolor('darkcyan')
n=6
a= 360/6
t.begin_fill()
for i in range(6):
    t.forward(150)
    t.right(a)
t.end.fill()

turtle_done()