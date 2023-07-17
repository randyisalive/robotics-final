from flask import Blueprint, redirect, url_for, render_template, request, session
import services.arduino_service as ardSer
import pyfirmata

run = Blueprint('run', __name__)

servo_bottom_pin = 13
servo_left_pin = 12
servo_right_pin = 11
servo_claw_pin = 10


@run.route('/')
def index():
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    servo_bottom = board.get_pin("d:13:s")  # bottom servo
    servo_left = board.get_pin("d:12:s")  # left servo
    servo_right = board.get_pin("d:11:s")  # right servo
    servo_claw = board.get_pin("d:10:s")  # servo claw

    ardSer.run()
    return redirect(url_for('index'))