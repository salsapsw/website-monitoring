from django.urls import path, include
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("get-dashboard-data/", views.get_dashboard_data, name="get_dashboard_data"),
    path("get-data-minutes/", views.get_data_minutes, name="get_data_minutes"),
    path("get-data-online-offline/", views.get_data_online_offline, name="get_data_online_offline"),
    path('get-data-online-offline-week/', views.get_data_online_offline_week, name='get_data_online_offline_week'),
    path("setting/", include("setting.urls")),
    path("user/", include("user.urls")),
]
