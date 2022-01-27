import turtle
# em deda
def prepare_fig(fig, x, y):
    fig.hideturtle()
    fig.penup()
    fig.setposition(x, y)
    fig.speed(13)

def draw_square(fig, color, side_length):
    fig.pendown()
    fig.fillcolor(color)
    fig.begin_fill()
    for i in range(4):
        fig.fd(side_length)
        fig.rt(90)
    fig.end_fill()

def message(text, color):
    circ.hideturtle()
    circ.goto(0, 0)
    circ.color(color)
    sq.clear()
    sq2.clear()
    print(moves)
    circ.write(text, font=("Arial", 12, "bold"))

def win_or_die(moves):
    if -20 < circ.xcor() < 40 and 10 < circ.ycor() < 70:
        message(GAME_OVER_MSG + str(moves), 'red')
    if -60 < circ.xcor() < -20 and 50 < circ.ycor() < 90:
        message(WIN_MSG + str(moves), 'green')

def movey(deltay):
    global moves
    y = circ.ycor() + deltay
    circ.sety(y)
    moves += 1
    win_or_die(moves)

def movex(deltax):
    global moves
    x = circ.xcor() + deltax
    circ.setx(x)
    moves += 1
    win_or_die(moves)

wndow = turtle.Screen()
wndow.title("Circle game")
wndow.setup(500, 500)

circ = turtle.Turtle()
circ.penup()
circ.shape("circle")
circ.color("orange")

sq = turtle.Turtle()
prepare_fig(sq, -20, 70)
draw_square(sq, 'red', 60)
sq2 = turtle.Turtle()
prepare_fig(sq2, -60, 90)
draw_square(sq2, 'green', 40)

moves = 0
GAME_OVER_MSG = 'Game over!\nСделано шагов: '
WIN_MSG = 'Победа!\nСделано шагов: '
STEP = 10

turtle.listen()
turtle.onkeypress(lambda: movey(STEP), 'Up')
turtle.onkeypress(lambda: movey(-STEP), 'Down')
turtle.onkeypress(lambda: movex(STEP), 'Right')
turtle.onkeypress(lambda: movex(-STEP), 'Left')
turtle.done()