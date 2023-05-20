from django.contrib import admin
from django.urls import path, include
from campaign_manager import views

urlpatterns = [
    path("", views.add_subscriber, name='campaign_manager')
    
]