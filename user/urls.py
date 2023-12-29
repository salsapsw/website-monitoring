from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path("", views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('reset-password/', views.reset_password, name='reset_password'),
    
]
