from cs1robots import *

# Your code must work for all world files below.
# load_world( "worlds/trash1.wld" )
load_world( "worlds/trash2.wld" )
hubo = Robot()
hubo.set_trace('red')

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_and_collect():
    while hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            while hubo.on_beeper():
                hubo.pick_beeper()

move_and_collect()
turn_around()
move_and_collect()
turn_right()
hubo.move()

while hubo.carries_beepers():
    hubo.drop_beeper()

turn_around()
hubo.move()
hubo.turn_left()
