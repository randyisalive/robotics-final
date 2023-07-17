from flask import Flask, request, redirect, render_template, url_for
import services.arduino_service as AS
from controller.movement import movement
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "1"
app.debug = True


toolbar = DebugToolbarExtension(app)

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
