from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def post_count(self):
        return Post.objects.filter(topic__board=self).count()

    def last_post(self):
        return Post.objects.filter(topic__board=self).last()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_msg = Truncator(self.message)
        return truncated_msg.chars(20)









