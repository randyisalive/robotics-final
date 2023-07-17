import pyfirmata
import time
from configuration import check_os
from services.turn_class import turn



arduino_port = check_os() # declare function
# define the pin
servo_bottom_pin = 13
servo_left_pin = 12
servo_right_pin = 11
servo_claw_pin = 10
# define the pin


    



def reset():
    board = pyfirmata.Arduino(arduino_port)
    servo_bottom = board.get_pin("d:13:s")  # bottom servo
    servo_left = board.get_pin("d:12:s")  # left servo
    servo_right = board.get_pin("d:11:s")  # right servo
    servo_claw = board.get_pin("d:10:s")  # servo claw
    servo_bottom.write(90)
    print("Bottom to 90")
    servo_left.write(90)
    print("Left to 90")
    servo_right.write(90)
    print("Right to 90")
    servo_claw.write(90)
    board.exit()


def run(): # this is the main code
    board = pyfirmata.Arduino(arduino_port)
    servo_bottom = board.get_pin("d:{}:s".format(servo_bottom_pin))  # bottom servo
    servo_left = board.get_pin("d:{}:s".format(servo_left))  # left servo
    servo_right = board.get_pin("d:{}:s".format(servo_right))  # right servo
    servo_claw = board.get_pin("d:{}:s".format(servo_claw_pin))  # servo claw
    time.sleep(3)
    print("Turning bottom servo")
    turn.negative_turn(servo_bottom, 90, 20)  # turn claw to the front
    time.sleep(5)
    # bring the claw forward
    print("Bring Claw Forward")
    turn.positive_turn(servo_left, 90, 180)
    turn.positive_turn(
        servo_right, 90, 180
    )  # so for servo right, bigger make the arm more down
    time.sleep(1)
    # open claw
    print("Opening Claw")
    turn.positive_turn(servo_claw, 90, 180) # this is open claw REMEMBER
    time.sleep(1)
    # close the claw REMEMBER
    print("Close the claw")
    turn.negative_turn(servo_claw, 180, 0)
    # pick up the item and move it
    print("Picking up item, then turn")
    turn.negative_turn(servo_left, 180, 100)
    turn.negative_turn(servo_right, 180, 0)
    time.sleep(3)
    turn.positive_turn(servo_bottom, 20, 90)
    time.sleep(3)
    turn.positive_turn(servo_claw, 0, 180)
    print("RUN DONE")
    # run done
    time.sleep(2)
    board.exit()



def move_botom(degree):
    board = pyfirmata.Arduino(arduino_port)
    servo_bottom = board.get_pin("d:13:s")  # bottom servo
    if degree < 90:
        turn.negative_turn(servo_bottom, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_bottom, 90, degree)
    elif degree == 90:
        servo_bottom.write(degree)
    board.exit()

def move_right(degree):
    board = pyfirmata.Arduino(arduino_port)
    servo_right = board.get_pin("d:{}:s".format(servo_right_pin))
    if degree < 90:
        turn.negative_turn(servo_right, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_right, 90, degree)
    elif degree == 90:
        servo_right.write(degree)    
    board.exit()

def move_claw(degree):
    board = pyfirmata.Arduino(arduino_port)
    servo_claw = board.get_pin("d:{}:s".format(servo_claw_pin))
    if degree < 90:
        turn.negative_turn(servo_claw, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_claw, 90, degree)
    elif degree == 90:
        servo_claw.write(degree)
    board.exit()

def move_left(degree):
    board = pyfirmata.Arduino(arduino_port)
    servo_left = board.get_pin("d:{}:s".format(servo_left_pin))
    if degree < 90:
        turn.negative_turn(servo_left, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_left, 90, degree)
    elif degree == 90:
        servo_left.write(degree)
    board.exit()
