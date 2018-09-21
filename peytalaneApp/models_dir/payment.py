from django.db import models


class Payment_option(models.Model):
    name = models.CharField(max_length=50) 
    value = models.CharField(max_length=50)

class Payment(models.Model):
    price = models.IntegerField()
    product = models.CharField(max_length=100)
    options = models.ManyToManyField(Payment_option)
