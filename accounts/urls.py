from django.urls import path
from . import views

urlpatterns = [
    path('login_client/', views.client_login, name='login_client'),
    path('register_client/', views.client_register, name='register_client'),
    path('client_login/', views.get_client_login, name='client_login'),
    path('client_register', views.get_client_register, name='client_register'),
    path('client_dashboard', views.get_client_dashboard, name='client_dashboard'),
    path('client_profile', views.get_client_profile, name='client_profile'),
    path('client_documents', views.get_client_documents, name='client_documents'),
    path('client_logout/', views.get_client_logout, name='client_logout'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin', views.logout_admin, name='logout_admin'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('admin_register/', views.get_admin_register, name='admin_register'),
    path('admin_login/', views.get_admin_login, name='admin_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]