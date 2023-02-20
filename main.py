import random
import turtle
from turtle import Turtle,Screen

screen=Screen()
screen.listen()
screen.title("Turtle Racing Game")
colour=["red","orange","yellow","blue","purple","green"]
All_Turtle=[]

startRace=False
userChoose=screen.textinput(title="Make your Bet",prompt="Which colour will win the race? Enter a clour:")

screen.setup(width=500,height=400)

y=-110
for turtle_index in range(0,6):

    tim=Turtle("turtle")
    tim.color(colour[turtle_index])
    All_Turtle.append(tim)
    tim.pu()
    tim.goto(x=-235,y=y)
    All_Turtle.append(tim)
    y=tim.ycor() + 40


if userChoose:
    startRace=True

while startRace:

    for single_turtle in All_Turtle:
        if single_turtle.xcor() >= 225:
            startRace=False
            winning_colour = single_turtle.pencolor()

            if winning_colour == userChoose:
                print(f"You have win! The {winning_colour} turtle is the winner!")
                break
            else:
                print(f"You have loss! The {winning_colour} turtle is the winner!")
                break

        random_distance=random.randint(0,10)
        single_turtle.forward(random_distance)


screen.exitonclick()