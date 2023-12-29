from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import (
    MonitoringUpperAndLower,
)
import paho.mqtt.client as mqtt
import ssl

client = mqtt.Client()

# Konfigurasi TLS jika diperlukan (pastikan Anda memiliki sertifikat TLS)
sslContext = ssl.create_default_context()
client.tls_set_context(sslContext)

# Konfigurasi otentikasi jika diperlukan (ganti dengan informasi otentikasi Anda)
client.username_pw_set(username="RamaPMPD", password="Kerasakti123")

# Hubungkan ke broker HiveMQ (ganti dengan alamat host dan port HiveMQ yang sesuai)
client.connect("b5208bedc9794c2397ead6f7870bb494.s1.eu.hivemq.cloud", port=8883)

# Create your views here.


def monitoring(request):
    return render(request, "monitoring.html")


def get_monitoring_data(request):
    upper_and_lower = MonitoringUpperAndLower.objects.order_by("pk")[0]

    context = {
        "upperAndLower": {
            "vibration-X-upper": upper_and_lower.vibration_X_upper,
            "vibration-X-lower": upper_and_lower.vibration_X_lower,
            "vibration-Y-upper": upper_and_lower.vibration_Y_upper,
            "vibration-Y-lower": upper_and_lower.vibration_Y_lower,
            "vibration-Z-upper": upper_and_lower.vibration_Z_upper,
            "vibration-Z-lower": upper_and_lower.vibration_Z_lower,
            "current-upper": upper_and_lower.current_upper,
            "current-lower": upper_and_lower.current_lower,
            "temperature-upper": upper_and_lower.temperature_upper,
            "temperature-lower": upper_and_lower.temperature_lower,
            "cal-vib-x": upper_and_lower.cal_vibration_X,
            "cal-vib-y": upper_and_lower.cal_vibration_Y,
            "cal-vib-z": upper_and_lower.cal_vibration_Z,
        },
    }
    return JsonResponse(context)


def update_monitoring_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            save_to_database(data)
            return JsonResponse({"message": "Data updated successfully"})
        except json.JSONDecodeError:
            # Return an error response if the JSON data is not valid
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        # Return an error response if the request method is not POST
        return HttpResponse(status=405)


# Save data to database
def save_to_database(data):
    """
    Updates monitoring-related data in the database based on input JSON data.

    Parameters:
        data (dict): JSON data containing monitoring-related settings.

    Returns:
        None
    """

    # Get all row in the MonitoringUpperAndLower database
    upper_and_lower = MonitoringUpperAndLower.objects.order_by("pk")[0]
    try:
        for key, value in data.get("upperAndLower").items():
            setattr(upper_and_lower, key, value)
        upper_and_lower.save()
    except:
        print("Error saving data!")


def update_calibrations(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            client.publish(topic="offset_x", payload=data["calibration"]["cal_vibration_X"])
            client.publish(topic="offset_y", payload=data["calibration"]["cal_vibration_Y"])
            client.publish(topic="offset_z", payload=data["calibration"]["cal_vibration_Z"])
            update_calibrations_in_database(data)
            print(data)
            return JsonResponse({"message": "Calibrations updated successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return HttpResponse(status=405)

def update_calibrations_in_database(data):
    upper_and_lower = MonitoringUpperAndLower.objects.order_by("pk")[0]
    try:
        upper_and_lower.cal_vibration_X = data["calibration"]["cal_vibration_X"]
        upper_and_lower.cal_vibration_Y = data["calibration"]["cal_vibration_Y"]
        upper_and_lower.cal_vibration_Z = data["calibration"]["cal_vibration_Z"]
        upper_and_lower.save()
    except Exception as e:
        print(f"Error updating calibrations: {e}")