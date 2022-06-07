from django.db import models


# Create your models here.
class Achievement(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    summary = models.CharField(max_length=1000, db_index=True)
    photo = models.FileField(upload_to='article/achievement_photo',blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
