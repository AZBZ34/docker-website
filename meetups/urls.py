from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index),
    path('', views.index), # our-domain.com/meetups
]
