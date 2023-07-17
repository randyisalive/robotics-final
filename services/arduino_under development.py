import pyfirmata
import time


# HAVENT TESTED YET

class Arduino:
    def __init__(self, port):
        self.board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
        self.servo_bottom_pin = 13
        self.servo_left_pin = 12
        self.servo_right_pin = 11
        self.servo_claw_pin = 10
        servo_bottom = self.board.get_pin("d:13:s")  # bottom servo
        servo_left = self.board.get_pin("d:12:s")  # left servo
        servo_right = self.board.get_pin("d:11:s")  # right servo
        servo_claw = self.board.get_pin("d:10:s")  # servo claw
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
    def print_test(self):
        print("This is a test print")
        print(self.board)
