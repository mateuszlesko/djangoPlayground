from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("",views.index,name="index"),
    path("details/<int:id>",views.details,name="details"),
    path("create",views.create,name="create"),
]