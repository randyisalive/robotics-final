from flask import Flask, request, redirect, render_template, url_for
from controller.run import run
import pyfirmata
import services.arduino_service as AS
app = Flask(__name__)

app.secret_key = "1"
app.debug = True




@app.route("/")
def index():
    return render_template("index.html")


@app.route('/reset')
def reset():
    board = pyfirmata.Arduino("/dev/cu.wchusbserial1410")
    AS.reset(board)
    board.exit()
    return redirect(url_for("index"))

@app.route('/move_bottom')
def move_bottom():
    AS.move_botom(180)
    return redirect(url_for("index"))


@app.route('/move_right')
def move_right():
    AS.move_right(180) # plus more down
    return redirect(url_for('index'))


@app.route('/move_claw')
def move_claw():
    degree = 180
    AS.move_claw(degree) # 0 close, 180 open
    print("Move claw to: " + str(degree))
    return redirect(url_for('index'))

@app.route('/move_left')
def move_left():
    AS.move_left(0)
    return redirect(url_for('index'))



app.register_blueprint(run, url_prefix='/run')



if __name__ == "__main__":
    app.run(port=3000)
