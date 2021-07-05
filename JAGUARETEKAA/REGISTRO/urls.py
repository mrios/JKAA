from django.urls import path, include
from . import views

app_name = "REGISTRO"

urlpatterns = [
    path('', views.registro, name="registro"),
]