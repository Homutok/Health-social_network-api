from django.contrib.auth.models import User
from django.db import models
from Fitness.models import Fitness

DAY_OF_THE_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1, related_name='user_workout')
    day = models.CharField(max_length=1, choices=DAY_OF_THE_WEEK, blank=True, default=1,
                           help_text='День недели')
    exercise = models.ForeignKey(Fitness, blank=True, on_delete=models.CASCADE, default=1,
                                related_name='user_exercise')
    def __str__(self):
        pass
