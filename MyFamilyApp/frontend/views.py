from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from MyFamilyApp.backend.models import Person

'''Templates'''

peoples_table_template='frontend/peoples_table.html'

'''Templates END'''

class PersonListView(ListView):
    model               = Person
    queryset            = Person.objects.filter(same_vamsha=True)
    template_name       = peoples_table_template
    context_object_name = 'persons'
    paginate_by         = 20


