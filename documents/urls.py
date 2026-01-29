from django.urls import path
from . import views

urlpatterns = [
    path('add_document/', views.get_add_document_form, name='add_document'),
    path('save_document/', views.add_document, name='save_document'),
]