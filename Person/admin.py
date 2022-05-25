from django.contrib import admin
from .models import Person, PersonHealth

# Register your models here.

admin.site.register(Person)
admin.site.register(PersonHealth)