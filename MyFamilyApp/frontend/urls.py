"""

FrontendApp URL Configuration

"""
from django.urls import path
from MyFamilyApp.frontend.views import *

app_name="frontend"

urlpatterns = [
    path('',PersonListView.as_view(),name="peoples_table"),
    path('dashboard/',DashboardView.as_view(),name="dashboard"),
    path('person/<pk>',PersonDetailView.as_view(),name="person_detail"),
    path('tree',PersonTreeView.as_view(),name="person_tree"),
    path('search/',SearchView.as_view(),name="search_person"),
    path('suggest/<pk>',SuggestionCreateView.as_view(),name="suggest_person")
]
