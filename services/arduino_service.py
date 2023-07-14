import pyfirmata
import time


board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")


servo_bottom_pin = 13
servo_left_pin = 12
servo_right_pin = 11
servo_claw_pin = 10


servo_bottom = board.get_pin("d:13:s")  # bottom servo
servo_left = board.get_pin("d:12:s")  # left servo
servo_right = board.get_pin("d:11:s")  # right servo
servo_claw = board.get_pin("d:10:s")  # servo claw


class turn:
    def positive_turn(servo, start_angle, end_angle):
        print("Turning: " + str(servo))
        # Set the initial position of the servo
        servo.write(start_angle)

        # Set the step size for each iteration
        step = 1

        # Set the delay between each step (in seconds)
        delay = 0.01

        # Move the servo gradually from the start position to the end position
        for angle in range(start_angle, end_angle + step, step):
            servo.write(angle)
            time.sleep(delay)

    def negative_turn(servo, start_angle, end_angle):
        print("Turning: " + str(servo))
        servo.write(start_angle)
        step = -1
        delay = 0.01

        for angle in range(start_angle, end_angle + step, step):
            servo.write(angle)
            time.sleep(delay)


def reset():
    servo_bottom.write(90)
    print("Bottom to 90")
    servo_left.write(90)
    print("Left to 90")
    servo_right.write(90)
    print("Right to 90")
    servo_claw.write(90)


def run():
    reset()
    time.sleep(3)
    turn.negative_turn(servo_bottom, 90, 20)  # turn claw to the front
    time.sleep(3)

    # bring the claw forward
    turn.positive_turn(servo_left, 90, 0)
    turn.positive_turn(
        servo_right, 90, 180
    )  # so for servo right, bigger make the arm more down
    time.sleep(10)

    # open claw
    turn.positive_turn(servo_claw, 90, 180)  # this is open claw REMEMBER
    time.sleep(2)
    # close the claw REMEMBER
    servo_claw.write(0)
    # pick up the item and move it
    turn.negative_turn(servo_left, 180, 90)
    turn.negative_turn(servo_right, 180, 90)
    time.sleep(1)
    turn.positive_turn(servo_bottom, 20, 90)
    time.sleep(2)
    servo_claw.write(180)
    # run done


def console():
    print("Bottom Servo Angle: " + str(servo_bottom.read()))
    print("Left Servo Angle: " + str(servo_left.read()))
    print("Right Servo Angle: " + str(servo_right.read()))
    print("Claw Servo Angle: " + str(servo_claw.read()))


# run the loop
""" while True:
    console()
    time.sleep(5)
    board.exit() """
