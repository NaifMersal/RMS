from django.urls import path
from . import views
urlpatterns = [
    path('refrences/', views.get_post_refrences ),
]
