"""

BackendApp URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from MyFamilyApp.backend.views import DashboardView

app_name="backend"

urlpatterns = [
    path('dashboard/',DashboardView.as_view(),name="dashboard"),
    path('person/create',DashboardView.as_view(),name="create_person"),
    path('person/edit/<pk>',DashboardView.as_view(),name="edit_person"),
    path('person/delete/<pk>',DashboardView.as_view(),name="delete_person"),
    path('person/delete',DashboardView.as_view(),name="suggestion_notifications")
]
