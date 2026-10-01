from django.urls import path

from tweet import views

urlpatterns = [
    path("", views.index, name="index"),
]
