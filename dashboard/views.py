from django.shortcuts import render
from dashboard.models import MQTTData
from django.http import HttpResponse,JsonResponse
from .mqtt_utils import subscribe_to_hivemq, publish_to_hivemq, mqtt_data
import threading
from datetime import date, timedelta
from django.db.models import Avg
from django.db.models.functions import TruncMinute


# Create your views here.
def start_hivemq_subscription(request):
    subscribe_thread = threading.Thread(target=subscribe_to_hivemq)
    subscribe_thread.start()
    return HttpResponse("HiveMQ subscription started successfully")

def dashboard(request):
    return render(request, 'dashboard.html')

# def get_status(request):
#     status = "Server is online" if mqtt_data.data['current'] != 0 else "Server is offline"
#     response_data = {'status': status}
#     return JsonResponse(response_data)


def get_dashboard_data(request):
    
    subscribe_thread = threading.Thread(target=subscribe_to_hivemq)
    subscribe_thread.start()
    
    data_sensor = MQTTData.objects.order_by("-pk")[0]
    # if data_sensor.current > 0.1:
    #     # Jika 'current' melebihi 1.0, maka kirim pesan 'warning'
    #     publish_message(request)
    # # print(data_sensor.temperature, data_sensor.current)
    sensorValue = {
        "currentValue" : data_sensor.current,
        "temperatureValue" : data_sensor.temperature,
        "vibrationValue" : data_sensor.vibration,
    }
    # print(sensorValue)
    return JsonResponse(sensorValue)

def publish_message(request):
    # Panggil fungsi publish_to_hivemq dengan parameter yang sesuai
    publish_to_hivemq('warning', 'warning')
    return HttpResponse("warning")

def get_data_minutes(request):
    today = date.today()
    data_for_last_7_days = {
        'labels': [],  # Label tanggal
        'online': [],  # Data online
        'offline': [],  # Data offline
    }

    for i in range(7):
        day = today - timedelta(days=i)
        data_day = MQTTData.objects.filter(timestamp__date=day)
        minutes = data_day.annotate(group_by_minutes=TruncMinute("timestamp"))
        average = minutes.values("group_by_minutes").annotate(avg=Avg("current"))
        avg_list = [data for data in average if data['avg'] > 0.0]
        online_minutes = len(avg_list)
        offline_minutes = 1440 - online_minutes

        data_for_last_7_days['labels'].append(day.strftime("%Y-%m-%d"))
        data_for_last_7_days['online'].append(online_minutes)
        data_for_last_7_days['offline'].append(offline_minutes)

    return JsonResponse(data_for_last_7_days)
