from django.db import models
# Create your models here.

class Block(models.Model):
    difficulty = models.PositiveSmallIntegerField()
    extraData = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)