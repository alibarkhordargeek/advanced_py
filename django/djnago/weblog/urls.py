from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.mp, name = 'mainpage')
]