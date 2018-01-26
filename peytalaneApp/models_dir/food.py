from django.db import models
from peytalaneApp.models_dir.user import User

# Create your models here.


class ValueOption(models.Model):
    value = models.CharField(max_length=50) # EX: oui / non / grande / petite ...
    def __str__(self):
        return str(self.value)

class Option(models.Model):
    name = models.CharField(max_length=50) # EX: taille / tomates ? / oignon ? ...
    values = models.ManyToManyField(ValueOption)
    def __str__(self):
        return str(self.name)

class ValueIngredient(models.Model):

    value = models.CharField(max_length=50) # EX: tomates / poulet / chorizo ...
    def __str__(self):
        return str(self.value)
    
    
#templates will be food without user
class Food(models.Model):
    name = models.CharField(max_length=50) # EX : kebab, pizza 4 fromages, pizza carnivore...
    options = models.ManyToManyField(Option)
    ingredients = models.ManyToManyField(ValueIngredient)
    def __str__(self):
        return str(self.name)
    

class FoodBuy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
