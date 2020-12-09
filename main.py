import turtle
import pandas as pd

# Create screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the csv data
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()

# main
def main():
    state_count = 0
    while state_count < 51:
        # get answer from user
        answer_state = screen.textinput(title=f"{state_count}/50 Correct",
                                        prompt="What's another state name?").title()
        # loop flag
        if answer_state == "Exit":
            break
        # count how many correct answers user knew
        state_count += is_on_map(answer_state)

    # save missed states in the csv file
    st = pd.DataFrame(states)
    st.to_csv("states_to_learn.csv")


# return 1 if state is correct or 0 if not correct
def is_on_map(state):
    correct = 0
    # create turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    # check the input state
    if state in states:
        states.remove(state)  # remove the state from the states list
        state_data = (states_data[states_data['state'] == state])  # get row of the state
        x_cor = state_data["x"]
        y_cor = state_data["y"]
        t.goto(int(x_cor), int(y_cor))  # goto the coordinates
        t.write(state)  # write the name of the state on the screen
        correct = 1

    return correct


main()

