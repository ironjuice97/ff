import turtle as t
from Marble import Marble
from Point import Point
from random import shuffle
from time import sleep
from os import system

# Window setup
wn = t.Screen()
wn.title("Mastermind")
wn.bgcolor("light grey")
wn.setup(height=650, width=400)

# Function to get player name
def get_player_name():
    return textinput("Player Name", "Enter your name:")

player_name = get_player_name()

# Game variables
y_fill1_t = 270
y_fill1_b = 240

# Game logic
# Updated list of colors
code_list = ["red", "blue", "green", "yellow", "purple", "black"]

# Shuffle the colors
shuffle(code_list)

# Selecting four colors to create the code
c0 = code_list[0]  # c0 is the first color of the code
c1 = code_list[1]  # c1 is the second color of the code
c2 = code_list[2]  # c2 is the third color of the code
c3 = code_list[3]  # c3 is the fourth color of the code

# Creating the code
code = c0 + c1 + c2 + c3

# Game parameters
ans_count = 1  # ans_count is the number of attempts
ans_limit = 10
gameover = False

# Initializing variables for the answer
a0 = ""  # a0 is the first color of the answer
a1 = ""  # a1 is the second color of the answer
a2 = ""  # a2 is the third color of the answer
a3 = ""  # a3 is the fourth color of the answer

# Message Turtle
msg = t.Turtle()
msg.ht()
msg.speed(0)
msg.penup()
msg.color("grey")
msg.goto(-20, 277)

# Painter Turtle
pic = t.Turtle()
pic.ht()
pic.color("grey")
pic.penup()
pic.speed(0)
pic.pensize(10)
pic.goto(-150, -230)
pic.pendown()
pic.fd(250)
pic.penup()
pic.pensize(0.5)

# Drawing the main circles
xline = -120
yline = 240
line_no = 1
while line_no <= 10:
    while xline >= -130 and xline <= 30:
        pic.goto(xline, yline)
        pic.pendown()
        pic.circle(15)
        pic.penup()
        xline += 50
    xline = -120
    yline -= 50
    line_no += 1

# Drawing Indicator Circles
linesmall = 1
ysmall = 260
while linesmall <= 10:
    pic.goto(70, ysmall)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(90, ysmall)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(70, ysmall - 20)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    pic.goto(90, ysmall - 20)
    pic.pendown()
    pic.circle(5)
    pic.penup()
    linesmall += 1
    ysmall -= 50

# Giving line numbers
line = 1
ydraw = 245
while line <= 10:
    pic.goto(-150, ydraw)
    pic.write(line, align="center", font=("Arial", 10, "normal"))
    line += 1
    ydraw -= 50

# Enter and Reset Buttons
pic.goto(175, 245)
pic.write("ENTER", align="right", font=("Arial", 15, "normal"))
pic.goto(175, -205)
pic.write("RESET", align="right", font=("Arial", 15, "normal"))

# Color Picking Circles
colors = ["red", "blue", "green", "yellow", "purple", "black"]
color_no = 0
ycol = 190
while color_no <= 5:
    pic.goto(140, ycol)
    pic.fillcolor(colors[color_no])
    pic.begin_fill()
    pic.circle(15)
    pic.end_fill()
    ycol -= 50
    color_no += 1

# Check function
def check():
    global ans_count, gameover, y_fill1_t, y_fill1_b, a0, a1, a2, a3
    ans = a0 + a1 + a2 + a3
    red = 0
    white = 0
    # Check if inputs are valid and game is not over
    if a0 != a1 and a0 != a2 and a0 != a3 and a1 != a2 and a1 != a3 and a2 != a3 and a0 != "" and a1 != "" and a2 != "" and a3 != "" and not gameover:
        y_fill1_t -= 50
        y_fill1_b -= 50
        ans_count += 1
        # Counting correct color in correct place (red) and correct color in wrong place (white)
        if a0 == c0:
            red += 1
        elif a0 in code:
            white += 1
        if a1 == c1:
            red += 1
        elif a1 in code:
            white += 1
        if a2 == c2:
            red += 1
        elif a2 in code:
            white += 1
        if a3 == c3:
            red += 1
        elif a3 in code:
            white += 1
        # Draw indicators for correct guesses
        if ans != code:
            ind = [(70, 360 - 50 * ans_count), (90, 360 - 50 * ans_count), (70, 340 - 50 * ans_count), (90, 340 - 50 * ans_count)]
            shuffle(ind)
            draw_white = 0
            draw_red = 0
            while draw_white < white:
                pic.goto(ind[0])
                pic.pendown()
                pic.fillcolor("white")
                pic.begin_fill()
                pic.circle(5)
                pic.end_fill()
                pic.penup()
                ind.pop(0)
                draw_white += 1
            while draw_red < red:
                pic.goto(ind[0])
                pic.pendown()
                pic.fillcolor("red")
                pic.begin_fill()
                pic.circle(5)
                pic.end_fill()
                pic.penup()
                ind.pop(0)
                draw_red += 1
        # Check game over conditions
        if ans != code and ans_count > ans_limit:
            msg.write("You ran out of chances!", align="center", font=("Arial", 20, "normal"))
            gameover = True
        elif ans == code:
            gameover = True
            msg.write("Congrats! You Won!", align="center", font=("Arial", 20, "normal"))
        # Reset answer colors
        a0, a1, a2, a3 = "", "", "", ""
    else:
        msg.write("Invalid Input", align="center", font=("Arial", 20, "normal"))
        sleep(1)
        msg.clear()

# Mouse Click Function
def clk(x, y):
    global a0, a1, a2, a3, ans_count, y_fill1_b, y_fill1_t
    # Color Picking
    if 125 < x < 155 and not gameover:
        color_bounds = [(190, "red"), (140, "blue"), (90, "green"), (40, "yellow"), (-10, "purple"), (-60, "black")]
        for bound, color in color_bounds:
            if bound < y < bound + 30:
                pic.fillcolor(color)
                break
    # Enter Button
    if 105 < x < 175 and 245 < y < 275 and not gameover:
        check()
    # Filling Circles
    if y_fill1_b < y < y_fill1_t and ans_count <= ans_limit and not gameover:
        circle_positions = [(-120, a0), (-70, a1), (-20, a2), (30, a3)]
        for xpos, color_var in circle_positions:
            if -135 < x < -105 + xpos:
                pic.goto(xpos, 290 - 50 * ans_count)
                pic.pendown()
                pic.begin_fill()
                pic.circle(15)
                pic.end_fill()
                pic.penup()
                color_var = pic.fillcolor()
                break
    # Reset Button
    if 110 < x < 175 and -207 < y < -188:
        wn.bye()
        system("Mastermind.py")

# Listening to mouse click
t.onscreenclick(clk)
t.listen()
t.done()