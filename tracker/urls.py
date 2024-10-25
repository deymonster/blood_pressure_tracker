from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_record, name='create_record'),
    path('last/', views.last_record, name='last_record'),
    path('statistics/', views.statistics, name='statistics'),
]