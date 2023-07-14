from flask import Flask, request, redirect, render_template, url_for
from controller.arduino_service import board

app = Flask(__name__)

app.secret_key = "1"
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run")
def run():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
