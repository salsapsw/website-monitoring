from django.urls import path, include
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("get-dashboard-data/", views.get_dashboard_data,
         name="get_dashboard_data"),
    path("get-status/", views.get_status, name="get_status"),

    path("setting/", include("setting.urls")),
    path("graph/", include("graph.urls")),
    path("user/", include("user.urls")),
]
