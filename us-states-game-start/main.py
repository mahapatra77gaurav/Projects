import turtle
import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def write_answer(answer_states,x,y):
    region = Turtle()
    region.penup()
    region.goto(x,y)
    region.write(arg=answer_states, align='center', font=('Arial', 8, 'normal'))
    region.hideturtle()


correct_guesses = []
states = pandas.read_csv("50_states.csv")
all_states = states["state"].to_list()

while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?")).title()
    if answer_state in all_states:
        answer_row = states[states["state"] == answer_state]
        xcor = answer_row["x"].item()
        ycor = answer_row["y"].item()
        write_answer(answer_state,xcor,ycor)
        correct_guesses.append(answer_state)
        all_states.remove(answer_state)
    if answer_state == "Exit":
        df = pandas.DataFrame(all_states)
        df.to_csv("states to learn.csv")
        break
