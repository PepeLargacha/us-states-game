import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
screen.title("U.S. States Game")
screen.setup(740, 580)
turtle.hideturtle()

db = pd.read_csv("50_states.csv")
states_df = db.assign(found=False)
#states_df = states_df.set_index('state', drop=False)


game_is_on = True
while game_is_on:
    correct = (states_df['found'] == True).sum()

    if correct != 50:
        answer = turtle.textinput(f" {correct}/50 Guess the State", "What's another state's name?\n")

        if answer != None:
            answer = answer.title()

            if answer in [y for x, y in list(states_df.state.items())]:
                state = states_df[states_df.state == answer]
                states_df.loc[state.index, ['found']] = True
                turtle.penup()
                turtle.goto(int(state.x), int(state.y))
                turtle.write(f"{state.state.item()}")

    if correct == 50 or answer == None:
        game_is_on = False

states_to_learn = states_df.query('found == False')['state']
states_to_learn.to_csv("states_to_learn.csv")

turtle.mainloop()