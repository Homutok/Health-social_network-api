from django.contrib import admin
from .models import Person, PersonHealth, PersonPhoto

# Register your models here.

admin.site.register(Person)
admin.site.register(PersonHealth)
admin.site.register(PersonPhoto)
