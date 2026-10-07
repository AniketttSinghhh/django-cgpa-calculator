from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_cgpa, name='calculate_cgpa'),
]