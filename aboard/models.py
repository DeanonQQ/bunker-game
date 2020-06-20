from django.db import models

# Create your models here.
class Ch(models.Model):
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    profession = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    shape = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
    fobies = models.CharField(max_length=200)
    inventory = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

class ActCard(models.Model):
    act = models.CharField(max_length=200)

class SituationEvent(models.Model):
    event = models.TextField()
    aboutb = models.CharField(max_length=200)
    timer = models.CharField(max_length=200)
    containb = models.CharField(max_length=200)
    