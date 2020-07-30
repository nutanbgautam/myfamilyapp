from django.shortcuts import render
from django.views.generic import *
from MyFamilyApp.backend.models import Person,Suggestions

app_name="backend"

'''Templates'''

person_create_template='backend/Person_Manipulation/create_person.html'
person_edit_template='backend/Person_Manipulation/edit_person.html'
person_delete_template='backend/Person_Manipulation/delete_person.html'
suggestions_table_template='backend/suggestions_table.html'
suggestion_detail_template='backend/suggestion_detail.html'
user_profile_template='backend/user_profile.html'

'''Templates END'''


'''Person Manipulation Views'''

class PersonCreateView(CreateView):
	model 				= Person
	template_name       = person_create_template

class PersonEditView(UpdateView):
	model 				= Person
	template_name       = person_edit_template

class PersonDeleteView(DeleteView):
	model 				= Person 
	template_name       = person_delete_template

'''Person Manipulation Views END'''

class SuggestionsListView(ListView):
	model 				= Suggestions
	template_name       = suggestions_table_template

class SuggestionDetailView(DetailView):
	model 				= Suggestions
	template_name       = suggestion_detail_template

class UserProfileView(View):
	template_name       = user_profile_template

def load_data_test(request):
	from MyFamilyApp.backend.data_processing_functions import old_methods 
	return redirect("/")