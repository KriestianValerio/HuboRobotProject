from cs1robots import *

create_world()
hubo = Robot(orientation='S', avenue=9, street=5)
hubo.set_trace('blue')

def go_straight():
    while hubo.front_is_clear():
        hubo.move()


def gobacktoposition():
    if hubo.facing_north():
        hubo.turn_left()
        go_straight()
        hubo.turn_left()
        go_straight()
    else:
        while not hubo.facing_north():
            hubo.turn_left()
        gobacktoposition()

gobacktoposition()
    