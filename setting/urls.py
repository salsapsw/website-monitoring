from django.urls import path, include
from . import views_monitoring, views_members

app_name = "setting_app"

urlpatterns = [
    path("monitoring/", views_monitoring.monitoring, name="monitoring"),
    path("monitoring/get-monitoring-data/",
         views_monitoring.get_monitoring_data, name="get-monitoring-data"),
    path("monitoring/post-monitoring-data/",
         views_monitoring.update_monitoring_data, name="update-monitoring-data"),

    path("members/", views_members.members, name="members")

]
