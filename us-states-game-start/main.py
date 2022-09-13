import turtle
import pandas as pd

screen=turtle.Screen()

screen.title("US State Games")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state=screen.textinput(title="Guess the state",prompt="what is the next state?")
#print(answer_state)

print(answer_state)


score=0
data=pd.read_csv("50_states.csv")
states=data["state"].tolist()
print(states)

def get_mouse_click_coord(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coord)

if answer_state in states:
    coordinates=turtle.onscreenclick(get_mouse_click_coord)
    turtle.write(answer_state)






def get_mouse_click_coord(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coord)

turtle.mainloop()

#screen.exitonclick()