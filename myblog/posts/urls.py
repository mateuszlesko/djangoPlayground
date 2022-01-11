from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"
urlpatterns = [
    path("",views.index,name="index"),
    path('error404',views.error404,name="404"),
    path("details/<int:id>",views.details,name="details"),
    path("create",views.create,name="create"),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:id>',views.delete,name="delete"),
    path('403',views.error403,name="403"),
]