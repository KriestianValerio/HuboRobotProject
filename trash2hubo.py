from cs1robots import *

# Your code must work with any of the world files below.
load_world('worlds/trash3.wld')
# load_world('worlds/trash4.wld')

hubo = Robot()
hubo.set_trace('red')

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def pickall():
    while hubo.on_beeper():
                hubo.pick_beeper()

def move_and_collect():
    if hubo.on_beeper():
            pickall()
    while hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            pickall()
              
def go_straight():
    while hubo.front_is_clear():
        hubo.move()

def one_pattern():
    move_and_collect()
    hubo.turn_left()
    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
        move_and_collect()


def zigzag(): 
        turn_right()
        if  hubo.front_is_clear():
            hubo.move()
            turn_right()
            return True
        else:
            return False

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

while True:
    one_pattern()
    zigzag()

    if not hubo.front_is_clear():
        break

gobacktoposition()

while hubo.carries_beepers():
    hubo.drop_beeper()

