from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from MyFamilyApp.backend.models import Person,Suggestions

app_name="frontend"

'''Templates'''

dashboard_template='frontend/dashboard.html'
peoples_table_template='frontend/peoples_table.html'
person_detail_template='frontend/person_detail.html'
suggestion_create_template='frontend/create_suggestion.html'

'''Templates END'''

class DashboardView(TemplateView):
	template_name		= dashboard_template

class PersonListView(ListView):
    model               = Person
    queryset            = Person.objects.filter(same_vamsha=True)
    template_name       = peoples_table_template
    context_object_name = 'persons'
    paginate_by         = 20

class PersonDetailView(DetailView):
	model 				= Person
	template_name       = person_detail_template

class SearchView(View):
	pass

class SuggestionCreateView(CreateView):
	model 				= Suggestions
	template_name		= suggestion_create_template



