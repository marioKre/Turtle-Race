import random
from turtle import Turtle, Screen

# Create a screen with a specific width and height
screen = Screen()
screen.setup(width=500, height=400)

# Set up a list of colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up a flag to track whether the race is on or not
is_race_on = False

# Prompt the user to make a bet on which turtle will win the race, with exception handling
while True:
    try:
        user_bet = screen.textinput(
            title="Make your bet",
            prompt=f"Which turtle will win the race?\nPick one out of these turtles:\n\n {', '.join(colors)}\n"
        )
        if user_bet.lower() in colors:
            is_race_on = True
            break
        elif user_bet == "quit":
            break
        else:
            raise ValueError("Not a valid color")
    except ValueError as error:
        print(error)


# Initialize a list to hold all the turtles
all_turtles = []

# Set up the y-positions for the turtles
y_positions = [-80, -50, -20, 10, 40, 70]

# Create and position the racing turtles
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


# Create a turtle to write the final message
message_turtle = Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(x=0, y=150)


# Run the race
while is_race_on:
    for turtle in all_turtles:
        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 230:
            # If so, stop the race and display the winning message
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                message_turtle.write(
                    f"You've won! {winning_color.title()} turtle won the race.",
                    align="center",
                    font=("Arial", 16, "bold")
                )
            else:
                message_turtle.write(
                    f"You've lost! {winning_color.title()} turtle won the race.",
                    align="center",
                    font=("Arial", 16, "bold")
                )
        # Move the turtle a random distance
        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)

# Wait for the user to close the window
screen.exitonclick()
