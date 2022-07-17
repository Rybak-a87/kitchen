from django.db import models


class Recipe(models.Model):
    # photo = models.ImageField()
    title = models.CharField(max_length=255)
    ingredient = models.ManyToManyField("Ingredient", related_name="recires")
    description = models.TextField()
    # grade = 
    # comment = 
    active = models.BooleanField(default=True)



class Ingredient(models.Model):
    # photo = 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)