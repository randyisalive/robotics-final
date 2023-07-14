from flask import Flask, request, redirect, render_template, url_for
from controller.run import run
app = Flask(__name__)

app.secret_key = "1"
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")



app.register_blueprint(run, url_prefix='/run')



if __name__ == "__main__":
    app.run()
