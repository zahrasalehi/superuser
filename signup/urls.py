from django.urls import path
from .views import custom_login_view, register

urlpatterns = [
    path('', custom_login_view, name='login'),
    path('register', register, name='register')]
