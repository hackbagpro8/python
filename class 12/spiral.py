import turtle
screen=turtle.Screen()
screen.screensize(400,400)
screen.title("spiral")
screen.bgcolor("cyan")

t=turtle.Turtle()
t.color('navy')
t.width(1)

s=5
while True:
    t.forward(s)
    t.right(90)
    s+= 3
