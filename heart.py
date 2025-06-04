import turtle

# Set up turtle window
window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()
pen.hideturtle()

# Keep the window open
turtle.done()
