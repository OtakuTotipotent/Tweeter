from django.urls import include, path

from .views import register

urlpatterns = [
    path(
        "",
        include("django.contrib.auth.urls"),
        # This handles all of the three LOGIN, LOGOUT, & REGISTER
    ),
    path(
        "register/",
        register,
        name="register",
    ),
]
