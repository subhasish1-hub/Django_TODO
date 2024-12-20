from django.urls import path
from .views import register, login_view, logout_view,profile

urlpatterns = [
    path("register/", register, name="register"),     # Path for registration
    path("login/", login_view, name="login"),         # Path for login
    path("logout/", logout_view, name="logout"),      # Path for logout
    path("profile/", profile, name="profile"),
]
