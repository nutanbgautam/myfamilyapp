"""

BackendApp URL Configuration

"""
from django.urls import path
from MyFamilyApp.backend.views import *

app_name="backend"

urlpatterns = [
    path('person/create',PersonCreateView.as_view(),name="create_person"),
    path('person/edit/<pk>',PersonEditView.as_view(),name="edit_person"),
    path('person/delete/<pk>',PersonDeleteView.as_view(),name="delete_person"),
    path('suggestions/',SuggestionsListView.as_view(),name="suggestion_notifications"),
    path('suggestions/<pk>',SuggestionDetailView.as_view(),name="suggestion_detail"),
    path('profile/',UserProfileView.as_view(),name="user_profile"),
    path('load/',load_data_test)
]
