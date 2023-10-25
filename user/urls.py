from django.urls import path
from . import views_login, views_profile

app_name = "user_app"

urlpatterns = [
    path("login/", views_login.login, name="login"),
    path("profile/", views_profile.profile, name="profile")
]
