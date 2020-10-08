from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.authentication, name='auth'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]