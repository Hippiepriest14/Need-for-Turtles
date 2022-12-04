from turtle import Turtle, Screen
import random


def need_for_turtles():
    is_race_on = False
    screen = Screen()
    screen.setup(500, 400)
    screen.title("Welcome to the Need For Turtles!")
    user_bet = screen.textinput("Make your bet", "Which turtle will win the race?Enter a color ("
                                                 "red/yellow/orange/green/blue/purple: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = -70
    all_turtles = []
    for turtle_index in range(0, 6):
        tim = Turtle(shape="turtle")
        tim.color(colors[turtle_index])
        tim.penup()
        y_positions += 30
        tim.goto(-230, y_positions)
        all_turtles.append(tim)
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    a = screen.textinput(f'You win! The {winning_color} won!',
                                         "Let's play again? Enter "
                                         "continue or exit:       ")
                    if a == "exit":
                        break
                    if a == "continue":
                        screen.clear()
                        need_for_turtles()
                else:
                    a = screen.textinput(f'You lose! The {winning_color} won!',
                                         "Let's play again? Enter "
                                         "continue or exit:       ")
                    if a == "exit":
                        break
                    if a == "continue":
                        screen.clear()
                        need_for_turtles()




need_for_turtles()
