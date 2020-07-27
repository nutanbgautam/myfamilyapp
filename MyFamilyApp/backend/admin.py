from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
# from MyFamilyApp.backend.models import User

# admin.site.register(User,UserAdmin)

models=apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

