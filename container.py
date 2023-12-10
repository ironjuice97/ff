from Marble import Marble
from Point import Point
import turtle as t

# Define the leaderboard file path
leaderboard_file = "leaderboard.txt"

class Container:
    def __init__(self, x, y, width, height, border_thickness=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_thickness = border_thickness
        self.pen = t.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)  # Draw at the fastest speed

    def draw(self):
        self.pen.pensize(self.border_thickness)  # Set the border thickness
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.pendown()
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.penup()

class GameDisplay(Container):
    def __init__(self):
        super().__init__(x=-280, y=360, width=350, height=540, border_thickness=4)
        self.guess_marbles = []
        self.indicator_marbles = []

    def draw_marbles_and_indicators(self):
        yOffset = 100  # Increase this value to move the marbles higher
        for row in range(10):  # Assuming 10 rows
            row_guess_marbles = []
            row_indicator_marbles = []
            for col in range(4):  # Assuming 4 guesses per row
                guess_position = Point(-250 + col * 50, 210 - row * 50 + yOffset)
                guess_marble = Marble(guess_position, "grey", 15)
                row_guess_marbles.append(guess_marble)
                guess_marble.draw_empty()

            for i in range(2):  # Two columns of indicators
                for j in range(2):  # Two rows of indicators
                    indicator_x = 2 + i * 15
                    indicator_y = 225 - row * 50 - j * 15 + yOffset
                    indicator_position = Point(indicator_x, indicator_y)
                    indicator_marble = Marble(indicator_position, "white", 5)
                    row_indicator_marbles.append(indicator_marble)
                    indicator_marble.draw_empty()

            self.guess_marbles.append(row_guess_marbles)
            self.indicator_marbles.append(row_indicator_marbles)

class Leaderboard(Container):
    def __init__(self):
        super().__init__(x=110, y=360, width=160, height=540, border_thickness=4)

    def draw(self):
        self.pen.pencolor("blue")  # Change the border color to blue
        self.pen.pensize(self.border_thickness)  # Set the border thickness
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.pendown()
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.penup()

# Define the Point and Marble classes here (assuming they are implemented elsewhere in your code)

class UserBoard(Container):
    def __init__(self):
        super().__init__(x=-280, y=-200, width=550, height=150, border_thickness=4)
        self.color_picker_turtle = t.Turtle()
        self.color_picker_turtle.hideturtle()
        self.color_picker_turtle.speed(0)
        self.color_picker_turtle.penup()

    def draw_color_pickers(self, display_colors, available_colors_per_row, current_row):
        self.color_picker_turtle.clear()  # Clear existing pickers before redrawing
        xpos = -250  # Starting position for color pickers
        ypos = -300  # Vertical position for color pickers

        for color in display_colors:
            self.color_picker_turtle.goto(xpos, ypos)
            self.color_picker_turtle.pendown()

            # Draw the outline
            self.color_picker_turtle.pencolor("black")
            self.color_picker_turtle.circle(15)

            # Fill the color if it's still available
            if color in available_colors_per_row[current_row]:
                self.color_picker_turtle.fillcolor(color)
                self.color_picker_turtle.begin_fill()
                self.color_picker_turtle.circle(15)
                self.color_picker_turtle.end_fill()
            else:
                pass  # Logic for unavailable colors

            self.color_picker_turtle.penup()
            xpos += 50  # Increment xpos for the next color picker
            
# Function to read the leaderboard file and return a sorted list of scores.
def read_leaderboard():
    try:
        with open(leaderboard_file, "r") as file:
            lines = file.readlines()
        leaderboard = [line.strip().split(",") for line in lines]
        leaderboard.sort(key=lambda x: int(x[1]), reverse=True)  # Sort in descending order by score
        return leaderboard
    except FileNotFoundError:
        # Handle the case when the leaderboard file doesn't exist yet
        return []

# Function to display the top scores from the leaderboard on the screen.
def display_leaderboard():
    leaderboard = read_leaderboard()
    leaderboard_display = t.Turtle()
    leaderboard_display.ht()
    leaderboard_display.penup()
    leaderboard_display.goto(t.window_width() / 3, t.window_height() / 2 - 100)
    leaderboard_display.write("Leaders:", align="right", font=("Arial", 16, "bold"))
    y_pos = t.window_height() / 2 - 150
    for i, (name, score) in enumerate(leaderboard[:5]):
        leaderboard_display.goto(t.window_width() / 4, y_pos - (20 * i))
        leaderboard_display.write(f"{i + 1}. {name} - {score}", align="right", font=("Arial", 12, "normal"))

    

# Setup turtle screen
screen = t.Screen()
screen.setup(width=600, height=800)

# Create and draw each section
game_display = GameDisplay()
leaderboard = Leaderboard()
userboard = UserBoard()

game_display.draw()
leaderboard.draw()
userboard.draw()

# Call methods to display contents within each section
game_display.draw_marbles_and_indicators()  # Call to display marbles and indicators in GameDisplay

# Display the leaderboard
display_leaderboard()

# To keep the window open
t.mainloop()