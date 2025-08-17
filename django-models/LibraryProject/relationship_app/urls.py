from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration
    path("register/", views.register, name="register"),

    # Login (built-in)
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # Logout (built-in)
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
