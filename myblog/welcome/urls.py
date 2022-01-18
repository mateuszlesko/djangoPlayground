from django.urls import path
from . import views

app_name = "welcome"
urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.mylogin,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.logout,name="logout"),
    path("changePassword",views.changePassword,name="changePassword"),
]