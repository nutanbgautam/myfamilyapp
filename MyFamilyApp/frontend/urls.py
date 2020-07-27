"""

FrontendApp URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from MyFamilyApp.frontend.views import PersonListView

app_name="frontend"

urlpatterns = [
    path('',PersonListView.as_view(),name="peoples_table"),
    path('sdf',PersonListView.as_view(),name="search_people"),
]
