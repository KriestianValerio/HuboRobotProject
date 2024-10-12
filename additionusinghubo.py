from cs1robots import *

load_world("worlds/add1.wld")
# load_world("worlds/add2.wld")
# load_world("worlds/add34.wld")

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def go_straight():
    while hubo.front_is_clear():
        hubo.move()


hubo.turn_left()
hubo.move()
turn_right()
go_straight()
turn_right()

n = 0

while hubo.on_beeper():
    
    while hubo.on_beeper():
        hubo.pick_beeper()  
        n += 1
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()  
        n += 1
    
    if n > 10:
        while n>10:
            hubo.drop_beeper()
            n -= 1
        turn_around()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
        hubo.drop_beeper()
        n=0

    elif n < 10:
        while n > 0:
            hubo.drop_beeper()
            n -= 1
        turn_around()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
    


    
    
