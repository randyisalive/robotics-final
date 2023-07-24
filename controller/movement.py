from flask import Blueprint, redirect, render_template, url_for, request
import services.arduino_service as AS


movement = Blueprint('movement', __name__)

@movement.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        typeData = request.form['type']
        input_data = request.form['degree']
        if int(input_data) > 256:
            return "Error"    # check to see if the user set above 256
        if typeData == "bottom":
            return redirect(url_for("movement.move_bottom", degree = int(input_data)))
        if typeData == "claw":
            return redirect(url_for('movement.move_claw', degree = int(input_data)))
        if typeData == "left":
            return redirect(url_for('movement.move_left', degree = int(input_data)))
        if typeData == "right":
            return redirect(url_for('movement.move_right', degree = int(input_data)))
        if typeData == None:
            return 'Error, choose something'
    return render_template('movement.html')



@movement.route('/move_bottom/<degree>')
def move_bottom(degree):
    AS.move_botom(degree)
    print("Move bottom to: " + str(degree))
    return redirect(url_for("app.index"))

@movement.route('/move_right/<degree>')
def move_right(degree):
    AS.move_right(degree) # plus more down
    print("Move right to: " + str(degree))
    return redirect(url_for('app.index'))


@movement.route('/move_claw/<degree>')
def move_claw(degree):
    AS.move_claw(degree) # 0 close, 180 open
    print("Move claw to: " + str(degree))
    return redirect(url_for('app.index'))

@movement.route('/move_left/<degree>')
def move_left(degree):
    AS.move_left(degree)
    print("Move left to: " + str(degree))
    return redirect(url_for('app.index'))




