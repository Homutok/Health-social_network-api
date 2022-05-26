from django.contrib.auth.models import User
from django.db import models
from Fitness.models import Fitness
from Recipe.models import Recipe


class Post(models.Model):
    post_name = models.CharField(max_length=100, db_index=True)
    post_summary = models.CharField(max_length=10000, db_index=True)
    post_author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='post_for_user')
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


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='likes')
    content_id = models.ForeignKey(Post,
                                   on_delete=models.CASCADE,
                                   related_name='likes_for_post')

    def __str__(self):
        return str(self.content_id) + " (" + str(self.user) + ")"
