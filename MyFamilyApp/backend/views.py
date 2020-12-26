from django.shortcuts import render,redirect
from django.views.generic import *
from MyFamilyApp.backend.models import Person

app_name="backend"

'''Templates'''

person_create_template='backend/Person_Manupulation/create_person.html'
person_edit_template='backend/Person_Manupulation/edit_person.html'
person_delete_template='backend/Person_Manupulation/delete_person.html'
suggestions_table_template='backend/suggestions_table.html'
suggestion_detail_template='backend/suggestion_detail.html'
user_profile_template='backend/user_profile.html'

'''Templates END'''


'''Person Manupulation Views'''

class PersonCreateView(CreateView):
	model 				= Person
	template_name       = person_create_template

class PersonEditView(UpdateView):
	model 				= Person
	template_name       = person_edit_template
	fields 				= '__all__'

class PersonDeleteView(DeleteView):
	model 				= Person 
	template_name       = person_delete_template

'''Person Manupulation Views END'''

class SuggestionsListView(ListView):
	model 				= Person
	template_name       = suggestions_table_template

class SuggestionDetailView(DetailView):
	model 				= Person
	template_name       = suggestion_detail_template

class UserProfileView(View):
	template_name       = user_profile_template

def load_data_test(request):
	from MyFamilyApp.backend.data_processing_functions import old_methods
	print("Sucessfull")
	return redirect("/")