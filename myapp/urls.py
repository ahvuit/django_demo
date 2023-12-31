from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.user, name='users'),
    path('users/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('login/', views.login, name='login'),
]