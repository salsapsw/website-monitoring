from django.urls import path, include
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("get-dashboard-data/", views.get_dashboard_data, name="get_dashboard_data"),
    path("get-data-minutes/", views.get_data_minutes, name="get_data_minutes"),
    path("setting/", include("setting.urls")),
]
