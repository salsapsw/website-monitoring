from django.urls import path
from . import views

app_name = "graph_app"

urlpatterns = [
    path("",views.graph , name="graph"),

    path("graph/", views.graph , name="graph2"),
    path("get-data-daily/", views.get_data_daily, name="get-data-daily"),
    path("get-data-weekly/", views.get_data_weekly, name="get-data-weekly"),
]
