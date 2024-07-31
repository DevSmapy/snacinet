from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name="main"),
    path("login/", views.login_page_view, name="login_page"),
    path("register/", views.register_page_view, name="register"),
    path("api/register/", views.register_view, name="register_api"),
    path("api/login/", views.login_view, name="login"),
]