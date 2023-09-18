"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('logout_user/', views.logout_view, name='logout'),
    path('login_user/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('register_user/', views.register, name='register'),
]
