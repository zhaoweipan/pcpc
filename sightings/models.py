from django.db import models
from django.conf import settings
# Create your models here.

class Sightings(models.Model):
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Unique_Squirrel_Id = models.CharField(max_length=16)
    Shift = models.CharField(max_length=16)
    Date = models.CharField(max_length=16)
    Age = models.CharField(max_length=16)
    Primary_Fur_Color = models.CharField(max_length=128)
    Location =  models.CharField(max_length=128)
    Specific_Location = models.CharField(max_length=128)
    Running = models.NullBooleanField()
    Chasing = models.NullBooleanField()
    Climbing = models.NullBooleanField()
    Eating = models.NullBooleanField()
    Foraging = models.NullBooleanField()
    Other_Activities = models.CharField(max_length=128)
    Kuks = models.NullBooleanField()
    Quaas = models.NullBooleanField()
    Moans = models.NullBooleanField()
    Tail_flags = models.NullBooleanField()
    Tail_twitches = models.NullBooleanField()
    Approaches = models.NullBooleanField()
    Indifferent = models.NullBooleanField()
    Runs_from = models.NullBooleanField()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    