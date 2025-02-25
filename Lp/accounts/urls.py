from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('users/', views.admin_user_list, name='admin_user_list'),
    path('users/<int:pk>/edit/', views.admin_user_edit, name='admin_user_edit'),
]
