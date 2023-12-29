# from apscheduler.schedulers.background import BackgroundScheduler
import paho.mqtt.client as mqtt
from dashboard.models import MQTTData
from setting.models import MonitoringUpperAndLower

# Define the MQTT parameters
username = "RamaPMPD"
password = "Kerasakti123"
host = "b5208bedc9794c2397ead6f7870bb494.s1.eu.hivemq.cloud"
port = 8883
topic = "dataSensor"

# Create an MQTT client
client = mqtt.Client()

# Set the username and password
client.username_pw_set(username, password)

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {str(message.payload)}")
    save_to_database(payload=message.payload.decode())
    warning_check()

# Set the callback function
client.on_message = on_message

# Connect to the MQTT broker
client.tls_set()
client.connect(host, port)

# Subscribe to the topic
client.subscribe(topic)

def save_to_database(payload):
    data = payload.split(' ')
    mqtt_data = MQTTData(
            temperature=data[0],
            current=data[1],
            accelvibX=data[2],
            accelvibY=data[3],
            accelvibZ=data[4],
            
         )
    mqtt_data.save()
    
def warning_check():
    data_sensor = MQTTData.objects.order_by("-pk")[0]
    treshold = MonitoringUpperAndLower.objects.order_by("-pk")[0]
    
    warning_check = "warning"
    
    if not treshold.temperature_lower <= data_sensor.temperature <= treshold.temperature_upper:
        warning_check = "warning_temperature"
        client.publish(warning_check, "warning")
    if not treshold.current_lower <= data_sensor.current <= treshold.current_upper:
        warning_check = "warning_current"
        client.publish(warning_check, "warning")
    if not treshold.vibration_X_lower<= data_sensor.accelvibX <= treshold.vibration_X_upper:
        warning_check = "warning_vibration"
        client.publish(warning_check, "warning")
    if not treshold.vibration_Y_lower<= data_sensor.accelvibY <= treshold.vibration_Y_upper:
        warning_check = "warning_vibration"
        client.publish(warning_check, "warning")
    if not treshold.vibration_Z_lower<= data_sensor.accelvibZ <= treshold.vibration_Z_upper:
        warning_check = "warning_vibration"
        client.publish(warning_check, "warning")
        
def start(register):
    if register:
        return
    print ("hello world!!!")
    client.loop_start()
    
def stop():
    print("stopd")
    client.loop_stop()