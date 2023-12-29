from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import MQTTData
from datetime import datetime, timedelta


def graph(request):
    return render(request, "graph1.html")

def get_data_daily(request):
    if request.method == 'GET':
        selected_date = request.GET.get('selected_date')
        labels = [f"{str(hour).zfill(2)}:00" for hour in range(24)]
        mqtt_data = MQTTData.objects.filter(timestamp__startswith=selected_date).order_by('timestamp')
        dataPoints = prepare_data_to_chart(mqtt_data)
        return JsonResponse(dataPoints, safe=False)

def get_data_weekly(request):
    if request.method == 'GET':
        selected_date = request.GET.get('selected_date')
        start_date = datetime.strptime(selected_date, '%Y-%m-%d')
        end_date = start_date + timedelta(days=6)
        labels = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        mqtt_data = MQTTData.objects.filter(timestamp__date__range=[start_date, end_date]).order_by('timestamp')
        dataPoints = prepare_data_to_chart(mqtt_data)
        return JsonResponse(dataPoints, safe=False)

def prepare_data_to_chart(mqtt_data):
    dataPoints = []
    for data in mqtt_data:
        dataPoints.append({
            "x": data.timestamp.timestamp() * 1000,
            "y_temperature": data.temperature,
            "y_current": data.current,
            "y_vibX": data.accelvibX,
            "y_vibY": data.accelvibY,
            "y_vibZ": data.accelvibZ,
        })
    return dataPoints
