
from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('log-in', auth_views.obtain_auth_token),
    path('register', views.regster),
]
