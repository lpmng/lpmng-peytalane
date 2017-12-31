from django.db import models

# Create your models here.

class ValueOption(models.Model):
    value = models.CharField(max_length=50) # EX: oui / non / grande / petite ...

class Option(models.Model):
    name = models.CharField(max_length=50) # EX: taille / tomates ? / oignon ? ...
    values = models.ManyToManyField(ValueOption)

#templates will be food without user
class Food(models.Model):
    name = models.CharField(max_length=50) # EX : kebab, pizza 4 fromages, pizza carnivore...
    options = models.ManyToManyField(Option)
    user = models.CharField(max_length=100,blank=True, null=True) #Uid user in the core
    

