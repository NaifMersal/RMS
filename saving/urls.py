from django.urls import path
from . import views

urlpatterns = [
    path('refrences/', views.CURD_refrences ),
]
