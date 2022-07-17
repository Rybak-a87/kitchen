from tkinter import CASCADE
from django.db import models


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    value = models.CharField(max_length=255)


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    value = models.CharField(max_length=255)


class Comment(models.Model): 
    user = models.ForeignKey(User, on_delete=CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(LikeDislike)
    active = models.BooleanField(default=True)