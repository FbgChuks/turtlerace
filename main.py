import random
import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=900, height=400)

user_stake = screen.textinput(title= "place your stakes", prompt="which color turtle will win? Enter a color(red, orange, yellow, green, blue, purple): ").lower()
colors =["red", "orange", "yellow", "green", "blue", "purple"]
race_on = False

def color_cons():
    for color in colors:
        yield color

def y_axis():
    coords = [150, 100, 50, 0, -50, -100]

    for _ in coords:
        yield _

coll = color_cons()
new_y = y_axis()
steps = list(range(10))
all_turtle = []

screen.title("FBg Turtle race game")

for color in colors:
    tim = Turtle(shape='turtle')
    tim.color(next(coll))
    tim.penup()
    tim.goto(x=-430, y= next(new_y))
    all_turtle.append(tim )

if user_stake:
    race_on = True



while race_on:

    for turts in all_turtle:
        if turts.xcor() > 430:
            race_on = False
            winner = turts.pencolor()
            if user_stake == winner:
                print(f"You won! {winner} is the winner")
            else:
                print(f"You lost! {winner} is the winner!")




        rand_steps = random.choice(steps)
        turts.forward(rand_steps)


screen.exitonclick()


