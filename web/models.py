from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Theatre(models.Model):
    
    name = models.CharField(max_length=100)
    date = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NUMBER_CHOISE= [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    ]
    YES_NO= [
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9')
    ]
    how_many = models.CharField(max_length=20, choices=NUMBER_CHOISE)
    place = models.CharField(max_length=100, default='I DONT KNOW.')
    score= models.CharField(max_length=20, choices=YES_NO, default="I DONT KNOW.")
    
    
    
class Cinema(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NUMBER_CHOISE= [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6')
    ]
    YES_NO= [
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9')
    ]
    how_many = models.CharField(max_length=20, choices=NUMBER_CHOISE)
    place = models.CharField(max_length=100, default="I DONT KNOW.")
    score= models.CharField(max_length=20, choices=YES_NO, default="I DONT KNOW.")