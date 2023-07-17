import pyfirmata
import time


# define the pin
servo_bottom_pin = 13
servo_left_pin = 12
servo_right_pin = 11
servo_claw_pin = 10




class turn:
    def positive_turn(servo, start_angle, end_angle):
        print("Turning: " + str(servo))
        # Set the initial position of the servo
        servo.write(start_angle)

        # Set the step size for each iteration
        step = 1

        # Set the delay between each step (in seconds)
        delay = 0.1

        # Move the servo gradually from the start position to the end position
        for angle in range(start_angle, end_angle + step, step):
            servo.write(angle)
            time.sleep(delay)

    def negative_turn(servo, start_angle, end_angle):
        print("Turning: " + str(servo))
        servo.write(start_angle)
        step = -1
        delay = 0.1

        for angle in range(start_angle, end_angle + step, step):
            servo.write(angle)
            time.sleep(delay)


def reset(board):
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


def run():
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_bottom = board.get_pin("d:13:s")  # bottom servo
    servo_left = board.get_pin("d:12:s")  # left servo
    servo_right = board.get_pin("d:11:s")  # right servo
    servo_claw = board.get_pin("d:10:s")  # servo claw
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


def console():
    print("Bottom Servo Angle: " + str(servo_bottom.read()))
    print("Left Servo Angle: " + str(servo_left.read()))
    print("Right Servo Angle: " + str(servo_right.read()))
    print("Claw Servo Angle: " + str(servo_claw.read()))



def move_botom(degree):
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_bottom = board.get_pin("d:13:s")  # bottom servo
    if degree < 90:
        turn.negative_turn(servo_bottom, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_bottom, 90, degree)
    elif degree == 90:
        servo_bottom.write(degree)
    board.exit()

def move_right(degree):
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_right = board.get_pin("d:{}:s".format(servo_right_pin))
    if degree < 90:
        turn.negative_turn(servo_right, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_right, 90, degree)
    elif degree == 90:
        servo_right.write(degree)    
        board.exit()

def move_claw(degree):
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_claw = board.get_pin("d:{}:s".format(servo_claw_pin))
    if degree < 90:
        turn.negative_turn(servo_claw, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_claw, 90, degree)
    elif degree == 90:
        servo_claw.write(degree)
    board.exit()

def move_left(degree):
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_left = board.get_pin("d:{}:s".format(servo_left_pin))
    if degree < 90:
        turn.negative_turn(servo_left, 90, degree)
    elif degree > 90:
        turn.positive_turn(servo_left, 90, degree)
    elif degree == 90:
        servo_left.write(degree)
    board.exit()


# run the loop
""" while True:
    console()
    time.sleep(5)
    board.exit() """
