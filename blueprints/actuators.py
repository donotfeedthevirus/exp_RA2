from flask import Blueprint, render_template, request, redirect, url_for

actuators_bp = Blueprint('actuators', __name__, template_folder='templates')
actuators_dict = {}

@actuators_bp.route('/')
def list_actuators():
    return render_template('actuators.html', actuators=actuators_dict)

@actuators_bp.route('/register', methods=['GET', 'POST'])
def register_actuator():
    if request.method == 'POST':
        name  = request.form['actuator']
        value = request.form.get('value', 0)
        actuators_dict[name] = value
        return redirect(url_for('actuators.list_actuators'))
    return render_template('register_actuator.html')

@actuators_bp.route('/delete', methods=['GET', 'POST'])
def delete_actuator():
    if request.method == 'POST':
        name = request.form['actuator']
        actuators_dict.pop(name, None)
        return redirect(url_for('actuators.list_actuators'))
    return render_template('remove_actuator.html', actuators=actuators_dict)
