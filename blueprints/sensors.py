from flask import Blueprint, render_template, request, redirect, url_for

sensors_bp = Blueprint('sensors', __name__, template_folder='templates')
sensors_dict = {}

@sensors_bp.route('/')
def list_sensors():
    return render_template('sensors.html', sensors=sensors_dict)

@sensors_bp.route('/register', methods=['GET', 'POST'])
def register_sensor():
    if request.method == 'POST':
        name  = request.form['sensor']
        value = request.form.get('value', 0)
        sensors_dict[name] = value
        return redirect(url_for('sensors.list_sensors'))
    return render_template('register_sensor.html')

@sensors_bp.route('/delete', methods=['GET', 'POST'])
def delete_sensor():
    if request.method == 'POST':
        name = request.form['sensor']
        sensors_dict.pop(name, None)
        return redirect(url_for('sensors.list_sensors'))
    return render_template('remove_sensor.html', sensors=sensors_dict)
