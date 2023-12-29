from django.urls import path
from . import views

app_name = "profil_app"

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    
]
