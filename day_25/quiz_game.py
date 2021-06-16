import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

# Helper function to get co-ordinates of states on the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()  # Keeps screen open

answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?")