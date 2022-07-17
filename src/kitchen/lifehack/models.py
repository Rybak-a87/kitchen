from django.db import models


class LifeHack(models.Model):
    # photo = 
    title = models.CharField(max_length=255)
    description = models.TextField()
    # comments = 
    # grade =