from django.urls import path, include
from . import views_monitoring, views_members, views_addmembers

app_name = "setting_app"

urlpatterns = [
    path("monitoring/", views_monitoring.monitoring, name="monitoring"),
    path("monitoring/get-monitoring-data/",
         views_monitoring.get_monitoring_data, name="get-monitoring-data"),
    path("monitoring/post-monitoring-data/",
         views_monitoring.update_monitoring_data, name="update-monitoring-data"),
    path("monitoring/post-calibrasi/", views_monitoring.update_calibrations, name="calibrasi-update"),

    path("members/", views_members.members, name="members"),
    path('add_group/<int:user_id>/', views_members.add_group, name='add_group'),
    path('edit_role/<int:user_id>/', views_members.edit_role, name='edit_role'),
    
    path("addmembers/", views_members.addmembers, name="addmembers"),
    
    path("addmembers/", views_addmembers.addmembers, name="addmembers"),
    path('delete_member/<int:user_id>/', views_members.delete_member, name='delete_member'),

]
