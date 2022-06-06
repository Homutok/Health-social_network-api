from django.contrib import admin
from .models import Person, PersonHealth, PersonPhoto, PersonAchievement

# Register your models here.

admin.site.register(Person)
admin.site.register(PersonHealth)
admin.site.register(PersonPhoto)
admin.site.register(PersonAchievement)
