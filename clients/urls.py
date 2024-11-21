from django.urls import path
from . import views

urlpatterns = [
    path('all_clients/', views.clients, name='clients'),
    path('clients/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
]