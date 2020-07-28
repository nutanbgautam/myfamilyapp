from django.shortcuts import render,redirect
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
	'''Filter data according to given parameters'''
	def get(self,request,*args,**kwargs):
		foundPersons=[]
		givenTerm=request.GET.get('givenTerm')
		searchBy=request.GET.get('searchBy')
		if searchBy=='serial_number':
			'''Search By Serial Number'''
			try:
				givenSN=int(givenTerm)
				a=Person.objects.filter(person_id=givenSN)
				foundPersons=[person for person in a]
			except:pass
		elif searchBy=='batch_no':
			'''Search By batch no'''
			try:
				givenBatchNo=int(givenTerm)
				foundPersons=[person for person in Person.objects.filter(batch_no=givenBatchNo)]
			except:pass
		else:pass
		return render(request,peoples_table_template,{"persons":foundPersons})

	def post(self,request,*args,**kwargs):
		foundPersons=[]
		givenTerm=request.POST.get('givenTerm')
		searchBy=request.POST.get('searchBy')
		if searchBy=='serial_number':
			'''Search By Serial Number'''
			try:
				givenSN=int(givenTerm)
				a=Person.objects.filter(person_id=givenSN)
				foundPersons=[person for person in a]
			except:pass
		elif searchBy=='name':
			'''Search By Name'''
			try:
				import nepali_roman as nr
				foundPersons=[person for person in Person.objects.all() if givenTerm.lower() in nr.romanize_text(person.full_name).lower()]
			except:pass
		elif searchBy=='batch_no':
			'''Search By batch no'''
			try:
				givenBatchNo=int(givenTerm)
				foundPersons=[person for person in Person.objects.filter(batch_no=givenBatchNo)]
			except:pass
		elif searchBy=='phone_number':
			'''Search By phone_number'''
			try:
				foundPersons=[person for person in Person.objects.all() if givenTerm in person.contact_number]
			except:pass
		elif searchBy=='father':
			'''Search By Father Name'''
			try:
				import nepali_roman as nr
				foundPersons=[person for person in Person.objects.all() if person.father!=None]
				foundPersons=[person for person in foundPersons if givenTerm.lower() in nr.romanize_text(person.father.full_name).lower()]
			except:pass
		elif searchBy=='grandfather':
			'''Search By Grandfather Name'''
			try:
				import nepali_roman as nr
				foundPersons=[]
				for person in Person.objects.all():
					try:
						if givenTerm.lower()==nr.romanize_text(person.father.father.full_name).lower():
							foundPersons.append(person)
					except:pass
			except:pass

		return render(request,peoples_table_template,{"persons":foundPersons})

class SuggestionCreateView(CreateView):
	model 				= Suggestions
	template_name		= suggestion_create_template



