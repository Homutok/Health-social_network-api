from django.contrib import admin
from django.contrib.auth.models import User
from Blog.models import Post
from django.db import models


# Register your models here.


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1, related_name='user_favourite')
    content_id = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='favourite_content')

    def __str__(self):
        return str(self.user)+"["+str(self.content_id)+"]"
