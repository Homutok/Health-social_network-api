from django.contrib.auth.models import User
from django.db import models


class ToDoTask(models.Model):
    task_name = models.CharField(max_length=100, db_index=True, default='Error')
    task_summary = models.CharField(max_length=1000, db_index=True, default='error')
    task_author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='todo_for_user')
    complete_stage = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return str(self.task_name) + "[" + str(self.task_author) + "]"
