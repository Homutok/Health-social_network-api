from django.contrib.auth.models import User
from django.db import models
from Blog.models import Post


# Comments
class Comment(models.Model):
    comment_text = models.CharField(max_length=200, db_index=True)
    comment_author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment_for_user')
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return f"{self.comment_text} - {self.comment_author}"