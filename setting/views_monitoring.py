"""
Module: monitoring.views

This module contains Django view functions related to the monitoring functionality.

Functions:
- monitoring(request): Renders the monitoring page.
- get_monitoring_data(request): Retrieves monitoring-related data from the database and returns it as a JSON response.
- update_monitoring_data(request): Handles updating monitoring-related data in the database based on POST requests.
- save_to_database(data): Updates monitoring-related data in the database based on input JSON data.
- manual_monitoring(switches): Performs manual monitoring control based on the provided switch settings.
"""
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import (
    MonitoringUpperAndLower,
)

# Create your views here.


def monitoring(request):
    """
    Renders the monitoring page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered monitoring page.
    """
    return render(request, "monitoring.html")


def get_monitoring_data(request):
    """
    Retrieves monitoring-related data from the database and returns it as a JSON response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response containing monitoring-related data.
    """
    # Get the last row in the SettingMode database (eventhough there is only one row of data :D)

    # Get all row in the monitoringTargetAndTolerance, monitoringSwitches, and WateringSchedule database
    upper_and_lower = MonitoringUpperAndLower.objects.order_by("pk")[0]

    context = {
        "upperAndLower": {
            "vibration-upper": upper_and_lower.vibration_upper,
            "vibration-lower": upper_and_lower.vibration_lower,
            "current-upper": upper_and_lower.current_upper,
            "current-lower": upper_and_lower.current_lower,
            "temperature-upper": upper_and_lower.temperature_upper,
            "temperature-lower": upper_and_lower.temperature_lower,
        },
    }
    return JsonResponse(context)


def update_monitoring_data(request):
    """
    Handles updating monitoring-related data in the database based on POST requests.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response confirming the update.
    """
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
