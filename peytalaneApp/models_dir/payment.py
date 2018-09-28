from django.db import models
from peytalaneApp.models_dir.user import User

class Payment_option(models.Model):
    name = models.CharField(max_length=50) 
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ":" + self.value


class Payment(models.Model):
    price = models.IntegerField()
    type_product = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    options = models.ManyToManyField(Payment_option,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)