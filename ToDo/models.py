from django.db import models


# Create your models here.
from Person.models import Person


class ToDoTask(models.Model):
    task_name = models.CharField(max_length=1000, db_index=True)
    task_author = models.ForeignKey(Person, on_delete=models.PROTECT, default=1, related_name='todo_for_user')
    complete_stage = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return str(self.task_name) + "[" + str(self.task_author) + "]"
