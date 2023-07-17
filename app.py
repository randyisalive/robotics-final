from flask import Flask, redirect, render_template, url_for
import services.arduino_service as AS
from controller.movement import movement
app = Flask(__name__)

app.secret_key = "1"
app.debug = False # Debug setting



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run")
def run():
    AS.run()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    AS.reset()
    return redirect(url_for("index"))


app.register_blueprint(movement)

if __name__ == "__main__":
    app.run()
