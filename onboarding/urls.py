from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('register-user/', views.RegisterUser.as_view(), name='registr-user'),
]