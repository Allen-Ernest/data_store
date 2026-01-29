from django.urls import path
from . import views

urlpatterns = [
    path('all_departments', views.all_departments, name='all_departments'),
    path('add_department', views.add_department, name='add_department'),
]