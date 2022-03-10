from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('request-list/', views.Request.as_view(), name='request_list'),
    path('request-details/<int:requestId>', views.RequestDetail.as_view(), name='request_details')
]