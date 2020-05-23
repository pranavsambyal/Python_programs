import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Green")
amy.forward(50)
amy.speed(0)
kenji = turtle.Turtle()
kenji.forward(60)
kenji.pencolor("Red")
kenji.speed(0)
if kenji.pencolor() == "Red":
   for x in range(99999):
        kenji.right(x)
        amy.left(x)
        kenji.forward(20)
        amy.forward(20)
else:
    kenji.left(60)
    kenji.forward(100)
