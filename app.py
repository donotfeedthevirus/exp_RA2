from flask import Flask, jsonify
from flask_mqtt import Mqtt
import config

from blueprints.actuators import actuators_bp
from blueprints.auth import auth_bp
from blueprints.dashboard import dashboard_bp
from blueprints.sensors import sensors_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(config)

mqtt_client = Mqtt(app)

sensor_data = {"dht": None, "mq2": None}
actuator_state = {"servo": None, "buzzer": None}

app.register_blueprint(auth_bp)
app.register_blueprint(sensors_bp, url_prefix="/sensors")
app.register_blueprint(actuators_bp, url_prefix="/actuators")
app.register_blueprint(dashboard_bp)


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT broker connected, subscribing to sensor topics")
        mqtt_client.subscribe(config.TOPIC_SENSOR_DHT)
        mqtt_client.subscribe(config.TOPIC_SENSOR_MQ2)
        print(f"Subscribed to {config.TOPIC_SENSOR_DHT} and {config.TOPIC_SENSOR_MQ2}")
    else:
        print("MQTT connect failed:", rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"MQTT message received: {topic} -> {payload}")
    if topic == config.TOPIC_SENSOR_DHT:
        sensor_data["dht"] = payload
    elif topic == config.TOPIC_SENSOR_MQ2:
        sensor_data["mq2"] = payload


@app.route("/api/sensors")
def api_sensors():
    return jsonify(sensor_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
