from django.db import models
from Person.models import Person
import datetime


# Create your models here.
class Purposes(models.Model):
    person_data = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, related_name='purposes_for_user')
    purpose_name = models.CharField(max_length=100, db_index=True)
    day_begin = models.DateField(null=True, blank=True)
    day_end = models.DateField(null=True, blank=True)

    def day_pass(self):
        return self.day_begin - datetime.datetime.today()

    def __str__(self):
        return '[' + str(self.person_data.id) + ']' + str(self.person_data.person_name) + '-' + str(self.id)


class PurposePause(models.Model):
    purpose = models.ForeignKey(Purposes, on_delete=models.PROTECT, null=True, related_name='purpose')
    day_pause = models.DateField(null=True, blank=True)
    pause_reason = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return str(self.day_pause) + '[' + str(self.pause_reason)  + ']'
