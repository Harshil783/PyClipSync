from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]