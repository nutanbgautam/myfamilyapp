from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from MyFamilyApp.backend.models import Person


class DashboardView(ListView):
    model               = Person
    template_name       = "backend/index.html"
    context_object_name = 'persons'