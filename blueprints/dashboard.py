import json

from flask import Blueprint, jsonify, render_template, request, url_for

import config

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_bp.route('/home')
def home():
    return render_template('home.html')

@dashboard_bp.route('/realtime')
def realtime():
    return render_template('realtime.html')

@dashboard_bp.route('/control')
def control():
    return render_template('control.html')

@dashboard_bp.route('/api/servo', methods=['POST'])
def servo_control():
    from app import mqtt_client
    data = request.get_json()
    angle = data.get('angle')
    mqtt_client.publish(config.TOPIC_ACTUATOR_SERVO, angle)
    return jsonify({'status': 'ok', 'angle': angle})

@dashboard_bp.route('/api/buzzer', methods=['POST'])
def buzzer_control():
    from app import mqtt_client
    data = request.get_json()
    freq = data.get('frequency')
    vol  = data.get('volume')
    payload = json.dumps({'frequency': freq, 'volume': vol})
    mqtt_client.publish(config.TOPIC_ACTUATOR_BUZZER, payload)
    return jsonify({'status': 'ok', 'payload': payload})
