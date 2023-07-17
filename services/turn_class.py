import time

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