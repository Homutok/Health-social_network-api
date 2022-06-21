from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Fitness(models.Model):
    fitness_name = models.CharField(max_length=100, db_index=True)
    fitness_kcal = models.IntegerField(null=True, blank=True)
    fitness_time = models.IntegerField(null=True, blank=True)
    fitness_weight = models.IntegerField(null=True, blank=True)
    fitness_summary = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    fitness_author = models.ForeignKey(User, on_delete=models.PROTECT, default=1, related_name='fitness_for_user')
    fitness_preview = models.ImageField(upload_to='article/fit_photo', height_field=None, width_field=None, max_length=100,
                                        null=True, blank=True)

    def __str__(self):
        return self.fitness_name
