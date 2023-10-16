from django.shortcuts import render
import paho.mqtt.client as mqtt
from dashboard.models import MQTTData
from setting.models import MonitoringUpperAndLower
from django.http import HttpResponse,JsonResponse
from .mqtt_utils import subscribe_to_hivemq, publish_to_hivemq, mqtt_data, subs_baru
import threading
import time

# Create your views here.
def start_hivemq_subscription(request):
    subscribe_thread = threading.Thread(target=subscribe_to_hivemq)
    subscribe_thread.start()
    return HttpResponse("HiveMQ subscription started successfully")

def subscription(request):
    subscribe_thread = threading.Thread(target=subs_baru)
    subscribe_thread.start()
    return HttpResponse("HiveMQ subscription started successfully")

def dashboard(request):
    return render(request, 'dashboard.html')

def get_status(request):
    status = "Server is offline" if mqtt_data.data['current'] == 0 else "Server is online"
    response_data = {'status': status}
    return JsonResponse(response_data)


def get_dashboard_data(request):
    
    # subscribe_thread = threading.Thread(target=subscribe_to_hivemq)
    # subscribe_thread.start()
    subs_baru()
    
    data_sensor = MQTTData.objects.order_by("-pk")[0]
    treshold = MonitoringUpperAndLower.objects.order_by("-pk")[0]
    # print(data_sensor.temperature, data_sensor.current)
    sensorValue = {
        "currentValue" : data_sensor.current,
        "temperatureValue" : data_sensor.temperature,
        "vibrationValue" : data_sensor.vibration,
    }
    warningCondition = (
        {
            "warningTemperature" : not treshold.temperature_lower <= data_sensor.temperature <= treshold.temperature_upper,
            "warningCurrent" : not treshold.current_lower <= data_sensor.current <= treshold.current_upper,
            "warningVibration" : not treshold.vibration_lower <= data_sensor.vibration <= treshold.vibration_upper,
        }
    )
    context = {"sensorValue": sensorValue, "warningCondition": warningCondition}
    if any(warningCondition.values()):
        publish_message(warningCondition)
        time.sleep(.15)
        # client = mqtt.Client
        # client.loop_stop(self)
    return JsonResponse(context)

def publish_message(warningCondition):
    # Kirim pesan dengan topik yang sesuai ke broker MQTT
    publish_to_hivemq('warning', 'warning')
    return HttpResponse('haha')

