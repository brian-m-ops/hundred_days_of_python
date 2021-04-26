"""Can't run locally. This is just the solution to the challenge on
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()