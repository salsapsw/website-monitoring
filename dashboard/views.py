from django.shortcuts import render
from dashboard.models import MQTTData
from setting.models import MonitoringUpperAndLower
from django.http import HttpResponse, JsonResponse
from .mqtt_utils import publish_to_hivemq, subs_baru
import threading
from datetime import date, timedelta
from django.db.models import Avg
from django.db.models.functions import TruncMinute
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import Group


# Create your views here.

@login_required
def dashboard(request):
    
    test_group = Group.objects.get(name='admin')
    user_group = request.user.groups.all()
    
    template_name = None
    if test_group in user_group:
        template_name = 'dashboard.html'
    else:
        template_name = 'dashboard_staff.html'
    
    return render(request, template_name)


@login_required
def get_dashboard_data(request):
    data_sensor = MQTTData.objects.order_by("-pk")[0]
    treshold = MonitoringUpperAndLower.objects.order_by("-pk")[0]
    last_time_data = data_sensor.timestamp
    now_date = datetime.now()
    seconds = (now_date - last_time_data).total_seconds()
    if seconds > 10 :
        sensorValue = {
            "currentValue" : "-",
            "temperatureValue" : "-",
            "accelvibXValue" : "-",
            "accelvibYValue" : "-",
            "accelvibZValue" : "-",
        }
        context = { "sensorValue" : sensorValue, "warningCondition": None}
        return JsonResponse(context)
    
    sensorValue = {
        "currentValue" : data_sensor.current,
        "temperatureValue" : data_sensor.temperature,
        "accelvibXValue" : data_sensor.accelvibX,
        "accelvibYValue" : data_sensor.accelvibY,
        "accelvibZValue" : data_sensor.accelvibZ
    }
    warningCondition = (
        {
            "warningTemperature": not treshold.temperature_lower <= data_sensor.temperature <= treshold.temperature_upper,
            "warningCurrent" : not treshold.current_lower <= data_sensor.current <= treshold.current_upper,
            "warningaccelvibx" : not treshold.vibration_X_lower <= data_sensor.accelvibX <= treshold.vibration_X_upper,
            "warningaccelviby" : not treshold.vibration_Y_lower <= data_sensor.accelvibY <= treshold.vibration_Y_upper,
            "warningaccelvibz" : not treshold.vibration_Z_lower <= data_sensor.accelvibZ <= treshold.vibration_Z_upper,
        }
    )
    context = {"sensorValue" : sensorValue, "warningCondition" : warningCondition}
    return JsonResponse(context)

@login_required
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
        average = minutes.values(
            "group_by_minutes").annotate(avg=Avg("current"))
        avg_list = [data for data in average if data['avg'] > 0.0]
        online_minutes = len(avg_list)
        offline_minutes = 1440 - online_minutes

        data_for_last_7_days['labels'].append(day.strftime("%Y-%m-%d"))
        data_for_last_7_days['online'].append(online_minutes)
        data_for_last_7_days['offline'].append(offline_minutes)

    return JsonResponse(data_for_last_7_days)

@login_required
def get_data_online_offline(request):
    today = date.today()

    data_day = MQTTData.objects.filter(timestamp__date=today)
    minutes = data_day.annotate(group_by_minutes=TruncMinute("timestamp"))
    average = minutes.values("group_by_minutes").annotate(avg=Avg("current"))
    avg_list = [data for data in average if data['avg'] > 0.0]
    online_minutes = len(avg_list)
    offline_minutes = 1440 - online_minutes

    online_hours, online_minutes = divmod(online_minutes, 60)
    offline_hours, offline_minutes = divmod(offline_minutes, 60)

    response_data = {
        'total_waktu_online_hours': online_hours,
        'total_waktu_online_minutes': online_minutes,
        'total_waktu_offline_hours': offline_hours,
        'total_waktu_offline_minutes': offline_minutes,
    }

    # print(f"online {online_hours} hours {online_minutes} minutes")
    # print(f"offline {offline_hours} hours {offline_minutes} minutes")

    return JsonResponse(response_data)

@login_required
def get_data_online_offline_week(request):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    data_week = MQTTData.objects.filter(
        timestamp__date__range=[start_of_week, end_of_week])
    minutes = data_week.annotate(group_by_minutes=TruncMinute("timestamp"))
    average = minutes.values("group_by_minutes").annotate(avg=Avg("current"))
    avg_list = [data for data in average if data['avg'] > 0.0]
    online_minutes = len(avg_list)
    offline_minutes = 7 * 24 * 60 - online_minutes  # total menit dalam 1 minggu

    online_hours, online_minutes = divmod(online_minutes, 60)
    offline_hours, offline_minutes = divmod(offline_minutes, 60)

    data = {
        'total_waktu_online_hours': online_hours,
        'total_waktu_online_minutes': online_minutes,
        'total_waktu_offline_hours': offline_hours,
        'total_waktu_offline_minutes': offline_minutes,
    }

    return JsonResponse(data)

