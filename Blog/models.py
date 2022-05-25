from django.db import models
from Person.models import Person
from Fitness.models import Fitness
from Recipe.models import Recipe


class Post(models.Model):
    post_name = models.CharField(max_length=100, db_index=True)
    post_summary = models.CharField(max_length=10000, db_index=True)
    post_author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='post_for_user')
    post_date = models.DateField(null=True, blank=True)
    post_tags = models.ManyToManyField('Tags')
    post_recipes = models.ManyToManyField(Recipe, null=True, blank=True)
    post_fitness = models.ManyToManyField(Fitness, null=True, blank=True)

    ALL = 'all'
    FITNESS = 'fitness'
    DIET = 'diet'
    TYPE_CHOICE = (
        (ALL, 'Все новости'),
        (FITNESS, 'Фитнес и спорт'),
        (DIET, 'Питание '),
    )
    post_type = models.CharField(max_length=50, choices=TYPE_CHOICE, blank=True, default='all',
                                     help_text='Тип '
                                               'новостей')

    def __str__(self):
        return self.post_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.tag_name
