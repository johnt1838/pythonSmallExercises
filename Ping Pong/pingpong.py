import turtle
import os
# graphics

window = turtle.Screen()
window.title("Game")
window.bgcolor("black")
window.setup(width=800, height=600)  # window size
window.tracer(0)  # stops the window from updating

# Score
score_a = 0
score_b = 0

# Brick A
brick_a = turtle.Turtle()
brick_a.speed(0)  # speed of animation
brick_a.shape("square")
brick_a.color("blue")
brick_a.shapesize(stretch_wid=5, stretch_len=1)
brick_a.penup()
brick_a.goto(-350, 0)

# Brick B
brick_b = turtle.Turtle()
brick_b.speed(0)  # speed of animation
brick_b.shape("square")
brick_b.color("red")
brick_b.shapesize(stretch_wid=5, stretch_len=1)
brick_b.penup()
brick_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# winner
winner = turtle.Turtle()
winner.speed(0)
winner.color("red")
winner.hideturtle()
winner.goto(0,0)

# Functions
def brick_a_up():
    y = brick_a.ycor()  # returns y cordinate
    y += 20  # add 20 to y
    brick_a.sety(y)


def brick_a_down():
    y = brick_a.ycor()  # returns y cordinate
    y -= 20  # add 20 to y
    brick_a.sety(y)


def brick_b_up():
    y = brick_b.ycor()  # returns y cordinate
    y += 20  # add 20 to y
    brick_b.sety(y)


def brick_b_down():
    y = brick_b.ycor()  # returns y cordinate
    y -= 20  # add 20 to y
    brick_b.sety(y)


# -----------------------------------
# ---test for left and right---------
def brick_a_right():
    x = brick_a.xcor()  # returns y cordinate
    x += 20  # add 20 to y
    brick_a.setx(x)


def brick_a_left():
    x = brick_a.xcor()  # returns y cordinate
    x -= 20  # add 20 to y
    brick_a.setx(x)


# ------------------------------------
# keyboard binding
window.listen()
window.onkeypress(brick_a_up, "w")
window.onkeypress(brick_a_down, "s")
window.onkeypress(brick_a_left, "a")
window.onkeypress(brick_a_right, "d")

window.onkeypress(brick_b_up, "Up")
window.onkeypress(brick_b_down, "Down")

# main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse direction

    if ball.xcor() > 390:
        os.system("aplay sound.wav")
        ball.goto(0, 0)
        ball.dx *= -1  # reverse direction
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        os.system("aplay sound.wav")
        ball.goto(0, 0)
        ball.dx *= -1  # reverse direction
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    # border left and right test
    # if ball.xcor() > 390:
    #     ball.setx(390)
    #     ball.dx *= -1  # reverse direction
    #
    # if ball.xcor() < -390:
    #     ball.setx(-390)
    #     ball.dx *= -1  # reverse direction

    # bouncing

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < brick_b.ycor() + 40 and ball.ycor() > brick_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < brick_a.ycor() + 40 and ball.ycor() > brick_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score_a == 10 or score_b == 10:
        brick_a.hideturtle()
        brick_b.hideturtle()
        ball.hideturtle()
        if score_a == 10:
            winner.write("Winner is Player 1", align="center", font=("Courier", 24, "normal"))
        else:
            winner.write("Winner is Player 2", align="center", font=("Courier", 24, "normal"))
     
