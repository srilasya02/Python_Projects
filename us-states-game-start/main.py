import turtle
import pandas as pd

screen=turtle.Screen()

screen.title("US State Games")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data["state"].tolist()
#print(states)
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)/50}",prompt="what is the next state?").title()
    #answer_state.title()
    if answer_state=="Exit":
        missing=[]
        for state in states:
            if state not in guessed_states:
                missing.append(state)
        new_data=pd.DataFrame(missing)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data=data[data.state==answer_state]
        #print(states_data)
        t.goto(int(states_data.x),int(states_data.y))
        t.write(answer_state)

#screen.exitonclick()



