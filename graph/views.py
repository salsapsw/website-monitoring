from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import MQTTData
import json
from datetime import datetime
from django.db.models import Avg
from django.db.models.functions import TruncHour


def graph(request):
    return render(request, "graph1.html")


def get_date_selection(request):
    get_all_datetime = MQTTData.objects.values_list("timestamp", flat=True)

    unique_date = set()

    for dt in get_all_datetime:
        unique_date.add(dt.date().strftime("%d-%m-%Y"))

    unique_date = list(unique_date)
    unique_date.sort()

    return JsonResponse({"dates": unique_date})


def post_selected_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            checked_value = data.get("checkedValue")
            selected_date = data.get("selectedDate")
            if checked_value and selected_date:
                result = get_data_to_show(checked_value, selected_date)
            else:
                result = None
            # Return a JSON response with the list of values
            response_data = {"message": "Data received successfully", "avg_data": result}
            return JsonResponse(response_data, status=200)
        except Exception as e:
            error_message = str(e)
            return JsonResponse({"error": error_message}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_data_to_show(checked_value, selected_date):
    target_date = datetime.strptime(selected_date, "%d-%m-%Y").date()
    labels = [
        "00:00",
        "01:00",
        "02:00",
        "03:00",
        "04:00",
        "05:00",
        "06:00",
        "07:00",
        "08:00",
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
        "23:00",
    ]

    try:
        # Get all data in the selected date
        result = (
            MQTTData.objects.filter(
                timestamp__startswith=target_date
            )  # filter all data by selected date
            .annotate(
                group_by_hour=TruncHour("timestamp")
            )  # group all data hourly and make a new key called 'group_by_hour'
            .values("group_by_hour")  # get the data from new key
            .annotate(
                average_value_per_hour=Avg(checked_value)
            )  # make a new key 'average_value_per_hour' and take average all values in that hour
            .order_by("group_by_hour")
        )
        # Create a dictionary to store avg values with group_by_hour as keys
        avg_dict = {
            item["group_by_hour"].strftime("%H:%M"): item["average_value_per_hour"]
            for item in result
        }

        # Create the final list with None for missing hours
        result = [avg_dict.get(label, None) for label in labels]

    except Exception as e:
        result = None
        print(e)

    return result
